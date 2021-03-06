from camino_borrachos import BorrachoTradicional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import figure,show

def caminata(campo,borracho,pasos):
	inicio = campo.obtener_coordenada(borracho)

	for _ in range(pasos):
		campo.mover_borracho(borracho)

	return inicio.distancia(campo.obtener_coordenada(borracho))	


def simular_caminata(pasos,numero_de_intentos,tipo_de_borracho):
	borracho = tipo_de_borracho(nombre='David') # funcion agnostica al tipo del borracho
	origen = Coordenada ( 0, 0 )
	distancias = []

	for _ in range(numero_de_intentos): # _ significa que no vamos a utilizar la variable
		campo = Campo()
		campo.anadir_borracho(borracho, origen)
		simulacion_caminata = caminata(campo, borracho, pasos)
		distancias.append(round(simulacion_caminata, 1))

	return distancias	

def graficar(x,y):
	grafica = figure(title = 'Camino aleatorio',x_axis_label = 'Pasos',y_axis_label = 'Distancia recorrida')
	grafica.line(x,y,legend = 'Distancia media')
	show(grafica)


def main(distancia_de_caminata,numero_de_intentos,tipo_de_borracho):
	distancias_media_por_caminata = []
	for pasos in distancia_de_caminata:
		distancias = simular_caminata(pasos,numero_de_intentos, tipo_de_borracho)
		distancia_media = round(sum(distancias)/len(distancias),4)
		distancia_maxima = max(distancias)
		distancia_minima = min(distancias)
		distancias_media_por_caminata.append(distancia_media)
		print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} ')
		print(f'La distancia media = {distancia_media}')
		print(f'Max = {distancia_maxima}')
		print(f'Min = {distancia_minima}')
	graficar(distancia_de_caminata,distancias_media_por_caminata)	

if __name__ == '__main__':
	distancia_de_caminata = [10,100,1000,10000]

	numero_de_intentos = 100
	main(distancia_de_caminata,numero_de_intentos,BorrachoTradicional)