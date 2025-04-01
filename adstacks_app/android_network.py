import requests
import json

class AndroidNetwork:
    def __init__(self , base_url = "https://127.0.0.1:8000/api/"):
        self.base_url = base_url

    def send_data(self , device_data):
        try:
            response =requests.post(
                f"{self.base_url}add-app/",
                data =json.dumps(device_data),
                headers ={"content-type":'application/json'}

            )
            return response.json()
        except Exception as e:
            return {"error" :str(e)}
        
