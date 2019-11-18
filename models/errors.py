
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
