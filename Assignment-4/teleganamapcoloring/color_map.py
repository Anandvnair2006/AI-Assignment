import cv2
import numpy as np

# Colors (BGR for OpenCV)
COLORS = [
    (255, 0, 0),    # Blue
    (0, 255, 0),    # Green
    (0, 0, 255),    # Red
    (0, 255, 255)   # Yellow
]

# Load image
img = cv2.imread("telangana.png")
original = img.copy()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold to get boundaries
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# Find contours (district-like regions)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours (ignore tiny ones like text)
regions = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:   # adjust if needed
        regions.append(cnt)

print("Detected regions:", len(regions))

# ---- CSP Coloring ----
n = len(regions)
graph = {i: [] for i in range(n)}

# Detect adjacency (if contours touch)
def are_adjacent(c1, c2):
    for p1 in c1:
        for p2 in c2:
            if np.linalg.norm(p1 - p2) < 3:
                return True
    return False

# Build graph
for i in range(n):
    for j in range(i + 1, n):
        if are_adjacent(regions[i], regions[j]):
            graph[i].append(j)
            graph[j].append(i)

# Backtracking coloring
assignment = [-1] * n

def is_safe(node, color):
    for neighbor in graph[node]:
        if assignment[neighbor] == color:
            return False
    return True

def solve(node=0):
    if node == n:
        return True

    for c in range(len(COLORS)):
        if is_safe(node, c):
            assignment[node] = c
            if solve(node + 1):
                return True
            assignment[node] = -1

    return False

solve()

# ---- Fill regions ----
output = original.copy()

for i, cnt in enumerate(regions):
    color = COLORS[assignment[i]]
    cv2.drawContours(output, [cnt], -1, color, thickness=-1)

# Save result
cv2.imwrite("output.png", output)

print("✅ Colored map saved as output.png")
