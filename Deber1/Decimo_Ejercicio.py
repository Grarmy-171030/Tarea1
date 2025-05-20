#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso 
# de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en 
# cada paquete a demanda. Cada payaso pesa 112 gy cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcular el peso total del paquete que será enviado.
peso_de_payaso = 112  # gramos
peso_de_muniecas = 75   # gramos
numero_de_payaso = int(input("Ingrese el número de payasos: "))
numero_de_muniecas = int(input("Ingrese el número de muñecas: "))
peso_total = (numero_de_payaso * peso_de_payaso) + (numero_de_muniecas * peso_de_muniecas)
print("El peso total del paquete es:", peso_total, "gramos")
