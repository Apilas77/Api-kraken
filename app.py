from flask import Flask, render_template
import requests, json
#from jinja2 import Template

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
@app.route("/Acceuil")
def acceuil():
    return render_template("Acceuil.html")

@app.route("/Actualités")
def Actualités():
    return render_template("Actualités.html")

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")

if __name__ == "__main__":
    app.run(debug=True)
