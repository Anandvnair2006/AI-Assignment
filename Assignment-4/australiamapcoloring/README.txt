# 🗺️ Australia Map Coloring using CSP (Flask)

This project implements the **Map Coloring Problem** using a **Constraint Satisfaction Problem (CSP)** approach with **Backtracking**.
It visualizes how different regions of Australia are colored such that no two adjacent regions share the same color.

---

## 🚀 Features

* 🎯 CSP Backtracking Algorithm
* 🗺️ Interactive Australia Map (SVG)
* ▶️ Step-by-step visualization
* ⚡ Run full animation
* 📊 Live statistics:

  * Assigned variables
  * Backtracks
  * Constraint checks
* 📜 Trace log of decisions

---

## 🧠 Problem Description

Regions:

* WA (Western Australia)
* NT (Northern Territory)
* SA (South Australia)
* QLD (Queensland)
* NSW (New South Wales)
* V (Victoria)
* T (Tasmania)

Constraint:

* No two neighboring regions can have the same color

Colors:

* Red
* Green
* Blue

---

## 🛠️ Tech Stack

* Backend: Python (Flask)
* Frontend: HTML, CSS, JavaScript
* Visualization: SVG

---

## 📁 Project Structure

```
map-coloring-csp/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/map-coloring-csp.git
cd map-coloring-csp
```

---

### 2. Install dependencies

```
pip install flask
```

---

### 3. Run the application

```
python app.py
```

---

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 🎮 How to Use

* **Step →**
  Executes one step of the backtracking algorithm

* **Run All**
  Automatically runs the full algorithm

* **Reset**
  Clears the map and restarts

---

## 🧩 Algorithm Used

Backtracking Search:

1. Select an unassigned region
2. Try assigning a color
3. Check constraints
4. If valid → continue
5. If conflict → backtrack

---

## ⚠️ Common Issues

### Buttons not working

* Ensure `script.js` is loaded only once

### Map not visible

* Check CSS contrast (dark-on-dark issue)

### JSON error

* Ensure `/api/solve` route returns valid JSON

---

## 📸 Preview

(Insert screenshot here)

---

## 🚀 Future Improvements

* 🌍 Real GeoJSON map rendering
* 🧠 Heuristics (MRV, Forward Checking)
* 🎨 User-driven coloring mode
* 📊 Graph visualization of constraints

---

## 👨‍💻 Author

Anand Nair

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

