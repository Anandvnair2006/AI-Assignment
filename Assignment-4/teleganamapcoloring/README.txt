# 🗺️ Telangana Map Coloring using CSP (Constraint Satisfaction Problem)

## 📌 Overview

This project solves the **Map Coloring Problem** for the districts of Telangana using a **Constraint Satisfaction Problem (CSP)** approach.

The goal is to assign colors to each district such that:

* No two adjacent districts share the same color
* Minimum number of colors is used (4-color theorem)

The project also includes a **Flask web app** to visualize the colored map.

---

## 🚀 Features

* 🧠 CSP-based map coloring (Backtracking)
* 🖼️ Automatic region detection using OpenCV
* 🎨 District-wise coloring of map image
* 🌐 Flask web interface to display output
* ⚡ Works with any clean district outline map

---

## 🛠️ Technologies Used

* Python
* OpenCV (Image Processing)
* NumPy
* Flask (Web Framework)

---

## 📁 Project Structure

```
project/
│
├── app.py                # Flask backend
├── color_map.py         # CSP + image processing logic
├── telangana.png        # Input map (outline image)
│
├── static/
│   └── output.png       # Generated colored map
│
└── templates/
    └── index.html       # Frontend UI
```

---

## 📦 Installation

### 1. Clone or download the project

```bash
git clone <your-repo-url>
cd project
```

---

### 2. Install dependencies

```bash
pip install opencv-python numpy flask
```

---

## ▶️ How to Run

### Step 1: Add your map

Place your Telangana district outline image as:

```
telangana.png
```

✔ Recommended:

* Black boundaries
* Light/white background
* Clear district separation

---

### Step 2: Run Flask app

```bash
python app.py
```

---

### Step 3: Open browser

Go to:

```
http://127.0.0.1:5000/
```

---

### Step 4: View output

* The CSP algorithm runs automatically
* Colored map will be generated at:

```
static/output.png
```

* Displayed on the webpage

---

## 🧠 How It Works

### 1. Image Processing

* Convert image to grayscale
* Threshold to detect boundaries
* Extract district regions using contours

### 2. Graph Construction

* Each district = node
* Adjacency determined by contour proximity

### 3. CSP Solver

* Uses **Backtracking**
* Ensures no neighboring regions have same color

### 4. Visualization

* Each region is filled with assigned color
* Output saved as image

---

## 🎨 Color Scheme

* Blue
* Green
* Red
* Yellow

(You can modify colors in `color_map.py`)

---

## ⚠️ Notes / Limitations

* Accuracy depends on map quality
* Text labels inside regions may create noise
* Very thin borders may merge districts

---

## 💡 Future Improvements

* Use exact Telangana district adjacency graph
* Add district labels on output map
* Interactive UI (click districts)
* Better region segmentation

---

## 👨‍💻 Author

* Your Name

---

## ⭐ Acknowledgment

Based on classic **Map Coloring Problem (CSP)** from Artificial Intelligence.

