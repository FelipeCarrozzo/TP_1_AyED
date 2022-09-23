# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:43:07 2022

@author: alumno
"""

from TP1_Carrozzo.LDE import ListaDobleEnlazada

class ColaDoble(ListaDobleEnlazada):
    
    def __init__(self):
        self.items = ListaDobleEnlazada()


    def agregarFrente(self, item):
        self.item.agregar(item)
        
    def agregarFinal(self, item):
        self.item.anexar(item)

    def removerFinal(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)

class JuegoGuerra:
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']


# obj=ColaDoble()
# obj.agregarFinal(1)
# print(obj)


# print(obj.esta_vacia())