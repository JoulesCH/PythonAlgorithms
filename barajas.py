#simulacion de una baraja 
import random

PALOS = ['espada','corazón','rombo','trebol'] #mayúsculas significan constantes
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey',]

def crear_baraja():
	barajas = []

	for palo in PALOS:
		for valor in VALORES:
			barajas.append((palo,valor))

	return barajas	

def obtener_mano(barajas,tamano_mano):
	mano = random.sample(barajas,tamano_mano) #dentro de una coleccion obtiene una muestra sin repetirse.	
	return mano

def main(tamano_mano,intentos):
	barajas = crear_baraja()

	manos = []

	for _ in range(intentos):
		mano = obtener_mano(barajas,tamano_mano)
		manos.append(mano)

	return manos	

if __name__ == '__main__':

	tamano_mano = 5
	intentos = 2
	print(main(tamano_mano,intentos))





