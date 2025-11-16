from flask import Flask, render_template, request
import cv2
import numpy as np
import easyocr
import os


# Ensure uploads folder exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

reader = easyocr.Reader(['en'])

def detect_number_plate(path):
    img = cv2.imread(path)
    img_copy = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 100, 200)
    gray_plate = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray_plate, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)


    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    

    plate = None
    for c in contours:
        per = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.03 * per, True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            plate = img[y:y+h, x:x+w]
            break

    if plate is None:
        return "PLATE NOT FOUND"


    result = reader.readtext(plate)
    extracted = ""
    for r in result:
        extracted += r[1] + " "

    return extracted.strip().replace(" ", "").upper()

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    if request.method == 'POST':
        file = request.files['image']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        text = detect_number_plate(file_path)

    return render_template('index.html', plate_text=text)

if __name__ == '__main__':
    app.run(debug=True)
