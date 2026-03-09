import requests
import pyfiglet

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print(response.status_code)
print(response.json())

text = pyfiglet.figlet_format("HELLO")
print(text)