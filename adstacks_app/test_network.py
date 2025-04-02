from android_network import AndroidNetwork

network = AndroidNetwork(base_url ="https://127.0.0.1:8000/api/")

device_data ={
    "app_name":"test_app",
    "version":5.0,
    "description":"this is test data"
}

response = network.send_data(device_data)
print("server response:" , response)