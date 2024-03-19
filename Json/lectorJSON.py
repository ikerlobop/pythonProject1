import json

# Abrir el archivo JSON
with open('datos.json') as archivo_json:
    # Cargar los datos del archivo en un diccionario
    datos = json.load(archivo_json)

# Imprimir los datos
print(datos)
