import json

# Abrir el archivo JSON
with open('datos.json') as archivo_json:
    # Cargar los datos del archivo en un diccionario
    datos = json.load(archivo_json)

# En caso de querer solo un tipo de dato colocar variable
# y su correspondiente formateo en el print
# nombre = datos["nombre"]
# edad = datos["edad"]


# Imprimir los datos
print(datos)
