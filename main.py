from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    photo = request.files['photo']
    filename = secure_filename(photo.filename)
    photo.save(filename )

    return 'foto zdes'


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
