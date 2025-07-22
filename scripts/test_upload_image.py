#!/usr/bin/env python3
import requests

url = "http://localhost:8000/images/"

# Path to your local image file
file_path = "../test_images/test_image_717_482.jpeg"

with open(file_path, "rb") as image_file:
    files = {"file": image_file}
    response = requests.post(url, files=files)

print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
