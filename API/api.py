from flask import Flask
from animal import *

app = Flask(__name__)

@app.route('/')
def hello():
    file = open("Client/index.html", "r")
    page = file.read()
    file.close()
    return page

@app.route("/animal_porfile/<animal_id>")
def animal_porfile(animal_id):
    file = open("Client/animal_profile.html", "r")
    page = file.read()
    page = page.format(id = animal_id)
    print(page)
    file.close()
    return page

@app.route('/animal/<animal_id>')
def get_animal(animal_id):
    requested = animal(id=animal_id)
    return requested.id


app.run(port=5500, debug=True)
