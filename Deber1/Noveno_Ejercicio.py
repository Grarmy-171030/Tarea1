#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital
#  obtenido en la inversión.
cantidad_invertir=float(input("Ingrese la cantidad que va a invertir: "))
interes_anual=float(input("Ingrese la cantidad anual: "))
numero_de_años=float(input("Ingrese el numero de años: "))
capital_obtenido=cantidad_invertir*(1+interes_anual/100)
print("Su capital es:  " , capital_obtenido )