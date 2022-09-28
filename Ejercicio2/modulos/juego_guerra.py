from Ejercicio2.modulos.Mazo import Mazo
from Ejercicio2.modulos.Carta import Carta 
import random as rd

class JuegoGuerra:
     
    def __init__(self,semilla):
        self.mazomesa = Mazo()
        self.mazo1 = Mazo()
        self.mazo2 = Mazo()
        self.semilla = semilla 
        
    # def crear_mazo(self):    
    #     '''creo un método ya dentro de JuegoGuerra, creando el mazo
    #     dentro del archivo donde "se va a jugar"'''
        
        # valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        # palos = ['♠', '♥', '♦', '♣']
        
        # for numero in valores:
        #     for palo in palos:
        #         self.mazomesa.agregar_carta(numero+palo)
        # rd.seed(self.semilla)
        # rd.shuffle(self.mazomesa) 
        # return self.mazomesa 
    def crear_mazo(self):    
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        lista_cartas = [] 
        
        for numero in valores:
            for palo in palos:
                lista_cartas.append(Carta(numero,palo))
            
        rd.seed(self.semilla)
        rd.shuffle(lista_cartas)
        # cartas_mezcladas = lista
        for carta in lista_cartas:
            self.mazomesa.agregar_carta(carta)
        return self.mazomesa




        
    def repartir(self):
        pass
    
if __name__ == "__main__":
    obj=JuegoGuerra(3)
    obj.crear_mazo() #3 es la semilla, que hace que la "mezcla" de las cartas 
                        #(shuffle) sea siempre igual
    print(obj.mazomesa)