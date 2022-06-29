import random

class generarListas: 
    
    def GenerarListaUsuario(self,n):
        lista=[]
        for _ in range (n):            
            lista.append(int(input("ingrese los numeros que quiere")))
        print(lista)
        return lista
    
    def GeneradorListaAleatoria(self, n):
        lista=[]
        for _ in range (n):
            a=random.randint(0,50)
            lista.append(a)
        print(lista)
        return lista
        