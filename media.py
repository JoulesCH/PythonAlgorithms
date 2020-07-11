import random

def media(X): # X es la forma matemática en que se representa un array

	return sum(X)/len(X)

def varianza(X):
	mu = media(X)

	sumatoria = 0

	for x in X: #Notación matemática
		sumatoria += (x-mu)**2

	return sumatoria / len(X)
	
def desviacion_estandar(X):
	return varianza(X)**0.5		

if __name__ == '__main__':

	X = [random.randint(1,21) for i in range(20)]
	Mu = media(X)
	Var = varianza(X)
	Sigma = desviacion_estandar(X)

	print(f'Arreglo = {X}')
	print(f'Media = {Mu}')
	print(f'Varianza = {Var} ')
	print(f'Desviacion estandar = {Sigma}')


	