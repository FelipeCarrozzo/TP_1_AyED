from Ejercicio_1.modulos.LDE_con_metodos_m import ListaDobleEnlazada
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
        return self.items.tamanio 
    
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
        self.estado = estado
        self._jerarquia = jerarquia
            
    def __str__(self):
        if self.estado == "Boca abajo":
            return "-X"    #pregunta si la carta está boca abajo, no muestra el valor ni el palo. 
        else:
            return str(self._valor)+ str(self._palo)
        
    def __eq__(self, otro):
        return self._jerarquia == otro._jerarquia
    
    def __lt__(self,otro):
        return self._jerarquia < otro._jerarquia
        
    def __gt__(self,otro):
        return self._jerarquia > otro._jerarquia
    
   
    
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
        
        
    def jugar_carta(self, nuevo_estado ="a"): #metodo para dar vuelta una carta
        carta = self.mazo.removerFinal()
        carta.estado = nuevo_estado 
        return  (carta)     
    
    
        
    def retirar_mesa(self,cartas_mesa):
        for i in cartas_mesa:
            cartas_mesa.removerFinal()
            
    def __len__(self):
        return self.mazo.tamanio()
    
    def jugador_gana(self,carta, nuevo_estado ="a"): #metodo para agregar las cartas ganadas ABAJO del mazo
        carta.dato.estado = nuevo_estado  
    
        self.mazo.agregarFrente(carta)
        
        
        
        
#%%

