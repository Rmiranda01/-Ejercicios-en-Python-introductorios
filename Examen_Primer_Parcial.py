#--------------------------------------------------------
                    #Ejercicio 1
#--------------------------------------------------------
cadena='(¡Hola a ‘” todas “’ y “’ todos!’”’)'
print(cadena)
print("\n")
#--------------------------------------------------------
                    #Ejercicio 2
#--------------------------------------------------------
username=('Ricardo')
print('¡Hola',username,'!')
print("\n")
#--------------------------------------------------------
                    #Ejercicio 3
#--------------------------------------------------------
x=1
y=0
o1=y|y
o2=y|x
o3=x|y
o4=x|x
print('A   B   Q')
print(y,'|',y,'=',o1)
print(y,'|',x,'=',o2)
print(x,'|',y,'=',o3)
print(x,'|',x,'=',o4)
print("\n")
#--------------------------------------------------------
                    #Ejercicio 4
#--------------------------------------------------------
h1=float(input('Ingrese el numero de horas de estudio a la semana: ')) 
p1=float(input('Ingrese el tiempo promedio de horas usadas: '))
totalh=round((h1*p1)*5,2) 
print('El total de horas empleadas en la semana es de: '+str(totalh))
print("\n")
#--------------------------------------------------------
                    #Ejercicio 5
#--------------------------------------------------------
m=int(input('Ingrese un valor para m: '))
suma=(m*(m+1))/2
print('La sumatoria desde 1 hasta '+str(m)+' es de: '+str(suma))
print("\n")
#--------------------------------------------------------
                    #Ejercicio 6
#--------------------------------------------------------
p=float(input('Ingrese su peso en libras: '))
a=float(input('Ingrese su altura en metros: '))
p2=p*0.453592
imc=p2/(a*a)
print("Tu índice de masa corporal es: ","{0:.2f}".format(imc))
print("\n")
#--------------------------------------------------------
                    #Ejercicio 7
#--------------------------------------------------------
a=float(input('Ingrese el primer valor flotante a: '))
b=float(input('Ingrese el segundo valor flotante b: '))
c=a/b
d=a%b
print("a entre b nos da como valores:")
print("Un cociente de: ","{0:.2f}".format(c))
print("Un resto de: ","{0:.2f}".format(d))
print("\n")
#--------------------------------------------------------
                    #Ejercicio 8
#--------------------------------------------------------
c=float(input('Ingrese el capital inicial: '))
i=float(input('Ingrese el interes anual que desea: '))
p=float(input('Ingrese el periodo: '))
Is=c*(1+(i*p/100))
cf=c+Is
print("El interes es de:  ","{0:.2f}".format(Is))
print("El capital obtenido con la inversion es de:  ","{0:.2f}".format(cf))
print("\n")
#--------------------------------------------------------
                    #Ejercicio 9
#--------------------------------------------------------
ba=int(input('Ingrese la cantidad de barrenos: '))
si=int(input('Ingrese la cantidad de sierras: '))
pb=ba*112
ps=si*75
pt=pb+ps
print("El peso total del paquete que sera enviado es de:  ",pt,'kg')
print("\n")
#--------------------------------------------------------
                    #Ejercicio 10
#--------------------------------------------------------
pme=20
cme=int(input('Ingrese la cantidad de memorias vendidas: '))
des=pme*0.6
pde=pme-des
ctf=pde*cme
print('El precio de una memoria nueva es de US$20')
print('El descuento de una memoria que no es nueva es de US$',des)
print('El coste final total es de US$',ctf)
