from flask import Flask
from flask import render_template
from vote_data import get_votes

app = Flask(__name__)


@app.route("/")
def home():
    votos = get_votes()
    return render_template("main.html", votos=votos)


if __name__ == "__main__":
    app.run(debug=True)
