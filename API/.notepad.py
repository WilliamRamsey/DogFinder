from animal import *
from sql_utils import *
from person import *

db = sql_database()
db.reset_database()

test_animal = animal(is_lost=False, name="Rudolf", species="dog", )

db.save_animal()
