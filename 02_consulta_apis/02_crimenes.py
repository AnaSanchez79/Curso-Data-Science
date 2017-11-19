import requests
import json

#Obtención de información del lugar al que pertenecen las coordenadas lat:51.4965946 y lon:-0.1436476
r = requests.get("http://nominatim.openstreetmap.org/reverse", params = {"format":"jsonv2","lat":"51.4965946", "lon":"-0.1436476"})

#Obtención de los crímenes cercanos a las coordenadas lat:51.4965946 y lon:-0.1436476 en Abril 2017
r1 = requests.get("https://data.police.uk/api/crimes-at-location", params = {"date":"2017-04", "lat":"51.4965946", "lng":"-0.1436476"})

#Utilizo la librería json para poder tratar la respuesta
crimenes = json.loads(r1.text)

#Diccionario vacío en el que se guardarán las categorías de los crímenes (claves) y los contadores de cada uno (valores)
conteo_crimen_categoria = {}

#Recorro los crímenes
for crimen in crimenes: 
    #Si el crimen ya existe en el diccionario incremento su valor, si no existe lo añado con valor 1
    if crimen["category"] in conteo_crimen_categoria.keys():
        conteo_crimen_categoria[crimen["category"]] = conteo_crimen_categoria[crimen["category"]] + 1
    else:
        conteo_crimen_categoria[crimen["category"]] = 1
#Imprimo el diccionario
print(conteo_crimen_categoria)