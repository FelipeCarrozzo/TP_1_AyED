from Ejercicio1.Modulos.LDE import ListaDobleEnlazada, Nodo
import random as rd
from Ejercicio2.modulos.Carta import Carta



class ColaDoble:
    def __init__(self):
        self.items = ListaDobleEnlazada()
        
    def __iter__(self):
        return iter(self.items)
            
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
    

# a=ColaDoble()
# a.agregarFinal(1)
# # a.agregar
# a.agregarFrente(5)
# print(a.estaVacia())
# print(a)

class Mazo:
    
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        return str(self.mazo) 
    
    def __iter__(self):
       pass 
    
    
    def crear_mazo(self):    
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        
        for numero in valores:
            for palo in palos:
                carta_nueva = Carta(numero,palo)
                self.mazo.append(carta_nueva)
                        
        rd.shuffle(self.mazo) 
        return self.mazo
    
    def comprarar_carta(self):
        pass
    
    def repartir(self):
       for carta in self.mazo:
           pass
   
    


if __name__ == "__main__":
    # MAZO=Mazo()
    # MAZO.crear_mazo()
    # print(MAZO.mazo)
    # c = ColaDoble()
    # c.agregarFinal(1)
    # c.agregarFinal(15)
    # print(c)
    obj=Mazo()
    obj.crear_mazo()
    print(obj)




