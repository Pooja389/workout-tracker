import requests
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("api_id")
API_KEY = os.getenv("api_key")
print(APP_ID)
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("sheet_url")

exercise_text = input("tell me which exercise you did :")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = { "query" : exercise_text,
          "gender": "female",
          "height_cm" : "160",
          "weight_kg" : "47",
          "age" : 18,

}
response = requests.post(url = exercise_endpoint,headers=headers,json=params )
result = response.json()

today_date = dt.datetime.now().strftime("%d%m%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout" : {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]}
    }
header = {"Authorization": os.getenv("auth")}

response_ = requests.post(url=sheet_endpoint,json=sheet_input,headers=header)
print(response_.json())


