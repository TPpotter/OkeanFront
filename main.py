from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import foto
import os

app = Flask(__name__)


@app.route('/process_photo', methods=['POST'])
def process_photo():
    photo = request.files['photo']
    photo.save('to_model.jpg')
    data = foto.predict(f'C:/Users/User/Desktop/project/to_model.jpg')

    response = {'output': data}
    os.remove('C:/Users/User/Desktop/project/to_model.jpg')
    return jsonify(response)


@app.route('/')
def main():
    if request.method == 'GET':
        return render_template('base.html')


@app.route('/model')
def second():
    if request.method == 'GET':
        return render_template('model.html')


@app.route('/about')
def third():
    if request.method == 'GET':
        return render_template('about.html')


if __name__ == "__main__":
    app.run(host='localhost', port=8000)
