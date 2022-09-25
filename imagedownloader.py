import requests
import re

file = open("index.md", "r")
line = file.read()

results = re.findall(r'(https?://[^\s]+)', line)

for result in results:
	indexOfPng = result.find("?")
	updatedResult = result[:indexOfPng]
	print(updatedResult)
