from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from animal import *
from person import *

def get_page(location):
    file = open(location, "r")
    page = file.read()
    file.close()
    return page

db = sql_database()
db.reset_database()
app = Flask(__name__)

# Sends to home page
@app.route('/')
def redriect_home():
    return redirect("/index.html", code=302)

# Home Page
@app.route('/index.html')
def index():
    page = get_page("Client/index.html")
    return page

# Opens Case Page to receive data about animal
@app.route('/new_case.html')
def new_case():
    page = get_page("Client/new_case.html")

    # This code will pre check a the box for lost or found depending on which link they use to get to the page
    is_lost = request.args.get('is_lost')
    if is_lost == "True":
        page = page.format(i_lost = "checked", i_found = "")
    elif is_lost == "False":
        page = page.format(i_lost = "", i_found = "checked")

    return page

# Receives information from new_case.html creates new animal and animal id and saves to database
@app.route('/create_new_case.html', methods=['POST', 'GET'])
def create_new_case():
    is_lost = request.args.get("anima_is_lost")
    name = request.args.get("animal_name")
    species = request.args.get("animal_species")
    sex = request.args.get('animal_sex')

    if is_lost == "True":
        is_lost = True
    else:
        is_lost = False
    
    if name == "":
        name = None
    else:
        name = name.lower()
        name = name.capitalize()
    
    if sex == "u":
        sex = None
    
    new_animal = animal(is_lost=is_lost, name=name, species=species, sex=sex)
    new_id = new_animal.save()
    return new_id


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

app.run(port=5500)
