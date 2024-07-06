#!/usr/bin/env python3

from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No image part", 400
    
    file = request.files['image']
    
    if file.filename == '':
        return "No selected file", 400
    
    input_image = Image.open(file)
    output_image = remove(input_image)

    img_byte_arr = io.BytesIO()
    output_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return send_file(img_byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
