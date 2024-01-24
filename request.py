import requests,json

# endpoint = "http://127.0.0.1:7000/api/postCarjson/"

data = {
    "model":"Creta",
    "company":"Hyundai"
}
jsonData = json.dumps(data)
# print(type(data), type(jsonData))
# resp = requests.post(url = endpoint,json=jsonData)
# print(resp.json())

endpoint = "http://127.0.0.1:8000/api/updateCar/10"

resp = requests.post(url = endpoint, json=jsonData)