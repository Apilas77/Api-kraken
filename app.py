from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    resultats = ""
    departements = ""
    station = ""
    station_pro = ""

    code_region = request.form.get("code_region")
    code_departement = request.form.get("code_departement")
    code_station = request.form.get("code_station")
    code_station_pro = request.form.get("code_station_pro")

    url_region = "https://geo.api.gouv.fr/regions/"
    url_departement = f"https://geo.api.gouv.fr/regions/{code_region}/departements"
    url_finale = f'https://hubeau.eaufrance.fr/api/v1/temperature/station?code_departement={code_departement}&pretty'
    url_station = f"https://hubeau.eaufrance.fr/api/v1/temperature/chronique?code_station={code_station}&size=5&sort=desc&pretty"
    url_station_pro = f"https://hubeau.eaufrance.fr/api/v1/temperature/chronique?code_station={code_station_pro}&size=5&sort=desc&pretty"
    try:
        response = requests.get(url_region)
    except requests.ConnectionError:
        return "Connection Error region"
    data_region = response.json()
    if request.method == "POST":
        try:
            response = requests.get(url_departement)
        except requests.ConnectionError:
            return "Connection Error department"
        departements = response.json()
    if request.method == "POST":
        try:
            resultats = requests.get(url_finale)
        except requests.ConnectionError:
            return "Connection Error results"
        resultats = resultats.json()
    if request.method == "POST" and code_station:
        try:
            station = requests.get(url_station)
        except requests.ConnectionError:
            return "Connection Error results"
        station = station.json()
    if request.method == "POST" and code_station_pro:
        try:
            station = requests.get(url_station_pro)
        except requests.ConnectionError:
            return "Connection Error results"
        station_pro = station.json()

    return render_template(
        "index.html",
        station=station,
        departements=departements,
        code_region=code_region,
        code_departement=code_departement,
        code_station=code_station,
        code_station_pro=station_pro,
        region=data_region,
        resultats=resultats,
        test=url_station
    )

@app.route("/")
def acceuil():
    return render_template("index.html", bodyId="index")

@app.route("/Actualites")
def Actualites():
    return render_template("Actualites.html")

@app.route("/Contact")
def Contact():
    return render_template("Contact.html", bodyId="contact")

if __name__ == "__main__":
    app.run(debug=True)
