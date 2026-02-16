import os  # <--- TAMBAHKAN BARIS INI
from flask import Flask, render_template, send_from_directory, jsonify

# Konfigurasi agar tidak butuh folder templates (mengacu pada percakapan sebelumnya)
app = Flask(__name__, template_folder='.')

IMAGE_FOLDER = r"D:\1\PYTHON\input"
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg'}
MAX_FILES = 15

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/images')
def get_images():
    # Sekarang baris ini tidak akan error lagi karena 'os' sudah di-import
    if not os.path.exists(IMAGE_FOLDER):
        return jsonify({"files": []})
    
    files = [f for f in os.listdir(IMAGE_FOLDER) 
             if os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS]
    files.sort()
    return jsonify({"files": files[:MAX_FILES]})

@app.route('/image/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)