from flask import Flask, render_template
import requests, json
#from jinja2 import Template


app = Flask(__name__)
#with open("index.html") as file_:
    #template = Template(file_.read())

@app.route("/")
def index():
    r = requests.get('https://hubeau.eaufrance.fr/api/v1/temperature/station?code_departement=45&pretty')
    return render_template("index.html")

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


