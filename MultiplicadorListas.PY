
from GenerarListas import generarListas

class multiplicadorListas(generarListas):
    def MultiplicarListas(self.):
        lista=generarListas()
        a=lista.GenerarListaUsuario(2)
        b=lista.GeneradorListaAleatoria(2)
        
        for i in range (2):
            print(a[i]*b[i])
     
multiplicadorListas.MultiplicarListas()
