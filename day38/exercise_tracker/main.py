import os
import requests
from datetime import datetime

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
SHEETY_BARIER = f"Bearer {os.environ.get('SHEETY_BARIER')}"

GENDER = os.environ.get("GENDER")
WEIGHT_KG = os.environ.get("WEIGHT")
HEIGHT_CM = os.environ.get("HEIGHT")
AGE = os.environ.get("AGE")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/fc9cd75ee88d0a72206a50b5cd38fcf4/myWorkoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

today = datetime.now()
date = today.strftime('%d/%m/%Y')
time = today.strftime('%X')


def api_call(*args, **kwargs):
    endpoint = kwargs.get("endpoint")
    params = kwargs.get("params")
    method = kwargs.get("method")
    headers = kwargs.get("headers")

    response = requests.request(method, headers=headers, url=endpoint, json=params)
    response.raise_for_status()
    return response.json()


def get_exercises():
    exercise_headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    exercise_parameters = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    exercise_result = api_call(
        endpoint=exercise_endpoint, params=exercise_parameters, method="POST", headers=exercise_headers)
    return exercise_result["exercises"]


def add_to_sheet(exercises):
    if not exercises:
        return
    headers = {
        "Authorization": SHEETY_BARIER,
    }
    for exercise in exercises:
        workout_params = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        post_response = api_call(endpoint=sheety_endpoint, params=workout_params, method="POST", headers=headers)
        print("Added to sheet: ", post_response)


def main():
    add_to_sheet(get_exercises())


if __name__ == "__main__":
    main()


