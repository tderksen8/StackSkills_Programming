import bcrypt
from pymongo import MongoClient


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.Users.insert({"First Name": data.first_name, "Last Name": data.last_name, "Email": data.email,
                               "Password": hashed})
        print("uid is", id)

