# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:22:23 2022


"""
from Ejercicio2.modulos.ColaDoble import ColaDoble
from Ejercicio2.modulos.Carta import Carta
class Mazo:
    
    def __init__(self):
        self.mazo = ColaDoble()
    
    def __str__(self):
        return str(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)

#%%
    
    def agregar_carta(self,carta): #Metodo que agrega cartas al mazo principal
        self.mazo.agregarFinal(carta)
        
    def jugar_carta(self,nuevo_estado="Boca abajo"): #metodo para dar vuelta una carta
        carta = self.mazo.removerFinal()
        carta.estado = nuevo_estado 
        return  str(carta)     
    
    def jugador_gana(self,lista_carta): #metodo para agregar las cartas ganadas ABAJO del mazo
        
        carta = self.mazo.agregarFrente(lista_carta)
         
        
    
#%%
    
    
if __name__ == "__main__":
    obj=Mazo()
    obj.crear_mazo(3)
    print(obj)
    
    
