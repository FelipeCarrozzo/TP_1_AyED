from Ejercicio1.modulos.LDE import ListaDobleEnlazada, Nodo

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
# a.agregar
a.agregarFrente(5)
print(a.estaVacia())
print(a)

class Mazo(ListaDobleEnlazada, Nodo):

    def crear_mazo(self):    
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        mazo = ListaDobleEnlazada()
        for numero in valores:
            for palo in palos:
                self.anexar(numero+palo)
        return mazo 

    def repartir(self):
       pass 

if __name__ == "__main__":
    MAZO=Mazo()
    MAZO.crear_mazo()
    print(MAZO)




