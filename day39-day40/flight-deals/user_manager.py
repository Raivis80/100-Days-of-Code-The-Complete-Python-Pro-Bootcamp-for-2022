import os
import requests
from user_data import UserData

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_USERS_ENDPOINT = f"{SHEETY_ENDPOINT}/users"


class UserManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.user_data = {}
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('SHEETY_API_KEY')}"
        }

    def get_users(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.user_data = data["users"]
        return self.user_data

    def create_user(self):
        print("Welcome to Flight Club.")
        print("We find the best flight deals and email you.\n")
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email = input("What is your email?\n")
        repeat_email = input("Type your email again.\n")

        if email != repeat_email:
            print("Emails don't match. Please try again.")
            return self.create_user()

        user_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        response = requests.post(
            url=SHEETY_USERS_ENDPOINT,
            json=user_data,
            headers=self.headers
            )
        response.raise_for_status()
        print(f"Your email {email} was added to the Flight Club.")

    def get_user_by_email(self, email):
        self.get_users()
        for user in self.user_data:
            if user["email"] == email:
                return UserData(**user)
        return None
