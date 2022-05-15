import flask
from flask import Flask, render_template
from num2words import num2words, CONVERTER_CLASSES

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("num2web.html",
                           languages=list(CONVERTER_CLASSES.keys()),
                           name="bob"
                           )


@app.route("/<language>/<int:number>")
def print_number(language, number):
    words = num2words(
        number,
        lang=language,
    )
    return words


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
