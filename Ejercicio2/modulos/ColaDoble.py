from Ejercicio1.Modulos.LDE import ListaDobleEnlazada
import random as rd
'''Importo los métodos de la listadobleEnlazada'''

class ColaDoble():

    def __init__(self):
        self.items = ListaDobleEnlazada()
        
    def __iter__(self):
        return iter(self.items)
            
    def __str__(self):
        lista = [str(nodo) for nodo in self]
        return str(lista)
    
    def estaVacia(self):
        return self.items.esta_vacia()

    def agregarFrente(self, item): #anexa al final de la cola doble
        self.items.anexar(item)

    def agregarFinal(self, item):
        self.items.agregar(item) # agrega al principio de la cola doble

    def removerFrente(self):
        return self.items.extraer(self.items.tamanio-1)

    def removerFinal(self):
        return self.items.extraer(0) #remueve del principio

    def tamano(self):
        return len(self.items) 
    
        
    

if __name__ == "__main__":
    
    a=ColaDoble()
    a.agregarFinal(1)
    # a.agregar
    a.agregarFrente(5)
    a.removerFinal()
    print(a.estaVacia())
    print(a)

