from sql_utils import *

db = sql_database()

"""
id = 10 charictar string unique to the animal contains ints, and lowercase letters
class will work without id but to relate data to SQL id will be required or generated

is_lost = bool
if the dog was found by someone will be false
if the dog was lost by someone will be true

name = lowercase string
species = lowercase string
breed = lowercase string
color = lowercase string
sex = "m", "f", "u" u for unknown
age = int estimate
owner = person class

date_seen = datetime object
this will be the date the animal was found or lost

location = ???
will be location animal was found or lost

description = long string upper and lower
will be user generated description of animal

image = ???
i want multiple images. i think creating an image folder class will make this easy but still work in progress
"""
class animal:
    def __init__(self, id=None, is_lost=None, name=None, species=None, breed=None, color=None, sex=None, age=None, owner=None, date_seen=None, location=None, description=None, image=None):
        self.id = id
        self.is_lost = is_lost
        self.name = name
        self.species = species
        self.breed = breed
        self.color = color
        self.sex = sex
        self.age = age
        self.owner = owner
        self.date_seen = date_seen
        self.location = location
        self.description = description
        self.image = image
        
        # Links to person class so contact information can be added
        self.found_by = found_by
        self.lost_from = lost_from
    
    def populate_from_sql(self):
        pass

    def save(self):
        db.save_animal(self)

        """
        if self.id is not None:
            db.save_animal(self)
        else:
            pass
        return "1235"
        """
    
