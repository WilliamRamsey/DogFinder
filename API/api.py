from flask import Flask
from flask import request
from flask import render_template
from animal import *
from person import *

def get_page(location):
    file = open(location, "r")
    page = file.read()
    file.close()
    return page

app = Flask(__name__)

# Home Page
@app.route('/index.html')
def index():
    page = get_page("Client/index.html")
    return page

# Opens Case Page to receive data about animal
@app.route('/new_case.html')
def new_case():
    lost = request.args.get('lost')
    print(lost)
    page = get_page("Client/new_case.html")
    return page

# Receives information from new_case.html creates new animal and animal id and saves to database
@app.route('/create_new_case.html', methods=['POST', 'GET'])
def create_new_case():
    lost = request.args.get()
    print(lost)
    return lost


@app.route("/animal_porfile/<animal_id>")
def animal_porfile(animal_id):
    file = open("Client/animal_profile.html", "r")
    page = file.read()
    page = page.format(id = animal_id)
    file.close()
    return page

@app.route('/animal/<animal_id>')
def get_animal(animal_id):
    requested = animal(id=animal_id)
    return requested.id


app.run(port=5500, debug=True)
