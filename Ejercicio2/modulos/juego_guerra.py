from Ejercicio1.modulos.LDE import ListaDobleEnlazada

class ColaDoble(ListaDobleEnlazada):
    
    def __init__(self):
        self.items = []


    def agregarFrente(self, item):
        self.agregar(item)
        
    def agregarFinal(self, item):
        self.anexar(item)

    def removerFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

class JuegoGuerra:
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']


obj=ColaDoble()
obj.agregarFinal(1)
print(obj)


print(obj.esta_vacia())