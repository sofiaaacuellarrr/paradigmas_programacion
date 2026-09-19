import requests

nombre = input("Escribe un nombre: ")

url = f"https://api.agify.io?name={nombre}"
respuesta = requests.get(url)

print(respuesta.status_code)
print(respuesta.text)
