import requests

url = 'http://localhost:5000/upload'

file_path = './cube.stl' #replace with user file
files = {'file': open(file_path, 'rb')}
response = requests.post(url, files=files)