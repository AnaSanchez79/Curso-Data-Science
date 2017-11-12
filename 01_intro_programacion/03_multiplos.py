#Variable "Suma" para guardar la suma de todos los múltiplos de 3 o de 5 menores que 1000
suma = 0

for m in range(1000) :  # de 0 a 999
#Uso la estructura if - elif para sumar m una sola vez en caso de ser múltiplo de 3 y de 5
	if m % 3 == 0 :
		suma = suma + m
	elif m % 5 == 0 :
		suma = suma + m

print(suma)