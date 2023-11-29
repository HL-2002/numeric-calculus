
# Clase matriz

class Matrix:
    def __init__(self, n):
        self.n = n
        self.matriz = []

    # Creacion de matriz 
    def crear(self):
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                valor = int(input(f"Ingrese valor de posicion [{i}][{j}]: "))
                fila.append(valor)
            self.matriz.append(fila)
    

    def imprimir(self):
        for fila in self.matriz:
            print(fila)
    
    # Matriz traspuesta
    def traspuesta(self):
        filas = len(self.matriz)
        cols = len(self.matriz[0])
        traspuesta = [[self.matriz[j][i] for j in range(filas)]
                      for i in range(cols)]
        print("Matriz traspuesta")
        for filas in traspuesta:
            print(filas)

# Entrada de datos
n = int(input("Ingrese la dimension de la matriz: "))
m = Matrix(n)
m.crear()
m.imprimir()
m.traspuesta()

    

    
        
