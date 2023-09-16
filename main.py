import requests

app_id = "b6f87c55"
api_key = "bdf1147a0d5088c226d8981a07c1f80d"
api_endpoint_exercise = "https://trackapi.nutritionix.com/v2/natural/exercise"

# ------------------------------------------------------------------
height = "168.4"
gender = "male"
weight = "70.9"
age = "21"
query = input("Enter the Query : ")
# ------------------------------------------------------------------

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

req_body = {
    "query": query,
    "height": height,
    "weight": weight,
    "gender": gender,
    "age": age
}

responses = requests.post(url=api_endpoint_exercise, json=req_body, headers=headers)
result = responses.json()
print(result)

# <<-- Shetty Sheets -->>

api_endpoint_sheets = "https://api.sheety.co/phill/myWebsite/workout"

