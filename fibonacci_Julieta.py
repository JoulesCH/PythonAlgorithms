"""

f(x):= 

	0              ssi              x = 0

	1              ssi              x = 1

	f(x-1)+ x(x-2)                  x > 1

"""



def fib(n,dic={}):

	if n == 0:
		return 0

	elif n == 1:
		return 1	

	else:
		try: 
			return dic[n]

		except KeyError:
	
			numero = fib(n-1) + fib(n-2)
			dic[n] = numero
			
			return numero


numero = fib(500)		

print(numero)


