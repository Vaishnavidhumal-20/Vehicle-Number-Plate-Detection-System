import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the image
img = cv2.imread("images/car.jpg")
img_copy = img.copy()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Edge detection
edges = cv2.Canny(blur, 100, 200)

# Step 5: Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

plate = None

# Step 6: Loop through contours to find number plate (rectangle area)
for c in contours:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.03 * perimeter, True)

    if len(approx) == 4:   # number plate is rectangular
        x, y, w, h = cv2.boundingRect(approx)
        plate = img[y:y+h, x:x+w]
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 3)
        break

# Step 7: Show results
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title("Edge Detection")
plt.imshow(edges, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("Detected Plate")
if plate is not None:
    plt.imshow(cv2.cvtColor(plate, cv2.COLOR_BGR2RGB))
else:
    plt.text(0.3, 0.5, "Plate not found", fontsize=18)

plt.show()

import easyocr

# Step 4: OCR Extraction
if plate is not None:
    reader = easyocr.Reader(['en'])  # English OCR
    result = reader.readtext(plate)

    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + " "

    # Cleaning the text
    extracted_text = extracted_text.strip().replace(" ", "").upper()
else:
    extracted_text = "Plate Not Found"


print("\nDetected Number Plate Text:", extracted_text)

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.title("Detected Number Plate Area")
if plate is not None:
    plt.imshow(cv2.cvtColor(plate, cv2.COLOR_BGR2RGB))
else:
    plt.text(0.3, 0.5, "Plate Not Found", fontsize=18)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Final Output")
plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
