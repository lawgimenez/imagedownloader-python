import requests
import re

file = open("index.md", "r")
line = file.read()

results = re.findall(r'(https?://[^\s]+)', line)
print(results)