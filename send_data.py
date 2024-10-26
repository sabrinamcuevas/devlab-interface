import requests

def send_data(data):
    url = "http://0.0.0.0:80/api/v1/analysis/data" ##we need to create an API to process this info
    headers = {"Authorization": "Bearer tu_token", "Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print(f"Error sending data: {response.status_code}")
