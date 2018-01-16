import re
import pandas as pd
import requests
import zipfile
import shutil
from os import listdir
from os import remove

#Variables para indicar la primera linea a leer en el excel dependiendo del año
first_row_data_default = 3
first_row_data_exceptions = {'1998': 2, '2009': 2, '2012': 4, '2013': 4, '2014': 4, '2015': 4}


def get_year(nombre_fichero):
    """
        Funcion que devuelve a que año pertenece al fichero excel
    """
    year = int(re.findall('\d{2}', nombre_fichero)[0])
    if year >= 90:
        return year + 1900
    elif year < 90:
        return year + 2000

def get_first_row(year_file):
     """
        Funcion que devuelve en que linea comienzan los datos del excel dependiendo del año
     """
     if year_file in first_row_data_exceptions:
        return first_row_data_exceptions[year_file]
     else:
         return first_row_data_default
        
def read_population(path, year):
    """
        Funcion que devuelve un dataframe con los datos del excel pasado por parametro
    """
    #Obtenemos la primera linea a leer del excel
    skip = get_first_row(year)
    #Leemos el excel y lo guardamos en un dataframe
    df = pd.read_excel(path, skiprows=skip)
    
    #Dependiendo del numero de columnas sabemos que los datos que nos interesan están en diferentes columnas
    if len(df.columns) == 6:
        df_filtrado = df.iloc[:,[0,1,3]]
    else:
        df_filtrado = df.iloc[:,[0,2,4]]
    
    #Le datos nombre a las columnas y devolvemos el dataframe
    df_filtrado.columns = ['cod_provincia', 'cod_municipio', 'poblacion']
    
    return df_filtrado

def download_population():
    """
        Funcion que descarga y descomprime el zip de archivos con la informacion de poblacion mundial
        de varios años.
        Lee los ficheros seleccionando las columnas que nos interesan de cada archivo, junta los datos 
        en un dataframe y finalmente guarda los datos en un csv.
    """
    #Descarga del zip
    print('Descargando ZIP...')
    url_archivo = 'http://www.ine.es/pob_xls/pobmun.zip'
    ruta_excels = '05_lectura_excel/pobmun/'
    r = requests.get(url_archivo)
    with open("05_lectura_excel/pobmun.zip", "wb") as code:
        code.write(r.content)
        
    #Descomprime el zip
    print('Descomprimiendo ZIP')
    zf=zipfile.ZipFile("05_lectura_excel/pobmun.zip", "r")
    for i in zf.namelist():
        zf.extract(i, path=ruta_excels)
        
    #Recorre los ficheros
    print('Recorriendo los ficheros')
    lista_ficheros = listdir(ruta_excels)
    df_res = pd.DataFrame([])
    for fichero in lista_ficheros:
        print('Obteniendo los datos del fichero ' + fichero)
        year = get_year(fichero)
        df_aux = read_population(ruta_excels+fichero, year)
        df_aux['anno'] = year
        df_res = df_res.append(df_aux)

    print('Los datos del fichero se han unido en un solo dataframe')
    ##### He intentado hacer el for con comprehesion pero no lo he conseguido.
    #lista_data = [read_population(ruta_excels+fichero, get_year(fichero)) for fichero in lista_ficheros]

    print('Creando CSV')
    #Indicamos los nombres que tendran las columnas del csv
    header = ["cod_provincia", "cod_municipio", "poblacion", "anno"]
    #Indicamos que el separador de los campos sera ";"
    df_res.to_csv('05_lectura_excel/pobmun.csv', columns = header, sep = ';')
    
    print('Eliminando pobmun.zip y el directorio con los ficheros descomprimidos')
    shutil.rmtree('05_lectura_excel/pobmun')
    os.remove('05_lectura_excel/pobmun.zip')
    
    print('Eliminados correctamente')

download_population()

