"""
for i in range(1,10,2): #arranca en 1 hasta 10 saltos de a 2
    print(i)
"""


"""
lista = [1,2,4,5,8]
for i in lista:
    print(i)
    #2
    #4
    #5
    #8
"""



"""

listaNombres = [] #appende para agregar / pop para borrar
listaEdades = []
listaTiempoempresa = []


for i in range(5):

    nombre = input("Ingrese el nombre del empleado ")
    edad = input("Ingrese edad del empleado ")
    tiempo_empresa = int(input("Cuanto tiempo lleva en la empresa?"))

    listaNombres.append(nombre)
    listaEdades.append(edad)
    listaTiempoempresa.append(tiempo_empresa)

print("termina el ciclo")



""

# Multiparadigma (lineal, funcional, multiparadigma)
# Funciones
"""

"""
def potenciar_numeros():
    print("esta funcion potencia 2 num internos")
    a = 9
    b = 2
    print(a**b)


potenciar_numeros()

"""

"""
def potenciar_numeros_usuario(a,b):
    print(a**b)


a=int(input("Ingresa a: "))
b=int(input("Ingresa b: "))

potenciar_numeros_usuario(a,b)
"""





# codear 2 funciones. La primera cargarNumeros() le pide al usuario que inrese 5 datos por consola y estos datos deben insertarse a una lista
# la segunda recorrerLista debe recorrer la lista y debe devolver la suma de todos los elementos de la lista
# una tercer fiuncion comprobarNumero debe recibir como parametro este valor y debe determinar si es par o impar

"""

lista = []
suma = 0

def cargarNumeros():
    for i in range(3):
        num = int(input("Ingresa numero: "))
        lista.append(num)
    print("Lista cargada ok!")
    # podria ser return lista


# listaResultante = cargarNumeros()
# print(listaResultante)

 

def recorrerLista(l):
    return sum(l)



def parOimpar():
    if(suma%2 == 0):
        print("es par")
    else:
        print("es impar")



cargarNumeros()
suma = recorrerLista(lista)
print("La suma de todos los numeros de la lista = ", suma)
parOimpar()
"""


# Ejercicio7

# import tandom
# r = random.randint(1,3)






"""
dic = {"max": 36, "nico": 24}
print(dic["max"])
"""
"""
dic = {}

def cargarDiccionario (n):
    for i in range(n):
        
        dni = int(input("Ingresa dni "))
        nombre = input("Ingresa tu nombre")
        edad = int(input("Edad? "))

        dic[dni] = [nombre, edad]
        # "31123...": ["Max", 36]



elementos = int(input("Cuantos empleados agregamos?"))
cargarDiccionario(elementos)

#print(dic)
"""



"""
print(dic[1][0])
"""

"""
for i in dic:
    print(dic[i])
    print(i) # imprimiria solo el primer campo o sea dni en este caso
"""


"""

import random 

dic = {}
letras = ["a","b","c","d","e","f","g","e","h","i"]

def cargarDiccionario (n):
    for i in range(n):
                
        nombre = letras[random.randint(0,len(letras)-1)]+letras[random.randint(0,len(letras)-1)]+letras[random.randint(0,len(letras)-1)]   
        
        dic[random.randint(20000000,30000000)] = [random.randint(21,50),nombre, random.randint(5000,50000)]
        

elementos = int(input("Cuantos empleados agregamos?"))
cargarDiccionario(elementos)


print(dic)
"""











# Ejercicio0

# Desarrollar un programa que imprima los números impares comprendidos entre 1 y 1000.
"""
def imprimeImpares():
	for i in range(1000):
		if(i%2!=0):
			print(i)

imprimeImpares()
"""









# Ejercicio1

# Leer diez números enteros e imprimir el mayor.
"""
def mayorDe(x):
	print("El mayor de los numeros es:",max(x))

numeros=[]

for i in range(10):
	
	mas = int(input("Ingrese numero: "))
	numeros.append(mas)

mayorDe(numeros)
"""






