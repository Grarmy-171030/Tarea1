#Escribir un programa que lea un entero positivo, , introducido por el usuario 
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
# . La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
numero_entero_positivo=int(input("Ingrese un numero: "))
suma_de_enteros=numero_entero_positivo*(numero_entero_positivo+1)/2
print("La suma de todos los enteros es : ",round(suma_de_enteros) )
