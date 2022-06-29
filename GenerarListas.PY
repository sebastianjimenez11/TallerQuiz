import random

class GenerarListas: 
    
    def GenerarListaUsuario():
        print("Ingrese 3 numeros=")
        a=int(input())
        b=int(input())
        c=int(input())
        lista=[a,b,c]
        print(lista)
        
    def GeneradorListaAleatoria():
        lista=[]
        for _ in range (0,100):
            a=random.randint(0,50)
        print(lista)
        
GenerarListas.GenerarListaUsuario()
GenerarListas.GeneradorListaAleatoria()
        