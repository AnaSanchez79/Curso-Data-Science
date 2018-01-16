import numpy as np
from os import listdir
import pandas as pd


estaciones = {"28079035":"Pza. del Carmen",
			  "28079004":"Pza. de España",
			  "28079039":"Barrio del Pilar",
			  "28079008":"Escuelas Aguirre",
			  "28079038":"Cuatro Caminos",
			  "28079011":"Av. Ramón y Cajal",
			  "28079040":"Vallecas",
			  "28079016":"Arturo Soria",
			  "28079017":"Villaverde Alto",
			  "28079018":"C/Farolillo",
			  "28079036":"Moratalaz",
			  "28079024":"Casa de Campo",
			  "28079027":"Barajas",
			  "28079047":"Méndez Álvaro",
			  "28079048":"Pº. Castellana",
			  "28079049":"Retiro",
			  "28079050":"Pza. Castilla",
			  "28079054":"Ensanche Vallecas",
			  "28079055":"Urb. Embajada(Barajas)",
			  "28079056":"Pza. Fdez. Ladreda",
			  "28079057":"Sanchinarro",
			  "28079058":"El Pardo",
			  "28079059":"Parque Juan Carlos I",
			  "28079060":"Tres Olivos"}

tecnicas = {"38":"Fluorencencia ultravioleta", 
			"48":"Absorción infrarroja",
			"08":"Absorción infrarroja",
			"47":"Microbalanza",
			"06":"Absorción ultravioleta",
			"59":"Cromatografía de gases",
			"02":"Ionización de llama"}

parametros = {"01":["Dióxido de Azufre", "SO2", "μg/m3"],
			  "06":["Monóxido de Carbono", "CO", "mg/m3"],
			  "07":["Monóxido de Nitrógeno", "NO", "μg/m3"],
			  "08":["Dióxido de Nitrógeno", "NO2", "μg/m3"],
			  "09":["Partículas < 2.5 μg", "PM2.5", "μg/m3"],
			  "10":["Partículas < 10 μg", "PM10", "μg/m3"],			  
			  "12":["Óxidos de Nitrógeno", "NOx", "μg/m3"],
			  "14":["Ozono", "O3", "μg/m3"],
			  "20":["Tolueno", "TOL","μg/m3"],
			  "30":["Benceno", "BEN", "μg/m3"],
			  "35":["Etilbenceno", "EBE", "μg/m3"],
			  "37":["Metalixeno", "MXY", "μg/m3"],
			  "38":["Paraxileno", "PXY", "μg/m3"],
			  "39":["Ortoxileno", "OXY", "μg/m3"],
			  "42":["Hidrocarburos totales (hexano)", "TCH", "mg/m3"],
			  "43":["Metano", "CH4", "mg/m3"],
			  "44":["Hidrocarburos no mecánicos (hexano)", "NMHC", "mg/m3"]}

DFparametros = pd.DataFrame(parametros)

#Funcion que lee los datos del archivo pasado por parámetro y los devuelve en una lista
def obtenerDatos(ruta, archivo):
    lista = np.genfromtxt(ruta +'/'+ archivo, delimiter=[8,2,2,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6], dtype='unicode',comments=None, names=None).tolist()
    #print(lista)
    return lista
    
lista_ficheros = listdir('04_datos_abiertos/dat/')
ruta = '04_datos_abiertos/dat/'

#en un for comprehesion llamar a una funcion que lea el archivo pasado por parametro y devuelva una lista
lista_resultado = [obtenerDatos(ruta,fichero) for fichero in lista_ficheros]

print(lista_resultado)
#res = pd.concat(objs = (pd.DataFrame(f) for f in lista_resultado),
#                keys = (n for n in range(len(lista_resultado))),
#                names = ['estacion'])

#res.reset_index(level = 0, inplace = True)
#res.reset_index(drop = True, inplace = True)

#print(res)








    
    
    