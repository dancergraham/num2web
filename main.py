import flask
from flask import Flask, render_template
from num2words import num2words

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("num2web.html")


@app.route("/<int:number>")
def print_number(number):
    words = num2words(
        number,
        lang="fr",
    )
    response = flask.jsonify(data={"words": words})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:63342/')
    return words


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
