# 5 10000 20000 30000 20000 20000
suma =0
#esto es un ciclo
for i in range(int(input("¿Cuántas boletas ingresará al sistema?: "))):
    valor=int(input(f"Ingrese valor boleta {i+1}:"))
    suma+=valor 
#terminó el ciclo
print(f"La suma total de la boleta es {suma}")
print(f"El iva ingresado es {0.19 *suma}")
print(f"El monto ingresado al negocio es {0.81*suma}")