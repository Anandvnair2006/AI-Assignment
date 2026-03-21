const rows = 70;
const cols = 70;

let grid = [];
let start = null;
let goal = null;
let mode = "obstacle";

const gridDiv = document.getElementById("grid");

function setMode(m) {
    mode = m;
}

function createGrid() {
    gridDiv.innerHTML = "";
    for (let r = 0; r < rows; r++) {
        grid[r] = [];
        for (let c = 0; c < cols; c++) {
            const cell = document.createElement("div");
            cell.className = "cell";
            cell.dataset.row = r;
            cell.dataset.col = c;
            cell.addEventListener("click", handleClick);
            gridDiv.appendChild(cell);
            grid[r][c] = 0;
        }
    }
}

function handleClick() {
    const r = parseInt(this.dataset.row);
    const c = parseInt(this.dataset.col);

    if (mode === "start") {
        document.querySelectorAll(".start").forEach(e => e.classList.remove("start"));
        this.classList.add("start");
        this.classList.remove("obstacle"); 
        start = [r, c];
        grid[r][c] = 0; 
    } else if (mode === "goal") {
        document.querySelectorAll(".goal").forEach(e => e.classList.remove("goal"));
        this.classList.add("goal");
        this.classList.remove("obstacle");
        goal = [r, c];
        grid[r][c] = 0;
    } else {
        if (!this.classList.contains("start") && !this.classList.contains("goal")) {
            this.classList.toggle("obstacle");
            grid[r][c] = grid[r][c] === 1 ? 0 : 1;
        }
    }

    clearPath();
    if (start && goal) {
        findPath(); // Dynamic replanning on every click
    }
}

function generateObstacles(density) {
    if (!start || !goal) {
        alert("Please place a Start and Goal node first.");
        return;
    }

    // Clear old obstacles
    document.querySelectorAll(".obstacle").forEach(e => e.classList.remove("obstacle"));
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            grid[r][c] = 0;
        }
    }

    // Generate new obstacles based on density
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            // Protect start and goal nodes
            if ((r === start[0] && c === start[1]) || (r === goal[0] && c === goal[1])) {
                continue;
            }
            if (Math.random() < density) {
                grid[r][c] = 1;
                let index = r * cols + c;
                gridDiv.children[index].classList.add("obstacle");
            }
        }
    }
    
    clearPath();
    findPath();
}

function clearPath() {
    document.querySelectorAll(".path").forEach(e => e.classList.remove("path"));
}

async function findPath() {
    const res = await fetch("/find_path", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ grid: grid, start: start, goal: goal })
    });

    const data = await res.json();
    
    if (data.path) {
        drawPath(data.path);
        document.getElementById("metrics").innerText = 
            `Path Length: ${data.path.length} | Nodes Explored: ${data.nodes} | Execution Time: ${data.time} ms`;
    } else {
        document.getElementById("metrics").innerText = 
            `No valid path found! | Nodes Explored: ${data.nodes} | Execution Time: ${data.time} ms`;
    }
}

function drawPath(path) {
    for (let p of path) {
        let index = p[0] * cols + p[1];
        let cell = gridDiv.children[index];
        if (!cell.classList.contains("start") && !cell.classList.contains("goal")) {
            cell.classList.add("path");
        }
    }
}

function resetGrid() {
    start = null;
    goal = null;
    createGrid();
    document.getElementById("metrics").innerText = "Path Length: 0 | Nodes Explored: 0 | Execution Time: 0 ms";
}

// Initialize the grid on page load
createGrid();
