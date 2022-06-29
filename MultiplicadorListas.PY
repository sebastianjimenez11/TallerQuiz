
from GenerarListas import generarListas

class multiplicadorListas(generarListas):
    
    
    def MultiplicarListas(self):
        lista=generarListas()
        a=lista.GenerarListaUsuario(3)
        b=lista.GeneradorListaAleatoria(3)
        
        for i in range (3):
            print(a[i]*b[i])
     

