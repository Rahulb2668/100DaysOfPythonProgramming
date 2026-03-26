from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import fitz
from gtts import gTTS

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

def extract_text(path_pdf):
    doc = fitz.open(path_pdf)
    text = ""
    for page in doc:
        text+=page.get_text()
    return text


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == "POST":
        if 'pdf_file' not in request.files: 
            return jsonify({'error': 'No file'})
            
        file = request.files['pdf_file']
        
        if file.filename == '': 
            return jsonify({'error': 'No file'})
            
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            
            text = extract_text(path)
            
            gTTS(text=text, lang='en', slow=False).save("static/audio/output.mp3")
            
            audio_url = url_for('static', filename='audio/output.mp3')

            return jsonify({"message": "File uploaded successfully!", "audio_url": audio_url})

if __name__ == '__main__':
    app.run(debug=True)
