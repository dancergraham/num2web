from flask import app
from num2words import num2words

from flask import Flask

app = Flask(__name__)


@app.route("/<int:number>")
def print_number(number):
    words = num2words(number,
                      lang="fr",
                      )
    return words


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
