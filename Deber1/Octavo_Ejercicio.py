#Escribir un programa que pida al usuario dos números enteros y 
# muestre por pantalla la entre da un cociente y un resto donde y
#  son los números introducidos por el usuario, y y son el cociente y 
# el resto de la división entera respectivamente.
numero1=int(input("Ingrese el primer numero:  "))
numero2=int(input("Ingrese el segundo numero:  "))
cociente = numero1 // numero2
resto = numero1 % numero2
print("La división entre", numero1, "y", numero2, "da un cociente de", cociente, "y un resto de", resto)

