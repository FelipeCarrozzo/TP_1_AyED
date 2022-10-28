from Ejercicio1.Modulos.LDE import ListaDobleEnlazada

'''Importo los métodos de la listadobleEnlazada'''

class ColaDoble():

    def __init__(self):
        self.items = ListaDobleEnlazada()
        
    def __iter__(self):
        return iter(self.items)
            
    def __str__(self):
        lista = [str(nodo) for nodo in self]

        return str(lista) #se agrego str


#%% MÉTODOS PARA LAS COLAS DOBLES (mazos)

    def estaVacia(self):
        return self.items.esta_vacia()

    def agregarFrente(self, item): #anexa al final de la cola doble
        self.items.anexar(item)    #para cuando reparte las cartas

    def agregarFinal(self, item): # agrega al principio de la cola doble
        self.items.agregar(item) # para cuando un jugador gana

    def removerFrente(self): #no se usa porque saca elementos de abajo del mazo, eso no se usa
        return self.items.extraer(self.items.tamanio-1)

    def removerFinal(self): #remueve del principio
        return self.items.extraer(0) #para cuando se juega una carta

    def tamanio(self):
        return len(self.items) 
    
        
    

if __name__ == "__main__":
    
    a=ColaDoble()
    a.agregarFinal(1)
    # a.agregar
    a.agregarFrente(5)
    a.removerFinal()
    print(a.estaVacia())
    print(a)

