class person:
    def __init__(self, id=None, name_first=None, name_last=None, phone_number=None, email=None, found_animals=None, lost_animals=None):
        self.id = id
        self.name_first = name_first
        self.name_last = name_last
        self.phone_number = phone_number
        self.email = email

        # Links to animal object
        self.found_animals = found_animals
        self.lost_animals = lost_animals

    def populate_from_sql():
        pass

    def populate_from_form():
        pass

    def populate_from_json():
        pass

    def convert_to_json():
        pass