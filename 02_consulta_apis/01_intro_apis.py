import requests

# Creamos la petición HTTP con GET:
r = requests.get("http://www.cartociudad.es/services/api/geocoder/reverseGeocode", params = {"lat":"36.9003409", "lon":"-3.4244838"})

print("Cuerpo de la respuesta = " + r.text)
print("Código HTTP del estado = " + str(r.status_code))
print("Cabeceras = " + str(r.headers))
