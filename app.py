from flask import Flask, request, render_template, send_from_directory
import os
from preprocessing import process_image
from depth_estimation import estimate_depth
from create_3d_model import create_3d_model

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process the image and create a 3D model
        processed_image = process_image(filepath)
        depth_map = estimate_depth(filepath)
        x_range, y_range, z_range = create_3d_model(depth_map)

        return render_template('display.html', filename=filename, x_range=x_range, y_range=y_range, z_range=z_range)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
