class animal:
    def __init__(self, id=None, animal_type=None, name=None, age=None, breed=None, color=None, lost=None, found_by=None, lost_from=None):
        self.id = id
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.lost = lost
        self.animal_type = animal_type
        
        # Links to person class so contact information can be added
        self.found_by = found_by
        self.lost_from = lost_from
    
    def populate_from_sql(self):
        pass
    
