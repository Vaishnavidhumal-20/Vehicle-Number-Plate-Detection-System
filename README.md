📌 Project Overview

This project allows users to upload an image of a vehicle, detects the number plate using OpenCV, extracts the text from the plate using EasyOCR, and displays the results through a Flask web interface.
It also visualizes detection steps using Matplotlib.

🚀 Features

📤 Upload vehicle image via Flask web interface

🔍 Detect number plate using OpenCV

🖼️ Preprocess image (grayscale, blur, edge detection)

🧊 Contour detection to locate number plate

🔠 Text extraction using EasyOCR

📊 Detection visualization using Matplotlib

📁 Save detected plates and results

⚡ Fast and efficient detection pipeline

🛠️ Technologies Used

Python 3.x

Flask – Web framework

OpenCV (cv2) – Image processing

EasyOCR – Text extraction

NumPy – Image array operations

Matplotlib – Visualization

Werkzeug – File handling

📂 Project Structure
vehicle-number-plate-detection/
│
├── app.py
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── models/
│   └── (optional saved results)
│
├── utils/
│   └── detection.py
│
├── README.md
└── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/vehicle-number-plate-detection.git
cd vehicle-number-plate-detection

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Application

Start the Flask server:

python app.py


Then open the browser:

http://127.0.0.1:5000


Upload a vehicle image → The app will detect and display:

Number plate bounding box

Extracted text

Processed image visuals

🧩 Detection Pipeline
✔ Step 1: Load Image

Read using OpenCV:

img = cv2.imread(file_path)

✔ Step 2: Preprocessing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blur, 50, 150)

✔ Step 3: Find Number Plate Contour
contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

✔ Step 4: Extract Text using EasyOCR
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_plate)

✔ Step 5: Display with Matplotlib
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

📊 Example Output
Detected Number Plate: MH12AB3456
Confidence: 92.3%
Image saved in /static/uploads/
