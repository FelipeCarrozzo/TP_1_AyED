from Ejercicio1.Modulos.LDE import ListaDobleEnlazada
import random as rd

#%%

class ColaDoble():

    def __init__(self):
        self.items = ListaDobleEnlazada()
        
    def __iter__(self):
        return iter(self.items)
            
    def __str__(self):
        lista = [str(nodo) for nodo in self]
        return str(lista) #se agrego str

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
    
#%%

class Carta:
    def __init__(self, valor = 0, palo = 0, jerarquia=0, estado = "Boca abajo"):
        '''
        Parameters
        ----------
        valor : TYPE str
            Número de la carta. Por defecto es 0.
        palo : TYPE str
            Palo de la carta. Por defecto default is 0.
        estado : TYPE optional
            Por defecto es "Boca abajo".
        jerarquia : TYPE optional
            Por defecto es 0.

        Returns
        -------
        None.

        '''
        self._valor = valor
        self._palo = palo
        self._estado = estado
        self._jerarquia = jerarquia
            
    def __str__(self):
        if self._estado == "Boca abajo":
            return "-X"    #pregunta si la carta está boca abajo, no muestra el valor ni el palo. 
        else:
            return str(self._valor)+","+ str(self._palo)
        
    def __lt__(self,otro):
        return self.jerarquia < otro.jerarquia
        
    def __gt__(self,otro):
        return self.jerarquia > otro.jerarquia
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter 
    def estado(self,nuevo_estado):
        self._estado = nuevo_estado
    
    @property
    def jerarquia(self):
        return self._jerarquia

    
#%%

class Mazo:
    
    def __init__(self):
        self.mazo = ColaDoble()
    
    def __str__(self):
        return str(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)
    
    def agregar_carta(self,carta): #Metodo que agrega cartas al mazo principal
        self.mazo.agregarFinal(carta)
        
    def jugar_carta(self,nuevo_estado="Boca abajo"): #metodo para dar vuelta una carta
        carta = self.mazo.removerFinal()
        carta.estado = nuevo_estado 
        return  str(carta)     
    
    def jugador_gana(self,lista_carta): #metodo para agregar las cartas ganadas ABAJO del mazo
        carta = self.mazo.agregarFrente(lista_carta)
        return carta
        
        
#%%

class JuegoGuerra:
    def __iter__(self):
        return iter(self.mazo)
     
    def __init__(self,Semilla = 5):
        self.mazomesa = Mazo()
        self.mazo1 = Mazo()
        self.mazo2 = Mazo()
        self.semilla = Semilla 

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
        return "MAZO CREADO", str(self.mazomesa)

    def repartir(self):
        for i,carta in enumerate(self.mazomesa):  # i es la posición
            if i%2 == 0:                          # si el resto de pos div 2 = 0:
                self.mazo1.agregar_carta(carta)   # agregar al mazo 1
                
            if i%2 != 0:                          # si el resto de pos div 2 ≠ 0:
                self.mazo2.agregar_carta(carta)   # agrego al mazo 2
                
        return "MAZO REPARTIDO", str(self.mazo1) +  str(self.mazo2)
    # def jugar(self):
    #     print("-----------------------------------")
    #     turno = 0
    #     cartas_mesa =  []
    #     while turno < 100:
    #         turno += 1

    #         while self.mazo1 and self.mazo2:
    
    #             c1=self.mazo1.jugar_carta("boca abajo")
    #             cartas_mesa.append(c1)
    #             c2=self.mazo2.jugar_carta("boca abajo")
    #             cartas_mesa.append(c2)
    #             '''Tomo la carta de mas arriba de cada mazo
    #             y las agrego a carta_mesa respectivamente'''
    #             if cartas_mesa[-2] > cartas_mesa[-1]:
    #                 for i in cartas_mesa:
    #                     self.mazo1.jugador_gana(i)
                    
                    
    #             elif cartas_mesa[-1] > cartas_mesa[-2]: 
    #                 for i in cartas_mesa:
    #                     self.mazo2.jugador_gana(i)

    #             else:
    #                 print("***GUERRA***")
    #                 for carta in range(0,3):
                        
                    
    #                     c3 = self.mazo1.jugar_carta()
    #                     cartas_mesa.append(c3)
    #                     c4 = self.mazo2.jugar_carta()
    #                     cartas_mesa.append(c4)
    #                 # c1=self.mazo1.jugar_carta("boca arriba") #remueve la carta de arriba
    #                 # cartas_mesa.append(c1)
    #                 # c2=self.mazo2.jugar_carta("boca arriba")
    #                 # cartas_mesa.append(c2)
                    
    #         if self.mazo1 == None:
    #             print("jugador 2 gana el juego")
    #             break
    #         elif self.mazo2 == None:
    #             print("Jugador 1 es el ganador")
    #             break
            
    #             # return cartas_mesa
#%%
if __name__ == "__main__":
    
    obj=JuegoGuerra(2)
    print(obj.crear_mazo()) 
    print((obj.repartir()))

