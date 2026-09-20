import requests

while True:
    nombre = input("Escribe un nombre o escribe salir para terminar: ").strip().lower()

    if nombre == "salir":
        print("Programa finalizado.")
        break

    if nombre:
        if nombre.isalpha():
            url = f"https://api.agify.io?name={nombre}"
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()

                nombre_consultado = datos.get("name", "No disponible")
                edad = datos.get("age", "No disponible")
                cantidad = datos.get("count", "No disponible")

                print("\nResultado de la API")
                print(f"Nombre consultado: {nombre_consultado}")
                print(f"Edad estimada: {edad}")
                print(f"Cantidad de registros analizados: {cantidad}\n")
            else:
                print("No se pudo consultar la API.\n")
        else:
            print("El nombre solo debe contener letras.\n")
    else:
        print("Debes escribir un nombre para consultar la API.\n")