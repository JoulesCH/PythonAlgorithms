import random
import math
from media import desviacion_estandar,media

def estimacion(numero_de_agujas,numero_de_intentos):
	estimados = []
	for _ in range(numero_de_intentos): 
		estimacion_pi = aventar_agujas(numero_de_agujas)
		estimados.append(estimacion_pi)
	return estimados
	
def calculos(lista):
	return media(lista),desviacion_estandar(lista)	 	

def aventar_agujas (numero_de_agujas):
	adentro_del_circulo = 0 

	for _ in range(numero_de_agujas):
		x = random.random() * random.choice([1,-1]) #nos regresa un valor entre 0 y 1
		y = random.random() * random.choice([1,-1])

		distancia_desde_el_centro = math.sqrt(x**2 + y**2)

		if distancia_desde_el_centro <= 1:
			adentro_del_circulo += 1

	return (4 * adentro_del_circulo)/numero_de_agujas
	

if __name__ == '__main__':
	print(calculos(estimacion(100,1000)))

