from Ejercicio2.modulos.ClaseMazoDEF import Mazo
import random as rd

class JuegoGuerra(Mazo):
    
    def __init__(self):
        self.mazomesa = []
        self.mazo1 = Mazo(1)
        self.mazo2 = Mazo(2)
        
    def crear_mazo(self,semilla):    
        '''creo un método ya dentro de JuegoGuerra, creando el mazo
        dentro del archivo donde "se va a jugar"'''
        
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        
        for numero in valores:
            for palo in palos:
                self.mazomesa.append(numero+palo)
        rd.seed(semilla)
        rd.shuffle(self.mazomesa) 
        return self.mazomesa





        
    def repartir(self):
        pass
    
if __name__ == "__main__":
    obj=JuegoGuerra()
    obj.crear_mazo(3) #3 es la semilla, que hace que la "mezcla" de las cartas 
                        #(shuffle) sea siempre igual
    print(obj)