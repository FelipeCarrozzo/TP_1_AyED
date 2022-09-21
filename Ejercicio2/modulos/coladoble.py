from Ejercicio1.modulos.LDE import ListaDobleEnlazada

class ColaDoble:
    def __init__(self):
        self.items = ListaDobleEnlazada()
        self.cabeza = None
    def __iter__(self):
        nodo = self.cabeza
        while nodo:
            yield nodo 
            nodo=nodo.siguiente
            
    def __str__(self):
        lista = [str(nodo) for nodo in self]
        return str(lista)
    
    def estaVacia(self):
        return self.items.esta_vacia()

    def agregarFrente(self, item):
        self.items.agregar(item)

    def agregarFinal(self, item):
        self.items.anexar(item)

    def removerFrente(self):
        return self.items.extraer(0)

    def removerFinal(self):
        return self.items.extraer()

    def tamano(self):
        return len(self.items) 
    

a=ColaDoble()
a.agregarFinal(1)
a.agregar
a.agregarFrente(5)
print(a.estaVacia())
print(a)