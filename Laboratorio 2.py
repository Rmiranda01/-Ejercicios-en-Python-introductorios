#****************************************************************
#-----------------------CAPITULO 6-------------------------------
#****************************************************************
#---------------Operadores de comparación------------------------
# print("150 == 150 -->", 150==150)
# print("50 != 100 -->", 50!=100)
# print("15 < 100 -->", 15<100)
# print("150 > 50 -->", 150>50)
# print("14 <= 28 -->", 14<=28)
# print("40 >= 100 -->", 40>=100)
#***********************************************************
#---------------Operadores Logicos-------------------------
# print("(5 < 35) and (60 > 15)---> ", (5 < 35) and (60 > 15))
# print("(3 < 18) or (23 > 45)---> ",(3 < 18) or (23 > 45))
# print("not 60 < 30 ---> ", not 60 < 30)
#***********************************************************
#---------------Trabajar con una declaración if-------------------------
# numero1 = int(input('Ingrese el primer numero a evaluar: '))
# if numero1 < 0:
#  print(numero1, 'es negativo')
# print("")
# numero2 = int(input("Ingrese el segundo numero a evaluar: "))
# if numero2 > 0:
#  print(numero2, " es positivo.")
#  print(numero2, " El cuadrado es de: ", numero2*numero2)
# print("Adiós Mundo")
#***********************************************************************
#---------------Else en una declaración if---------------------
# numero = int(input("Ingrese ahora otro número: "))
# if numero < 0:
#     print("Este número es NEGATIVO")
# else:
#     print("Este número NO ES NEGATIVO")
#**************************************************************
#--------------------El uso de elif----------------------------
# ahorros = int(input("Ingrese cúanto tiene de ahorros actualmente: "))
# if ahorros == 0:
#     print("Lo sentimos, no tiene ningun ahorro.")
# elif ahorros < 1500:
#     print("Estas bien.")
# elif ahorros < 6000:
#     print("Es una muy buena suma.") 
# elif ahorros < 15000:
#     print("Bienvenido Señor/a")
# else:
#     print("GRACIAS.")
#***************************************************************
#------------------Declaración de If anidados-------------------
# nevar = True
# temperatura = -7
# if temperatura < 0:
#     print("Se está congelando")
#     if nevar:
#         print("     Ponte las botas.")
#     print("Hora del chocolate caliente!")
# print("Adiós Mundo")
# print("---------------------------------")
# nevar = True
# temperatura = -7
# if temperatura < 0:
#     print("Se está congelando")
#     if nevar:
#         print("     Ponte las botas.")
#         print("     Hora del chocolate caliente!")
# print("Adiós Mundo")
#*****************************************************************
#------------------------Expresiones If---------------------------
# edad = 23
# estado = None
# if (edad > 14) and (edad < 22):
#     estado = "Adolescente"
# else: 
#     estado = "No es adolescente"
# print("A los ", edad, "--> ", estado)
# print("-----------------------------")
# estado = ("Adolescente" if edad>15 and edad<20 else "No es adolescente")
# print(estado)
#******************************************************************
#----------------------Bucle While---------------------------------
# contador = 0 
# print('Comenzar') 
# while contador < 15: 
#  print(contador, ' ', end='')  
#  contador += 1  
# print()  
# print('Terminado')
#****************************************************************
#----------------------Bucle For---------------------------------
# print('Imprimir valores en un rango') 
# for x in range(0, 20): 
#  print(x, ' ', end='') 
# print() 
# print('Terminando') 
# print('-----------------------------------------------------------------') 
# print('Imprima valores en un rango con un incremento de 2') 
# for i in range(0, 20, 2): 
#  print(i, ' ', end='') 
# print() 
# print('Terminando') 
# print('-----------------------------------------------------------------')
# for _ in range(0,15): 
#  print('*', end='') 
# print()
#***************************************************************
#------------------Declaración de rotura del bucle-------------------
# print('Solo imprima el código si se completan todas las iteraciones') 
# num = int(input('Introduzca un número para comprobar si esta en el rango: ')) 
# for i in range(0, 20): 
#     if i == num: 
#         break
#     print(i, ' ', end='')
# print() 
# print('Terminando') 
#******************************************************************
#------------------Declaración del bucle continuo------------------
# for i in range(0, 14): 
#     print(i, '\n', end='') 
#     if i % 2 == 1: 
#         continue
#     print('Este es un numero par') 
#     print('Nosotros amamos los numeros pares') 
# print('Terminando') 
#******************************************************************
#-----------------Bucle For con Else-------------------------------
# print('Solo imprima código si se completan todas las iteraciones') 
# num = int(input('Ingrese un numero para chequear el for: ')) 
# for i in range(0, 20): 
#     if i == num: 
#         break
#     print(i, ' ', end='') 
# else: 
#     print() 
#     print('Todas las iteraciones son exitosas') 
#*****************************************************************
#-----------------Juego de tirar dados----------------------------
# import random 
# MIN = 1 
# MAX = 6 
# tiro_nuevo = 'si' 
# while tiro_nuevo == 'si': 
#     print('Los dados estan rodando...') 
#     print('Los valores son...') 
#     dice1 = random.randint(MIN, MAX) 
#     print(dice1) 
#     dice2 = random.randint(MIN, MAX) 
#     print(dice2) 
#     tiro_nuevo = input('¿Desea tirar los dado de nuevo? (si / no): ')

