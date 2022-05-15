import flask
from flask import Flask, render_template, request
from num2words import CONVERTER_CLASSES, num2words

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "num2web.html", languages=list(CONVERTER_CLASSES.keys()), name="bob"
    )


@app.route("/num2words/", methods=["POST"])
def print_number():
    if request.method == "POST":
        data = request.json
        number = float(data["number"])
        language = data["language"]
        words = num2words(
            number,
            lang=language,
        )
        return words


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
