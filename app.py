import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hi from flask application "

@app.route('/mainPage')
def hello():
    return 'you are in main page'
@app.route('/read_file')
def read_file():
    f = open("/data//home/user")
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
