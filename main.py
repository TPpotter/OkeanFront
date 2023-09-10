from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    if request.method == 'GET':
        return render_template('base.html')


if __name__ == "__main__":
    app.run(host='localhost', port=8000)
