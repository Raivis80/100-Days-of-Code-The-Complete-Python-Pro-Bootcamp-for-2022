class UserData:
    """This class is responsible for holding user data."""
    def __init__(self, **kwargs):
        self.first_name = kwargs["firstName"]
        self.last_name = kwargs["lastName"]
        self.email = kwargs["email"]
        self.id = kwargs["id"]