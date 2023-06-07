import cv2
import numpy as np
import random

# Image dimensions
width, height = 800, 800

# Create a black background
image = np.zeros((height, width, 3), dtype=np.uint8)

# Circle center and radius
circle_center_x = width // 2
circle_center_y = height // 2
radius = 300

# Number of circles
num_circles = 100

# Circle effect speed
speed = 15

# Circle thickness
thickness = 4

# Gap between circles
gap = 4

# List of colors
colors = []

# Initial direction
direction = 1  # 1: Move right, -1: Move left

# Assign colors to circles
for i in range(num_circles):
    colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Draw circles in an infinite loop
while True:
    # Draw circles
    image = np.zeros((height, width, 3), dtype=np.uint8)  # Black background
    for i in range(num_circles):
        current_radius = i * (thickness + gap)
        cv2.circle(image, (circle_center_x, circle_center_y), current_radius, colors[i], thickness=thickness)

    # Display image
    cv2.imshow("LSD effect by ilkay eren", image)
    cv2.waitKey(1)

    # Change direction
    if circle_center_x >= width - radius:
        direction = -1  # Move left
    elif circle_center_x <= radius:
        direction = 1  # Move right

    # Update center position
    circle_center_x += direction * speed

    # Transfer colors
    colors.insert(0, colors.pop())

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the window
cv2.destroyAllWindows()
