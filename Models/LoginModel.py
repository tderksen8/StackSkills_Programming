import bcrypt
from pymongo import MongoClient


class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def check_user(self, data):
        user_email = self.Users.find_one({"email": data.email})
        if user_email:
            if bcrypt.checkpw(data.password.encrypt(), user_email["password"]):
                return user_email
            else:
                return False

        else:
            return False

