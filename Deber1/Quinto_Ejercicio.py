#Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
# el coste por hora. Después debe mostrar 
# por pantalla la paga que le corresponde.
horas_trabajadas=float(input("Ingrese el numero de horas trabajadas : \n "))
costo_por_hora=float(input("Ingrese el costo por hora : \n "))
paga_total=horas_trabajadas*costo_por_hora
print("La paga total es : ",paga_total)
