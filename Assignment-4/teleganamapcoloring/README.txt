Here’s a clean, ready-to-use **README.md** for your project 👇

---

# 🗺️ Telangana Map Coloring using CSP

This project solves the **map coloring problem** for Telangana districts using a **Constraint Satisfaction Problem (CSP)** approach. It ensures that no two adjacent districts share the same color and generates a visual output.

---

## 🚀 Features

* Generic CSP implementation (reusable)
* Automatic adjacency detection from GeoJSON
* Backtracking search algorithm
* Map visualization with labeled districts
* Clean output image generation

---

## 📁 Project Structure

```
.
├── csp.py                      # CSP framework (Constraint + CSP classes)
├── main.py                     # Map coloring implementation
├── telangana_districts.geojson # Auto-downloaded file
├── telangana_colored_map.png   # Output image
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

**Linux / Mac:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

---

### 4. Install dependencies

```bash
uv pip install geopandas matplotlib shapely
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📥 What Happens

* Downloads Telangana GeoJSON (if not already present)
* Extracts district data
* Detects neighboring districts using geometry
* Applies CSP with constraints
* Solves using backtracking
* Generates a colored map

---

## 🖼️ Output

* File: `telangana_colored_map.png`
* Each district:

  * Has a color assigned
  * Does not share color with neighbors
  * Is labeled clearly

---

## 🧠 Concept

* **Variables** → Districts
* **Domains** → Colors
* **Constraints** → Adjacent districts must differ

---

## 🔧 Customization

* Change colors → edit `colors` list
* Use different regions → replace GeoJSON
* Improve performance → add heuristics (MRV, forward checking)

---

## 🐛 Troubleshooting

If `geopandas` fails to install:

```bash
pip install --upgrade pip wheel
```

On Linux:

```bash
sudo apt install gdal-bin libgdal-dev
```

---

## 📌 Future Improvements

* Add GUI or web interface
* Optimize CSP solving
* Support other maps


