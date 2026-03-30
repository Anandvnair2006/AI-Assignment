var allSteps = []
var cursor = 0
var runTimer = null

// DOM refs
let statAssigned, statBacktracks, statSteps, statChecks
let traceLog, traceEmpty

// ───────── INIT ─────────
async function init() {
    try {
        const res = await fetch('/api/solve')
        const data = await res.json()

        allSteps = data.steps || []
        cursor = 0

        console.log("Loaded steps:", allSteps.length)

    } catch (err) {
        console.error(err)
        alert("Backend error")
    }
}

// ───────── APPLY STEP ─────────
function applyStep(step) {
    const assignment = step.assignment || {}

    // reset map
    document.querySelectorAll(".region").forEach(el => {
        el.setAttribute("class", "region")
    })

    // apply colors
    Object.keys(assignment).forEach(region => {
        const el = document.getElementById("r-" + region)
        if (el) {
            el.setAttribute("class", "region color-" + assignment[region])
        }
    })

    // update stats
    statAssigned.textContent = Object.keys(assignment).length
    statSteps.textContent = cursor

    if (step.backtracks !== undefined)
        statBacktracks.textContent = step.backtracks

    if (step.checks !== undefined)
        statChecks.textContent = step.checks

    // update trace
    addTrace(step)
}

// ───────── TRACE LOG ─────────
function addTrace(step) {
    traceEmpty.style.display = "none"

    const row = document.createElement("div")
    row.className = "trace-row"

    let text = ""

    if (step.type === "assign")
        text = `✓ ${step.region} = ${step.color}`

    else if (step.type === "conflict")
        text = `✗ conflict ${step.region} = ${step.color}`

    else if (step.type === "backtrack")
        text = `↩ backtrack ${step.region}`

    else if (step.type === "solved")
        text = "★ SOLUTION FOUND"

    row.innerText = text
    traceLog.appendChild(row)

    traceLog.scrollTop = traceLog.scrollHeight
}

// ───────── STEP ─────────
function step() {
    if (cursor >= allSteps.length) return

    applyStep(allSteps[cursor])
    cursor++
}

// ───────── RUN ALL ─────────
function runAll() {
    if (runTimer) return

    runTimer = setInterval(() => {
        if (cursor >= allSteps.length) {
            clearInterval(runTimer)
            runTimer = null
            return
        }
        step()
    }, 200)
}

// ───────── RESET ─────────
function reset() {
    cursor = 0

    if (runTimer) {
        clearInterval(runTimer)
        runTimer = null
    }

    document.querySelectorAll(".region").forEach(el => {
        el.setAttribute("class", "region")
    })

    statAssigned.textContent = 0
    statBacktracks.textContent = 0
    statSteps.textContent = 0
    statChecks.textContent = 0

    traceLog.innerHTML = ""
    traceEmpty.style.display = "block"
}

// ───────── DOM READY ─────────
document.addEventListener("DOMContentLoaded", () => {

    console.log("Visualizer ready")

    // buttons
    document.getElementById("btn-step").addEventListener("click", step)
    document.getElementById("btn-run").addEventListener("click", runAll)
    document.getElementById("btn-reset").addEventListener("click", reset)

    // stats
    statAssigned = document.getElementById("stat-assigned")
    statBacktracks = document.getElementById("stat-backtracks")
    statSteps = document.getElementById("stat-steps")
    statChecks = document.getElementById("stat-checks")

    // trace
    traceLog = document.getElementById("trace-log")
    traceEmpty = document.getElementById("trace-empty")

    init()
})