class JuegoGuerra:
    def __iter__(self):
        return iter(self.mazo)
     
    def __init__(self,random_seed ):
        self.mazomesa = Mazo()
        self.mazo1 = Mazo()
        self.mazo2 = Mazo()
        self.semilla = random_seed 
        self.turnos_jugados = 0
        self.ganador = ""
        
    def crear_mazo(self):    
        valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        palos = ['♠', '♥', '♦', '♣']
        lista_cartas = [] 
        jerarquia=0
        for numero in valores:
            jerarquia+=1
            for palo in palos:
                carta=Carta(numero,palo,jerarquia,"a")
                lista_cartas.append(carta)
            
        rd.seed(self.semilla)
        rd.shuffle(lista_cartas)

        for carta in lista_cartas:
            
            self.mazomesa.agregar_carta(carta)
        return self.mazomesa
    
        
    def repartir(self):
        for i,carta in enumerate(self.mazomesa):  # i es la posición
            
            if i%2 == 0:                          # si el resto de pos div 2 = 0:
                self.mazo1.agregar_carta(carta)   # agregar al mazo 1
                
            if i%2 != 0:                          # si el resto de pos div 2 ≠ 0:
                self.mazo2.agregar_carta(carta)   # agrego al mazo 2
                
        return "MAZO REPARTIDO.", "\n","Mazo 1: ",(self.mazo1),"\n","Mazo 2:" ,  (self.mazo2)
    
    def iniciar_juego(self):
        self.crear_mazo()
        self.repartir()
        print("-----------------------------------")
        cartas_mesa =  []
        guerra = False
        while self.turnos_jugados < 10000:
            if guerra == False:
                try:
                    self.turnos_jugados += 1
                    c1=self.mazo1.jugar_carta()
                    cartas_mesa.append(c1.dato)
                    c2=self.mazo2.jugar_carta()
                    cartas_mesa.append(c2.dato)
                    '''Tomo la carta de mas arriba de cada mazo
                    y las agrego a carta_mesa respectivamente'''
                except IndexError:
                    if len(self.mazo1) == 0:
                        self.ganador = "jugador 2"
                        return self.ganador
            
                    elif len(self.mazo2) == 0:
                        self.ganador = "juagdor 1"
                        return self.ganador
                    
                
                print("turno número:",self.turnos_jugados)
                for carta in cartas_mesa:
                    print(carta)
                print("---------")
                print("\n")
                if cartas_mesa[-2] > cartas_mesa[-1]:   # Si el jugador 1 tiene la carta mas grande, entra en esta condición
                    for i in cartas_mesa:
                        self.mazo1.jugador_gana(i)
                        
                    cartas_mesa = []
                    print(self.mazo1, "\n","------","\n")
                    print(self.mazo2)
                    if guerra == True:
                        guerra = False
                        
                elif cartas_mesa[-1] > cartas_mesa[-2]: # Si el jugador 2 tiene la carta mas grande, entra en esta condición
                    for i in cartas_mesa:
                        self.mazo2.jugador_gana(i)
                        
                    cartas_mesa = []
                    print(self.mazo1, "\n","------","\n")
                    print(self.mazo2)
                    if guerra == True:
                        guerra = False
                            
                elif cartas_mesa[-1] == cartas_mesa[-2]:
                      # Si ambas cartas son iguales
                    if guerra == False:
                        guerra = True
                        try:
                            print("***GUERRA***")
                            for carta in range(0,3):
                                '''Se juegan 4 cartas más por jugador'''
                                c3 = self.mazo1.jugar_carta("Boca")
                                cartas_mesa.append(c3.dato)
                                c4 = self.mazo2.jugar_carta("Boca")
                                cartas_mesa.append(c4.dato)
                            c1=self.mazo1.jugar_carta("a")
                            cartas_mesa.append(c1.dato)
                            c2=self.mazo2.jugar_carta("a")
                            cartas_mesa.append(c2.dato)
                
                        except IndexError:
                            print("fin del juego")
                            if len(self.mazo1) == 0:
                                self.ganador = "jugador 2"
                                return self.ganador
          
                            elif len(self.mazo2) == 0:
                                self.ganador = "jugador 1"
                                return self.ganador
                              
                          
                    print("cartas en juego:")
                    for carta in cartas_mesa:
                        print(carta)
                    
            else:
                if cartas_mesa[-2] > cartas_mesa[-1]:
                    for i in cartas_mesa:
                        self.mazo1.jugador_gana(i)
                        
                    cartas_mesa = []
                    print(self.mazo1, "\n","------","\n")
                    print(self.mazo2)
                    if guerra == True:
                        guerra = False
                            
                    
                elif cartas_mesa[-1] > cartas_mesa[-2]: 
                    for i in cartas_mesa:
                        self.mazo2.jugador_gana(i)
                        
                    cartas_mesa = []
                    print(self.mazo1, "\n","------","\n")
                    print(self.mazo2)
                    if guerra == True:
                        guerra = False
                            
                elif cartas_mesa[-1] == cartas_mesa[-2]:
                    
                    if guerra == False:
                        guerra = True
                    try:
                        print("***GUERRA***")
                        for carta in range(0,3):
                            '''Se juegan 4 cartas más por jugador'''
                            c3 = self.mazo1.jugar_carta("Boca abajo")
                            cartas_mesa.append(c3.dato)
                            c4 = self.mazo2.jugar_carta("Boca abajo")
                            cartas_mesa.append(c4.dato)
                        c1=self.mazo1.jugar_carta("a")
                        cartas_mesa.append(c1.dato)
                        c2=self.mazo2.jugar_carta("a")
                        cartas_mesa.append(c2.dato)
                
                    except IndexError:
                              if len(self.mazo1) == 0:
                                  self.ganador = "jugador 2"
                                  break
            
                              elif len(self.mazo2) == 0:
                                  self.ganador = "jugador 1"
                                  break
                   
                    
                    print("cartas en juego:")
                    for carta in cartas_mesa:
                        print(carta)
         
        if self.mazo1 and self.mazo2:
            return("empate")
                
             

if __name__ == "__main__":
    
    obj=JuegoGuerra(random_seed= 314)
    # obj.crear_mazo() #3 es la semilla, que hace que la "mezcla" de las cartas 
    # obj.repartir()

    print(len(obj.mazo1))
    print(obj.mazo2)
    print()
    print()
    
    print(obj.iniciar_juego())
    print(obj.turnos_jugados)