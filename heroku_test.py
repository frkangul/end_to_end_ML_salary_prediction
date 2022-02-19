import requests

data = {
    "age": 43,
    "workclass": "Federal-gov",
    "education": "Masters",
    "marital_status": "Married-civ-spouse",
    "occupation": "Adm-clerical",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "hours_per_week": 60,
    "native_country": "United-States"
}
r = requests.post('https://ml-heroku-fastapi.herokuapp.com/', json=data)

assert r.status_code == 200

print(f"Response code: {r.status_code}")
print(f"Response body: {r.json()}")
