Here’s a clean **README.md** for your **Crypt-Arithmetic (SEND + MORE = MONEY) Web App** 👇

---

# 🔐 Crypt-Arithmetic Solver (Flask Web App)

This project solves the classic crypt-arithmetic puzzle:

```
  SEND
+ MORE
------
 MONEY
```

using a **Constraint Satisfaction Problem (CSP)** approach and presents the result in a clean **web UI built with Flask**.

---

## 🚀 Features

* 🧠 Solves crypt-arithmetic using permutations (CSP approach)
* 🔢 Ensures:

  * Unique digits for each letter
  * No leading zeros
  * Valid arithmetic equation
* 🎨 Modern UI with:

  * Equation display
  * Clean mapping visualization
  * Loading indicator
* ⚡ Fast solution generation

---

## 📁 Project Structure

```bash
crypto-csp/
│
├── app.py
├── solver/
│   └── crypto.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
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

### 2. Create virtual environment

```bash
uv venv
```

---

### 3. Activate environment

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

* Letters → Variables
* Digits (0–9) → Domain
* Constraints:

  * All digits must be unique
  * Leading digits ≠ 0
  * SEND + MORE = MONEY

The solver:

* Tries permutations of digits
* Checks constraints
* Returns the first valid solution

---

## 🎮 How to Use

1. Open the app in your browser
2. Click **Solve**
3. View:

   * ✅ Solved equation
   * 🔢 Letter → digit mapping

---

## 🐛 Troubleshooting

### App not starting?

```bash
uv pip install flask
```

---

### Port already in use?

Modify in `app.py`:

```python
app.run(debug=True, port=5001)
```

