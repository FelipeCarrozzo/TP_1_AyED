from Ejercicio2.modulos.Mazo import Mazo
from Ejercicio2.modulos.Carta import Carta 
# from Ejercicio2.modulos.ColaDoble import ColaDoble
import random as rd

class JuegoGuerra:
     
    def __init__(self,semilla):
        self.mazomesa = Mazo()
        self.mazo1 = Mazo()
        self.mazo2 = Mazo()
        self.semilla = semilla 

    def crear_mazo(self):    
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        lista_cartas = [] 
        jerarquia=0
        for numero in valores:
            jerarquia+=1
            for palo in palos:
                carta=Carta(numero,palo,jerarquia)
                lista_cartas.append(carta)
            
        # rd.seed(self.semilla)
        rd.shuffle(lista_cartas)
        # cartas_mezcladas = lista
        for carta in lista_cartas:
            self.mazomesa.agregar_carta(carta)
        return self.mazomesa


        
    def repartir(self):
        for i, carta in enumerate(self.mazomesa):
            if i%2 == 0:
                self.mazo1.agregar_carta(carta)
                
            if i%2 != 0:  
                self.mazo2.agregar_carta(carta)
                
        return self.mazo1, self.mazo2
    
    # def jugar(self):

    #     while self.mazo1 and self.mazo2:
    #         cartas_mesa =  []
        
    #         c1=self.mazo1.jugar_carta("boca arriba")
    #         cartas_mesa.append(c1)
    #         c2=self.mazo2.jugar_carta("boca arriba")
    #         cartas_mesa.append(c2)
    #         '''Tomo la carta de mas arriba de cada mazo
    #         y las agrego a carta_mesa respectivamente'''
    #         if cartas_mesa[-2] > cartas_mesa[-1]:
    #             for i in cartas_mesa:
    #                 self.mazo1.agregarFrente(i)
    #             #self.mazo1.Jugador_gana(cartas_mesa)
    #         elif cartas_mesa[-1] > cartas_mesa[-2]: 
    #             for i in cartas_mesa:
    #                 self.mazo2.agregarFrente(i)
    #             #self.mazo1.Jugador_gana(cartas_mesa)
    #         else:
    #             for carta in range(0,3):
    #                 c3 = self.mazo1.removerFinal()
    #                 cartas_mesa.append(c3)
    #                 c4 = self.mazo2.removerFinal()
    #                 cartas_mesa.append(c4)
    #             c1=self.mazo1.jugar_carta("boca arriba") #remueve la carta de arriba
    #             cartas_mesa.append(c1)
    #             c2=self.mazo2.jugar_carta("boca arriba")
    #             cartas_mesa.append(c2)
                
    #         return cartas_mesa
                
                






if __name__ == "__main__":
    obj=JuegoGuerra(3)
    obj.crear_mazo() #3 es la semilla, que hace que la "mezcla" de las cartas 
    obj.repartir()   #(shuffle) sea siempre igual
    print(obj.mazo1)
    print(obj.mazo2)
    #print(obj.repartir())
    # print(obj.jugar())