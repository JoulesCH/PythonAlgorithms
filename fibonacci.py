#---------------------------

#@: Julio César. Algoritmo de programación dinámica en Fibonacci

#---------------------------
import sys

def fibonacci_recursivo(n):
	"""

	Recibe un numero entero, y devuelve el numero
	fibonacci en esa posicion de manera recursiva.

	"""
	if n == 0 or n == 1:
		return 1

	return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)	


def fibonacci_dinamico(n,memoization={}):
	"""

	Recibe un numero entero, y devuelve el numero
	fibonacci en esa posicion utilizando memoization (caché)
	con el diccionario memoization.

	"""
	if n == 0 or n == 1:
		return 1

	try:
		return memoization[n]

	except KeyError: #KeyError es cuando no se encuentra la llave en el diccionario
		resultado = fibonacci_dinamico(n-1) + fibonacci_dinamico(n-2)
		memoization[n] = resultado
		return resultado

		
if __name__ == '__main__':
	sys.setrecursionlimit(1002)
	print(fibonacci_dinamico(1000))
	

