#For simple
'''for x in range(101):
    print(x)'''
#En la funcion Ranga, el primer parametro es donde inicia y 2do. donde finaliza menos uno.
'''for x in range(1,100):
    print(x)'''

#En la funcion Ranga, el primer parametro es donde inicia, 2do. donde finaliza menos uno y 3ro los saltos que dara.
'''for x in range(1,100,3):
    print(x)'''

'''suma=0
for f in range(10):
    valor=int(input("Ingrese valor:"))
    suma=suma+valor
print("La suma es")
print(suma)
promedio=suma/10
print("El promedio es:")
print(promedio)'''

'''
aprobados = 0;
reprobados = 0;
for f in range(3):
    nota=int(input("Ingrese la nota:"));
    if nota >= 7:
        aprobados=aprobados+1
    else:
        reprobados=reprobados+1;
print("Cantidad de aprobados");
print(aprobados);
print("Cantidad de reprobados");
print(reprobados); '''

'''
mul3 = 0;
mul5 = 0;
for f in range(10):
    valor = int(input("Ingrese un valor: "));
    if valor % 3 == 0:
        mul3 = mul3 + 1
    if valor % 5 == 0:
        mul5 = mul5 + 1;
print("Cantidad de valores ingresados múltiplos de 3");
print(mul3);
print("Cantidad de valores ingresados múltiplos de 5");
print(mul5);
'''
'''
cantidad=0
n=int(input("Cuantos valores ingresará:"))
for f in range(n):
    valor=int(input("Ingrese el valor:"))
    if valor>=1000:
        cantidad=cantidad+1
print("La cantidad de valores ingresados mayores o iguales a 1000 son")
print(cantidad) '''