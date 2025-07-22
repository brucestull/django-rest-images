#!/usr/bin/env python3
import requests
import os

URL = "http://localhost/images/"
FILE_PATH = "supplier-data/images/"

for file_name in os.listdir(FILE_PATH):
    if file_name.lower().endswith("jpeg"):
        with open(os.path.join(FILE_PATH, file_name), "rb") as file:
            response = requests.post(URL, files={"file": file})
            print(f"{file_name} -> {response.status_code}")
