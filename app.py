import requests

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    url = 'https://hubeau.eaufrance.fr/api/v1/temperature/station?code_departement=45&pretty'
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        return "Connection Error"
    data = response.json()

    return render_template("index.html.jinja2", data=data)


if __name__ == "__main__":
    app.run(debug=True)
