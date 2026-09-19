import requests

nombre = input("Escribe un nombre: ")

url = f"https://api.agify.io?name={nombre}"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()

    nombre_consultado = datos["name"]
    edad = datos["age"]
    cantidad = datos["count"]

    print("\nResultado de la API")
    print(f"Nombre consultado: {nombre_consultado}")
    print(f"Edad estimada: {edad}")
    print(f"Cantidad de registros analizados: {cantidad}")
else:
    print("No se pudo consultar la API.")
    