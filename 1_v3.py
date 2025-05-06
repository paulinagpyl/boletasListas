# 5 10000 20000 30000 20000 20000
boletas=int(input("¿Cuántas boletas ingresará al sistema?: "))
suma =0
valores = []
for i in range(boletas):
    valor=int(input("Ingrese valor boleta:"))
    valores.append(valor)
print(f"La suma total de la boleta es {sum(valores)}")
iva=0.19 *sum(valores) 
print(f"El iva ingresado es {iva}")
monto=0.81*sum(valores)
print(f"El monto ingresado al negocio es {monto}")
