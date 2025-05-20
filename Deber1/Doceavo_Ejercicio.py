#Una panadería vende barras de pan a 3.49€ cada una.  El pan que no es el día tiene 
# un descuento del 60%.  Escribir un programa que comience leyendo el número de barras  vendidas
#  que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

barras_de_pan=3.49
descuento=0.60
barras_vendidas=(int(input("Ingrese el numero de bandas vendidas que no son del día")))
(print("El precio es: ",barras_de_pan ))
print("El descuento por no ser fresca es del: ", descuento*100 , "%")
precio_descuento = barras_de_pan * (1 - descuento)
precio_total = barras_vendidas * precio_descuento
print("El coste final total es: €", round(precio_total, 2))


