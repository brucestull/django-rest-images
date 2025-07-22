#!/usr/bin/env python3
import os
import requests

URL = "http://localhost/fruits/"
for desc in os.listdir("./supplier-data/descriptions/"):
    if desc.endswith(".txt"):
        with open(f"./supplier-data/descriptions/{desc}") as f:
            name, weight, *desc_lines = f.read().splitlines()
            payload = {
                "name": name,
                "weight": int(weight.split()[0]),
                "description": " ".join(desc_lines),
                "image_name": desc.replace(".txt", ".jpeg"),
            }
            r = requests.post(URL, json=payload)
            print(f"{name} -> {r.status_code}")
