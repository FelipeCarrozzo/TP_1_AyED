# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 10:26:03 2022

@author: Felipe
"""

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