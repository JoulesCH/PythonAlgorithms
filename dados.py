import random
def tirar_dado(tiros):
	secuencia_de_tiros = []
	for _ in range(tiros):
		tiro = random.choice([2,3,4,5,6,7,3,4,5,6,7,8,4,5,6,7,8,9,5,6,7,8,9,10,6,7,8,9,10,11,7,8,9,10,11,12])
		secuencia_de_tiros.append(tiro)
	return secuencia_de_tiros

def main(numero_de_tiros,numero_de_intentos):
	tiros = []

	for _ in range(numero_de_intentos):
		secuencia_de_tiros = tirar_dado(numero_de_tiros)
		tiros.append(secuencia_de_tiros)

	tiros_con_1 = 0
	for tiro in tiros:
		if 12 in tiro: #if 1 not in tiro para calcular la negacion de 1
			tiros_con_1 += 1

	probabilidad_de_tiros_con_1 = tiros_con_1 / numero_de_intentos

	print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_de_tiros_con_1}')		

if __name__ == '__main__':

	numero_de_tiros=10
	numero_de_intentos=10000

	main(numero_de_tiros,numero_de_intentos)

