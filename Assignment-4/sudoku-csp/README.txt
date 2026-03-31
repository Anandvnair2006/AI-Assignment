Here’s a clean **README.md** for your **Sudoku CSP Web App** using Flask + uv 👇

---

# 🧩 Sudoku CSP Solver (Flask Web App)

This project is a **Sudoku Solver** built using a **Constraint Satisfaction Problem (CSP)** approach and deployed as a **Flask web application** with a clean UI.

---

## 🚀 Features

* 🧠 Backtracking-based CSP solver
* 🎯 Valid Sudoku constraint enforcement
* 🎨 Clean interactive UI (no arrows, proper grid)
* ⚡ Instant solve via backend API
* 🧹 Clear grid functionality

---

## 📁 Project Structure

```bash
sudoku-csp/
│
├── app.py
├── solver/
│   └── sudoku.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Setup Instructions (Using `uv`)

### 1. Install `uv`

```bash
pip install uv
```

---

### 2. Create a virtual environment

```bash
uv venv
```

---

### 3. Activate the environment

#### Linux / Mac:

```bash
source .venv/bin/activate
```

#### Windows:

```bash
.venv\Scripts\activate
```

---

### 4. Install dependencies

```bash
uv pip install flask
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 🌐 Open in Browser

Go to:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

* The frontend collects the Sudoku grid input
* Sends it to Flask via a POST request
* Backend solves using CSP (backtracking)
* Returns solution → displayed instantly

---

## 🎮 How to Use

1. Enter numbers (1–9) in the grid
2. Leave empty cells blank
3. Click **Solve**
4. View solved Sudoku instantly
5. Use **Clear** to reset

---

## 🐛 Troubleshooting

### App not starting?

Make sure Flask is installed:

```bash
uv pip install flask
```

---

### Port already in use?

Run with a different port:

```python
app.run(debug=True, port=5001)
```





