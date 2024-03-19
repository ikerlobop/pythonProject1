import requests
from bs4 import BeautifulSoup

# Diccionario para almacenar las siglas y su significado
diccionario_siglas = {}

# Lista de siglas a consultar
lista_siglas = ["PT", "PDT", "LAH"]

# URL de la página web con las siglas de instrumentación
url_siglas = "https://blog.ansi.org/ansi-isa-5-1-2022-instrumentation-symbols/"

# Función para obtener el significado de una sigla
def obtener_significado(sigla):
  # Petición a la página web
  response = requests.get(url_siglas)

  # Parseo del HTML
  soup = BeautifulSoup(response.content, "html.parser")

  # Búsqueda de la sección con la información de la sigla
  seccion_sigla = soup.find("div", class_="rte-table rte-table-border")

  # Si la sección no se encuentra, se retorna un mensaje de error
  if seccion_sigla is None:
    return "Sigla no encontrada"

  # Obtención del significado de la sigla
  significado = seccion_sigla.find("td", class_="rte-table-cell").text

  # Retorno del significado
  return significado.strip()

# Consulta del significado de cada sigla
for sigla in lista_siglas:
  significado = obtener_significado(sigla)
  diccionario_siglas[sigla] = significado

# Impresión del diccionario
print(diccionario_siglas)