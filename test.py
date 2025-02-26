import requests

url = "http://127.0.0.1:5000/predict"
data = {"url": "https://amzn.in/d/acC95Xh"}

response = requests.post(url, json=data)
print(response.json())  # Should return predictions
 
