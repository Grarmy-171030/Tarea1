#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero
#  depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe 
# calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
#  Redondear cada cantidad a dos decimales.
cantidad_de_dinero=float(input("Ingresa la cantidad de dinero: \n"))
interes=0.04
primer_año = round(cantidad_de_dinero * (1 + interes), 2)
segundo_año = round(primer_año * (1 + interes), 2)
tercer_año = round(segundo_año * (1 + interes), 2)
print("Ahorros del primer año: ", primer_año)
print("Ahorros del segundo año: ", segundo_año)
print("Ahorro del tercer año: ",tercer_año)