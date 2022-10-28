from Ejercicio2.modulos.Mazo import Mazo
from Ejercicio2.modulos.Carta import Carta 
import random as rd

class JuegoGuerra:
    def __iter__(self):
        return iter(self.mazo)
     
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
                carta=Carta(numero,palo,jerarquia,"A")
                lista_cartas.append(carta)
            
        rd.seed(self.semilla)
        rd.shuffle(lista_cartas)

        for carta in lista_cartas:
            self.mazomesa.agregar_carta(carta)
        return self.mazomesa

#%% 

    def repartir(self):
        for i,carta in enumerate(self.mazomesa):  # i es la posición
            if i%2 == 0:                          # si el resto de pos div 2 = 0:
                self.mazo1.agregar_carta(carta)   # agregar al mazo 1
                
            if i%2 != 0:                          # si el resto de pos div 2 ≠ 0:
                self.mazo2.agregar_carta(carta)   # agrego al mazo 2
                
        return "MAZO REPARTIDO", str(self.mazo1) +  str(self.mazo2)
    
#%%
    def jugar(self):
        print("-----------------------------------")
        turno = 0
        cartas_mesa =  []
        while turno < 100:
            turno += 1

            while self.mazo1 and self.mazo2:
    
                c1=self.mazo1.jugar_carta("boca abajo")
                cartas_mesa.append(c1)
                c2=self.mazo2.jugar_carta("boca abajo")
                cartas_mesa.append(c2)
                '''Tomo la carta de mas arriba de cada mazo
                y las agrego a carta_mesa respectivamente'''
                if cartas_mesa[-2] > cartas_mesa[-1]:
                    for i in cartas_mesa:
                        print(cartas_mesa)
                        self.mazo1.jugador_gana(i)
                    
                    #self.mazo1.Jugador_gana(cartas_mesa)
                elif cartas_mesa[-1] > cartas_mesa[-2]: 
                    for i in cartas_mesa:
                        print(cartas_mesa)
                        self.mazo2.jugador_gana(i)
                        
                    #self.mazo1.Jugador_gana(cartas_mesa)
                else:
                    print("***GUERRA***")
                    for carta in range(0,3):
                        
                    
                        c3 = self.mazo1.jugar_carta()
                        cartas_mesa.append(c3)
                        c4 = self.mazo2.jugar_carta()
                        cartas_mesa.append(c4)
                    # c1=self.mazo1.jugar_carta("boca arriba") #remueve la carta de arriba
                    # cartas_mesa.append(c1)
                    # c2=self.mazo2.jugar_carta("boca arriba")
                    # cartas_mesa.append(c2)
                    
            
                
        
            if self.mazo1 == None:
                print("jugador 2 gana el juego")
                break
            elif self.mazo2 == None:
                print("Jugador 1 es el ganador")
                break
            
                # return cartas_mesa
            
                    
                
                    
#%%


if __name__ == "__main__":
    
    obj=JuegoGuerra(2)
    obj.crear_mazo() #3 es la semilla, que hace que la "mezcla" de las cartas 
    print(obj.repartir())
    print()
    print()
    # print(obj.mazo1)
    # print(obj.mazo2)
    #print(obj.repartir())
    print(obj.jugar())
    # print(lista)
