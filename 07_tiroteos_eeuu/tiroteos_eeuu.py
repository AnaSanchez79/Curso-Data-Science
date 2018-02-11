import pandas as pd
from geopy.geocoders import GoogleV3

#Leemos el csv
df = pd.read_csv('07_tiroteos_eeuu/dat/us_mass_shootings.csv', encoding = "ISO-8859-1", sep = ',')

#Convertimos correctamente los tipos de datos: las fechas y los números
df['Date'] = pd.to_datetime(df['Date']).apply(lambda x:x.strftime('%d/%m/%Y'))
pd.to_numeric(df['S#'] , errors='coerce')
pd.to_numeric(df['Fatalities'] , errors='coerce')
pd.to_numeric(df['Injured'] , errors='coerce')
pd.to_numeric(df['Total victims'] , errors='coerce')
pd.to_numeric(df['Latitude'] , errors='coerce')
pd.to_numeric(df['Longitude'] , errors='coerce')

#Convertimos la columna Mental.Health.Issues a un valor booleano. 
#Los valores Unclear, Unknown, unknown y otros deben pasarse a NA.
df['Mental Health Issues'] = df['Mental Health Issues'].replace(['Unclear', 'Unknown', 'unknown'], np.nan)
df['Mental Health Issues'] = df['Mental Health Issues'].replace(['Yes'], True)
df['Mental Health Issues'] = df['Mental Health Issues'].replace(['No'], False)


#Estandarizamos las columnas de clases al mínimo de valores posibles y las convertimos a categorical. 
#Race: los valores que queremos tener son: white, black, asian, other. Algunos ejemplos de la transformación:
    #Black American or African American debe ser black
    #Some other race, las mezclas de razas y cosas minoritarias que no aplican en los otros grupos (como Latino o Native American or Alaska Native) deben ser other
    #Unknown debe ser NA
    
df['Race'] = df['Race'].replace(['Black', 'Black American or African American', 'Black American or African American/Unknown'], 'black')
df['Race'] = df['Race'].replace(['White', 'White American or European American/Some other Race', 'White American or European American'], 'white')
df['Race'] = df['Race'].replace(['Asian', 'Asian American', 'Asian American/Some other race'], 'asian')
df['Race'] = df['Race'].replace(['Unknown', 'Other', 'Some other race', 'Two or more races', 'Native American or Alaska Native', 'Latino', np.nan], 'other')

df['Race'] = df['Race'].astype('category')

#Gender: los valores que queremos tener son: male, female, male/female. Los unknown deben ser NA.

df['Gender'] = df['Gender'].replace(['M', 'Male'], 'male')
df['Gender'] = df['Gender'].replace(['M/F', 'Male/Female'], 'male/female')
df['Gender'] = df['Gender'].replace(['Unknown'], np.nan)
df['Gender'] = df['Gender'].replace(['Female'], 'female')

df['Gender'] = df['Gender'].astype('category')

#Separamos la columna Location en City y State. 

#Hay una fila que solamente tiene el valor Washington D.C. en su columna de localización. Lo convertimos a Washington, Washington antes de hacer la separación.
df['Location'] = df['Location'].astype('str')
df['Location'] = df['Location'].replace(['Washington D.C.'], 'Washington, Washington')

#Están ambos valores separados por coma. Pero no es tan simple como coger como City lo de la derecha y como State lo de la izquierda
#de la coma. Hay valores que tiene varias comas. 

#Creamos una funcion para obtener la parte "City" de la columna "Location".
#la función recibe la lista resultado de hacer split (por coma) de location

def city(loc):
    """
    Si loc tiene longitud 2 el campo city será el primer valor de la lista
    Si no, city será todos los elementos de la lista concatenados menos el último elemento
    """
    if len(loc) == 2:
        return loc[0]
    else:
        locations = loc[0:len(loc)-1]
        return ', '.join(locations)

#Dividimos la columna "Location" por coma
s = df['Location'].apply(lambda x: x.split(','))
#Obtenemos la parte correspondiente a la columna City
df['City'] = s.apply(lambda x: city(x) )
#Obtenemos la parte correspondiente a la columna State
df['State'] = s.apply(lambda x: x[-1])


#A veces las columnas de Fatalities y Injured no suman Total.victims. Actualizamos esta última para que sea la suma de las otras dos.
df['Total victims'] = df['Fatalities'] + df['Injured']


#Elimina los duplicados para un mismo estado y fecha.
df.drop_duplicates(['State', 'Date'])

df.head()



