import requests
import re
import os
from urllib.parse import urlparse
from urllib.request import urlopen

file = open("index.md", "r")
line = file.read()

results = re.findall(r'(https?://[^\s]+)', line)

for result in results:

	# Filter only Wordpress domains
	if "wordpress.com" in result:
		# print(result)
		# Create folder
		if not os.path.exists("images"):
			os.makedirs("images")

		# Remove unnecessary characters in the URL
		indexOfPng = result.find("?")
		updatedResult = result[:indexOfPng]
		# print(updatedResult)

		# Get the filename
		parse = urlparse(result)
		filename = os.path.basename(parse.path)

		# Create a file path
		filePath = os.path.join("images", filename)
		print(filePath)

		request = requests.get(updatedResult)
		with open(filePath, "wb") as file:
			file.write(request.content)
