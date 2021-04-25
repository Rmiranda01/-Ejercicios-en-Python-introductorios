class Nodo:
    def __init__(self, dato):
        
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
# Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def agregar_datos(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.agregar_datos(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agregar_datos(nodo.derecha, dato)

    def inorden_datos(self, nodo):
        if nodo is not None:
            self.inorden_datos(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.inorden_datos(nodo.derecha)

    def preorden_datos(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.preorden_datos(nodo.izquierda)
            self.preorden_datos(nodo.derecha)

    def postorden_datos(self, nodo):
        if nodo is not None:
            self.postorden_datos(nodo.izquierda)
            self.postorden_datos(nodo.derecha)
            print(nodo.dato, end=", ")

    def buscar_datos(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.buscar_datos(nodo.izquierda, busqueda)
        else:
            return self.buscar_datos(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, dato):
        self.agregar_datos(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo el árbol en inorden: ")
        self.inorden_datos(self.raiz)
        print("")

    def preorden(self):
        print("\nImprimiendo el árbol en preorden: ")
        self.preorden_datos(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo el árbol en postorden: ")
        self.postorden_datos(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.buscar_datos(self.raiz, busqueda)

arbol = Arbol("Ricardo")
arbol.agregar("Alexander")
arbol.agregar("Miranda")
arbol.agregar("Vivar")
arbol.agregar("Estudia")
arbol.agregar("Ingenieria")
arbol.agregar("En")
arbol.agregar("Sistemas")
# Agregar datos
nombre = input("Ingrese otro dato para agregar al árbol: ")
arbol.agregar(nombre)
print("\n******ORDENAMIENTOS DE UN ARBOL BINARIO CON CADENA DE CARACTERES******")
arbol.preorden()
arbol.inorden()
arbol.postorden()
# Búsqueda de datos 
busqueda = input("\nIngresa algun dato para buscar en el árbol: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"Lo sentimos -> {busqueda} no existe en el árbol \n")
else:
    print(f"{busqueda} sí existe en el árbol \n")
    
arbol_numeros = Arbol(20) 
arbol_numeros.agregar(19)
arbol_numeros.agregar(17)
arbol_numeros.agregar(12)
arbol_numeros.agregar(7)
arbol_numeros.agregar(13)
arbol_numeros.agregar(2)
arbol_numeros.agregar(18)
arbol_numeros.agregar(22)
arbol_numeros.agregar(35)
arbol_numeros.agregar(50)
arbol_numeros.agregar(24)
arbol_numeros.agregar(71)
arbol_numeros.agregar(90)
arbol_numeros.agregar(60)
print("\n******ORDENAMIENTOS DE UN ARBOL BINARIO CON NUMEROS ENTEROS******")
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()
# Búsqueda de datos
busqueda = int(input("\nIngresa un número para buscar en el árbol: "))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")