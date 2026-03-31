const grid = document.getElementById("grid");

// Create grid
for (let i = 0; i < 81; i++) {
    const input = document.createElement("input");
    input.type = "text";          // ✅ no arrows
    input.maxLength = 1;

    // Only allow 1-9
    input.addEventListener("input", () => {
        if (!/^[1-9]$/.test(input.value)) {
            input.value = "";
        }
    });

    grid.appendChild(input);
}

// Solve Sudoku
function solveSudoku() {
    const inputs = document.querySelectorAll("#grid input");
    let board = [];

    for (let i = 0; i < 9; i++) {
        let row = [];
        for (let j = 0; j < 9; j++) {
            let val = inputs[i*9 + j].value;
            row.push(val ? parseInt(val) : 0);
        }
        board.push(row);
    }

    fetch("/solve", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({board})
    })
    .then(res => res.json())
    .then(data => {
        if (data.solution) {
            data.solution.flat().forEach((v, i) => {
                inputs[i].value = v;
            });
        } else {
            alert("No solution found!");
        }
    });
}

// Clear grid
function clearGrid() {
    document.querySelectorAll("#grid input").forEach(i => i.value = "");
}
