# Create a class
class Person:
    # add the database ("db")
    db = "random_schema_name"
    # What `data` are we pulling for `self`?
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']