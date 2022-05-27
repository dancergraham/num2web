from flask import Flask, render_template, request
from langcodes import Language

from num2words import CONVERTER_CLASSES, num2words

app = Flask(__name__)


@app.route("/")
def home():
    """Render the single page template"""
    # handle inconsistencies between langcodes and num2words
    codes = {code: code for code in CONVERTER_CLASSES.keys()}
    codes["cz"] = "cs-cz"
    codes["dk"] = "da"
    codes["kz"] = "kk"
    languages = {
        num2word_code: Language.get(lang_code).autonym()
        for num2word_code, lang_code in codes.items()
    }
    return render_template(
        "num2web.html",
        languages=languages,
    )


@app.route("/num2words/", methods=["POST"])
def print_number():
    """Endpoint for the num2words service."""
    if request.method == "POST":
        data = request.json
        number = float(data["number"])
        language = data["language"]
        words = num2words(
            number,
            lang=language,
        )
        return words.capitalize()


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
