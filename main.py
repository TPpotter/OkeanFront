from flask import Flask, render_template, request

app = Flask(__name__)


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
