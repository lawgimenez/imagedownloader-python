import requests

file = open("index.md", "r")
line = file.read()
print("Read = %s" % (line))