# 5 10000 20000 30000 20000 20000
boletas=int(input("¿Cuántas boletas ingresará al sistema?: "))
suma =0
# inicio ciclo
for i in range(boletas):
    valor=int(input("Ingrese valor boleta:"))
    suma+=valor # lo mismo que suma = suma + valor
#fin ciclo

print(f"La suma total de la boleta es {suma}")
iva=0.19 *suma #iva = (19/100)*suma
print(f"El iva ingresado es {iva}")
monto=0.81*suma
print(f"El monto ingresado al negocio es {monto}")