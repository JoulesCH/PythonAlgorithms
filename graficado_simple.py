#--------------------------------------------------------

#@: Julio César. Archivo que hace graficado simple. 

#--------------------------------------------------------

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__': # Punto de entrada o entry point

	output_file('GraficadoSimple.html') # Nombre y exentsion del archivo output

	figura_de_bokeh = figure()

	valores_a_graficar = int(input('Cuantos valores quieres graficar? '))

	valores_x = list(range(valores_a_graficar))

	valores_y = []

	for x in valores_x:
		valor = int(input(f'Valor y para {x} '))

		valores_y.append(valor)

	figura_de_bokeh.line(valores_x,valores_y,line_width=2)	
	show(figura_de_bokeh)
