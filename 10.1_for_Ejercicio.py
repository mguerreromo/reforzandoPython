n = int(input("Cuantos triangulos procesar: "))
cantidad = 0;

for f in range(n):
    base = int(input("Ingrese el valor de la base: "))
    altura = int(input("Ingrese el valor de la altura: "))
    superficie = base * altura / 2;
    print (f'Superfice:  {superficie}');
    if superficie > 12:
        cantidad = cantidad + 1
print(f'Cantidad de triangulos con mayor a 12: {cantidad}');
