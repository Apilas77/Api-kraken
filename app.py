from flask import Flask
from jinja2 import Template


app = Flask(__name__)
with open("index.html.jinja2") as file_:
    template = Template(file_.read())

@app.route("/")
def hello():
    return template.render()

if __name__ == "__main__":
    app.run(debug=True)
