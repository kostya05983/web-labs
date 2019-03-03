from pymongo import MongoClient


class CookStorage:
    COOKIES = 'cgi-bin/cookies.json'
    db = None

    def __init__(self):
        client = MongoClient('172.17.0.2', 27017)
        self.db = client["cook"]
        self.users = self.db['users']

    def set_cookie_result(self, session, key, value):
        user = self.users.find_one({"session": session})
        if user is not None:
            user[key] = value
            self.users.save(user)
        else:
            user = {
                "session": session,
                key: value
            }
            self.users.insert(user)

    def find_cookie_session(self, session, key):
        user = self.users.find_one({"session": session})
        if user is None:
            return None
        return user[key]
