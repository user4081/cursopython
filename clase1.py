
# Ejercicio2

#I)  ingresar 2 numeros ENTEROS a y b a traves del teclado
#II) imprima su suma, diferencia y y cociente

"""
print("Por favor ingrese 2 numeros enteros a y b.")
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

if (a%1==0 and b%1==0):
    print("a + b = ", int(a+b))
    print("a - b = ", int(a-b))
    print("a / b = ", a/b)
else:
    print("ERROR! Por favor ingrese numeros ENTEROS.") 
"""


# Ejercicio3

#I)  Ingresar el radio de un circulo/esfera
#II) calcular superficies y perimetros

"""
import math as m
r=int(input("Ingresar el radio: "))
print("El area del circulo es: ", m.pi * r**2)
print("El perimetro del circulo es: ", m.pi * 2 * r)
print("La superficie de la esfera es: ", 4 * m.pi * r**2)
print("El volumne de la esfera es: ", 4/3 * m.pi * r**3) 
"""


# Ejercicio4

#I)  Ingresar una edad en anios
#II) Devolver la edad en dias

"""
edad=int(input("Ingrese su edad en anios: "))
print("Su edad en dias = ", edad*365) 
"""



# Ejercicio5

# I) Ingresar 3 numeros enteros. Calcular su promedio y mostrarlo en panpalla.

"""
print("Ingrese por favor 2 numeros enteros para calcular su promedio")
a=float(input("Ingrese a: "))
if (a%1==0):

    b=float(input("Ingrese b: "))
    
    if (b%1==0):
        print("Su promedio es =", (a+b)/2)
    else:
        print("Error! b NO es un numero entero.")
else:
    print("Error! a NO es un numero entero")
"""




# Ejercicio6

# Una inmobiliaria paga a sus vendedores un salario de $800,
# mas una comision de $50 por cada venta realizada, mas el %5 de valor de esas ventas.
# I) Realizar un programa que imprima el numero de vendedor y el salario que le corresponde en un determinado mes.
# II) Se leen el numero de vendedor, la cantidad de ventas que realizo y el valor total de las mismas

"""
salario=800
comision=50

print("Vamos a simular la cantidad de registros")
cantidad=int(input("Cuantos vendedores quiere tener?"))

registro={}


for i in range(cantidad):
    numero=int(input("\nIngrese numero de vendedor: "))
    ventas=int(input("Ingrese la cantidad de ventas: "))
    valor=int(input("Ingrese el valor total de las mismas: "))

    registro[numero]=[ventas, valor]

print("\n registro total:")
print(registro)

print("\nSalarios de este mes: ")

for i in registro:
    print("vendedor #:",i ,"  salario:",salario + registro[i][0]*comision + registro[i][1]/100*5)
"""        



# Ejercicio7

# Un banco necesita para sus cajeros automaticos un programa que lea la cantidad de dinero e imprima a cuantos billetes equivale.
# Considerando que existen billetes de 100, 50, 10, 5, y 1.
# Desarollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
"""
dinero=int(input("\nPor favor ingrese la cantidad de dinero a retirar: "))

if (dinero>=100):
    x=int(dinero/100)
    dinero=dinero-x*100
    print(x, "billete(s) de 100")
if (dinero>=50):
    x=int(dinero/50)
    dinero=dinero-x*50
    print(x, "billete(s) de 50")
if (dinero>=10):
    x=int(dinero/10)
    dinero=dinero-x*10
    print(x, "billete(s) de 10")
if (dinero>=5):
    x=int(dinero/5)
    dinero=dinero-x*5
    print(x, "billete(s) de 5")
if (dinero>=1):
    x=int(dinero/1)
    dinero=dinero-x
    print(x, "billete(s) de 1")
"""


# Ejercicio8

# Ingresar 2 numeros A y B e imprimir el mayo o cualquiera si son iguales
"""
a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))

print(max(a,b))
"""

# Ejercicio9

# Lee un numero entero A e imprime mensaje indicando si es par o impar
"""
a=int(input("Ingrese un numero entero para saber si es par o impar: "))

if (a%2==0):
    print("El numero es par")
else:
    print("El numero es impar")
"""




# Ejercicio10

# Lee un numero entero N y determinar si es un numero natural(positivo y distinto de cero).
# Si lo es, imprimirlo junto con su doble.
# En caso contrario, imprimirlo junto con su triple.
"""
n=int(input("Ingrese un numero NATURAL: "))

if (n>0 and n%1==0):
    print("El numero",n," pertenece a los naturales y su doble es ", n*2)
else:
    print("El numero",n," NO pertenece a los naturales y su triple es ", n*3)
"""




# Ejercicio11

# Ingresar dos numeros enteros A y B.
# Desarrollar un programa que determine si A es multiplo de B y si B es multiplo de A.
# Imprimir mensajes aclaratorios
"""
a=int(input("Ingrese un entero a: "))
b=int(input("Ingrese un entero b: "))

if (a%b==0):
    print("b es multiplo de a, pues", b,"multiplicado por", int(a/b),"=", int(a))
elif (b%a==0):
    print("a es multiplo de b, pues", a,"multiplicado por", int(b/a),"=", int(b))
else:
    print("Los numeros no son multiplos")
"""




# Ejercicio12

# Desarrollar un programa para leer la base y la altura de un triángulo e imprimir su superficie. 
# El algoritmo debe validar los datos de entrada, verificando que éstos sean números positivos. 
# En caso contrario debe imprimirse el dato erróneo junto con una leyenda aclaratoria. 
# Se recuerda que Sup = (Base * Altura) / 2
"""
base=int(input("Ingrese la base del triangulo: "))
if(base>=0):
	altura=int(input("Ingrese la altura del triangulo: "))

	if(altura>=0):
		print("la superficie del triangulo =", (base*altura)/2)
	else:
		print("ERROR! El numero no puede ser negativo.")

else:
	print("ERROR! El numero no puede ser negativo.")
"""





# Ejercicio13

# Una empresa aplica el siguiente procedimiento en la comercialización de sus productos: 
# · Aplica el precio base a la primera docena de unidades. 
# · Aplica un 10% de descuento a todas las unidades entre 13 y 100. 
# · Aplica un 25% de descuento a todas las unidades por encima de las 100. 
# Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
# El cálculo resultante sería: 100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04 

catalogo={'producto': ['Cuadernos','Lapiceras','Cartucheras'],'precio': [100, 20, 50] }



for i in range(3):
	print(i+1,")",catalogo['producto'][i],"$", catalogo['precio'][i])


producto=int(input("\nElija el producto: "))-1
cantidad=int(input("Elija la cantidad de unidades a comprar: "))


if (producto==0):
	precio=(catalogo['precio'][producto])
elif(producto==1):
	precio=(catalogo['precio'][producto])
elif(producto==2):
	precio=(catalogo['precio'][producto])


if (cantidad<=12):
	print("El precio final a pagar por",cantidad,catalogo['producto'][producto],": ",precio*cantidad)
elif(cantidad>12 and cantidad<=100):
	descuento10 = (precio*12)+(precio/100*90)*(cantidad-12)
	print("El precio final a pagar por",cantidad,catalogo['producto'][producto],": ",descuento10)
elif(cantidad>100):
	descuento25 = (precio*12)+(precio/100*90)*88+(precio/100*75)*(cantidad-100)
	print("El precio final a pagar por",cantidad,catalogo['producto'][producto],": ",descuento25)






