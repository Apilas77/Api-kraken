from flask import Flask
import requests, json
from jinja2 import Template


app = Flask(__name__)
with open("index.html.jinja2") as file_:
    template = Template(file_.read())

@app.route("/")
def index():
    r = requests.get('https://hubeau.eaufrance.fr/api/v1/temperature/station?code_departement=45&pretty')
    return template.render(r.json())


if __name__ == "__main__":
    app.run(debug=True)


