from flask import *
from flask import render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)