
class Error():
    pass

class UsernameNotGiven(Error):
    def __init__(self):
        self.message = "username not given"

class UsernameNotFound(Error):
    def __init__(self):
        self.message = "username not found"

class IncorrectPassword(Error):
    def __init__(self):
        self.message = "incorrect password"

class ItemNotFound(Error):
    def __init__(self):
        self.message = "item with given id not found"

class InvalidToken(Error):
    def __init__(self):
        self.message = "Invalid token"
