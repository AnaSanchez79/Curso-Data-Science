import pandas as pd
import requests
import calendar
from bs4 import BeautifulSoup

def datosMeteo(año, mes):
    #Obtenengo el último día del mes
    ult_dia_mes = calendar.monthrange(año,mes)
    # Descarga del html sustituyendo en la url los parámetros año, mes y último día del mes 
    res = requests.get('http://www.ogimet.com/cgi-bin/gsynres?ord=REV&decoded=yes&ndays='+str(ult_dia_mes[1])+'&ano='+str(año)+'&mes='+str(mes)+'&day='+str(ult_dia_mes[1])+'&hora=24&ind=08221')
    # Parseo
    soup = BeautifulSoup(res.content, 'lxml')
    # Busco la tercera tabla
    table = soup.find_all('table')[2]
    # Paso la tabla a pandas. Ademas, me quedo solo con las primeras columnas,
    #  que es donde va a estar la informacion interesante
    df_tabla = pd.read_html(str(table))[0].iloc[:,0:8]
    # Elimino la primera línea que es donde se encuentran las cabeceras, ya que están desplazadas
    df_tabla.drop(df_tabla.index[:1], inplace=True) 

    #Guardo en un diccionario las columnas que necesito del dataframe
    dicci = {}
    dicci['Fecha'] = df_tabla.iloc[:,0]
    dicci['Hora']  = df_tabla.iloc[:,1]
    dicci['T(C)']  = df_tabla.iloc[:,2]
    dicci['ddd']   = df_tabla.iloc[:,6]
    dicci['ffkmh'] = df_tabla.iloc[:,7]
    
    #Devuelvo un dataframe con los datos del diccionario
    return pd.DataFrame(dicci)

#Genero una lista de 1 a 12 para recorrer los 12 meses
meses = list(range(1,13))
#Utilizo for comprehension para llamar a la función datosMeteo por cada mes y guardo los dataframes en una lista 
list_resultado = [datosMeteo(2008,mes) for mes in meses]
#Concateno los dataframes de la lista en uno solo df_resultado
df_resultado = pd.concat(list_resultado)
#Elimino los duplicados
df_resultado.drop_duplicates()
#Imprimo el dataframe
print(df_resultado)


