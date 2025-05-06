# 5 10000 20000 30000 20000 20000
suma =0
valores = []
#inicio de ciclo
for i in range(int(input("¿Cuántas boletas ingresará al sistema?: "))):
    valores.append(int(input(f"Ingrese valor boleta {i+1}:")))
#fin ciclo
print(f"La suma total de la boleta es {sum(valores)}")
print(f"El iva ingresado es {0.19 *sum(valores)}")
print(f"El monto ingresado al negocio es {0.81*sum(valores)}")
