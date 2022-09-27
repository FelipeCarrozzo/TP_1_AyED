# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:12:35 2022

@author: Usuario
"""
import random as rd

def crear_mazo(semilla):    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
    mazo = [] #lista de python
    for numero in valores:
        for palo in palos:
            mazo.append(numero+palo)
    rd.seed(semilla)
    rd.shuffle(mazo) #2) shuffle de la lista 3)cargamos las cartas al mazo
    return mazo

    
obj=crear_mazo(3)
print(obj)