# Ejercicio2

# Leer dos números A y B enteros positivos. 
# Calcular el producto A * B por sumas sucesivas e imprimir el resultado. 
# Ejemplo: 4 * 3 = 4 + 4 + 4 (4 sumado 3 veces). 
"""
def sumaSucesiva(x,y):
	print(x, end =" ")
	for i in range(y-1):
		print("+",x, end =" ")
	print("=",x*y)

a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))

print("\na * b = ", a*b, "\n")

sumaSucesiva(a,b)
"""





# Ejercicio3

# Leer diez números e imprimir el menor de ellos, indicando además el número de orden con que fue leído. 
"""
def menorDe(x):
	print("El menor de los numeros es:", min(x))

numeros=[]
orden=0

for i in range(10):
	
	n = int(input("Ingrese numero: "))
	numeros.append(n)


for j in range(len(numeros)):
    if (numeros[j]==min(numeros)):
        orden=j+1


menorDe(numeros)
print("Y el numero de orden es: ",orden)
"""







# Ejercicio4

#  Escribir un programa que imprima los múltiplos de 7 hasta el 3000.
"""
for i in range(3000):
    if (i>0 and i%7==0):
        print(i)
"""









# Ejercicio5

# Leer diez números e imprimir el mayor, el menor y el rango del conjunto 
# (El rango de un conjunto se calcula restando el mayor menos el menor). 

"""
def menorDe(x):
    print("El menor de los numeros es:", min(x))

def mayorDe(x):
    print("El mayor de los numeros es:",max(x))

def rango(x):
    print("El rango del conjunto es:",max(x)-min(x))


numeros=[]

for i in range(10):
    
    n = int(input("Ingrese numero: "))
    numeros.append(n)

mayorDe(numeros)
menorDe(numeros)
rango(numeros)
"""













# Ejercicio6 

# El factorial de un número entero N mayor que cero se define como el producto 
# de todos los enteros X tales que 0 < X <= N. 
# Desarrollar un programa para calcular el factorial de un número dado. 
# Deberán rechazarse las entradas inválidas (menores que 0). 

"""
N = int(input("Ingrese un entero N>0 para calcular N!: "))

if (N>0):
    for i in range(N-1,1,-1):
        N = N*i

    print("El factorial =",N)
else:
    print("Entrada INVALIDA!")

"""








# Ejercicio7

# Una empresa cuenta con 100 empleados, divididos en tres categorías A, B y C. 
# Por cada empleado se lee su legajo, categoría y salario. 
# Se solicita elaborar un informe que contenga: 
# • Importe total de salarios pagados por la empresa. 
# • Cantidad de empleados que ganan más de $20000. 
# • Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”. 
# • Legajo del empleado que más gana. 
# • Sueldo más bajo. 
# • Importe total de sueldos por cada categoría. 
# • Salario promedio. 


import random 

dic = {}
letras = ["a","b","c","d","e","f","g","e","h","i","j","k","o","u"]
categoria = ["A","B","C"]

def cargarDiccionario ():

    for i in range(100):
                
        nombre = letras[random.randint(0,len(letras)-1)]+letras[random.randint(0,len(letras)-1)]+letras[random.randint(0,len(letras)-1)]+letras[random.randint(0,len(letras)-1)] 
        
        dic[nombre] = [random.randint(1000,3000),random.randint(21,50), random.randint(40000,100000), categoria[random.randint(0,len(categoria)-1)]]
"""        
def reporteSalarios ():
    salarios = 0
    for i in range(len(dic)):
        salarios = salarios + dic[i][2]

    return(salarios)
"""

cargarDiccionario()
print(dic)








# Ejercicio 8 
# Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar.
# Imprimir el valor mínimo y el lugar que ocupa. 
# Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe. 
# La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista. 




