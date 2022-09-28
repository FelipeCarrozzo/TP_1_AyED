# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:22:23 2022

ESTE "MAZO" ANDA BIEN.
"""
from Ejercicio2.modulos.ColaDoble import ColaDoble
from Ejercicio2.modulos.Carta import Carta
import random as rd 
class Mazo:
    
    def __init__(self):
        self.mazo = ColaDoble()
    
    def __str__(self):
        return str(self.mazo)
    
    def agregar_carta(self,carta): #Metodo que agrega cartas al mazo principal
        self.mazo.agregarFinal(carta)
        
    def juegar_carta(self,nuevo_estado): #metodo para dar vuelta una carta
        carta = self.mazo.removerFinal()
        carta.estado = nuevo_estado 
        return  carta      
    
    
    


    
    
if __name__ == "__main__":
    obj=Mazo()
    obj.crear_mazo(3)
    print(obj)
    
    
