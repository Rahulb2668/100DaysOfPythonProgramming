from flask import Flask, render_template, request
from PIL import Image
import numpy as np


app = Flask(__name__)

def extract_colors(file):
    try: 
        img = Image.open(file)
        img = img.convert('RGB')
        img.resize((150, 10))
        img_array = np.array(img)
        reshaped = img_array.reshape(-1, 3)
        unique_colors, counts = np.unique(reshaped, axis=0, return_counts=True)
        sorted_indices = np.argsort(counts)[::-1]
        top_colors = unique_colors[sorted_indices[:10]]
        colors = []
        for color in top_colors:
            colors.append({
                'hex': '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2]),
                'rgb': 'rgb({}, {}, {})'.format(color[0], color[1], color[2])
            })
        return colors
    except Exception as e:
        print(e)
        return None         

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods= ["POST"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        if file and file.filename.endswith(('.png', '.jpg', '.jpeg')):
            extracted_colors = extract_colors(file)
            return render_template('index.html', colors=extracted_colors)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)