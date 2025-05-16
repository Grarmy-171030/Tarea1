#Escribir un programa que pida al usuario su peso (en kg) y  estatura (en metros), 
# calcule el índice de masa corporal y  lo almacene en una variable, y muestre por pantalla la frase
#  Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
peso_en_kilogramos=float(input("Ingrese su peso en kilogramos: "))
estatura_metros=float(input("Ingrese su estatura en metros: "))
indice_de_masa_corporal = peso_en_kilogramos / (estatura_metros ** 2)
print("Su indice de masa corporal es de : ", round(indice_de_masa_corporal,2))
