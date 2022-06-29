import random

class generarListas: 
    
    def GenerarListaUsuario(self):
        for _ in range (2):
            lista=[]
            lista.append(int(input("ingrese los numeros que quiere")))
            print(lista)
            return lista
    
    def GeneradorListaAleatoria(self, n):
        lista=[]
        for _ in range (0,100):
            a=random.randint(0,50)
        print(lista)
        return lista
generarListas.GenerarListaUsuario()
generarListas.GeneradorListaAleatoria()
        