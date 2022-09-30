# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:17:20 2022

@author: Felipe
"""
import random as rd
def crear_mazo():    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
    lista_cartas = [] 
    jerarquia=0
    for numero in valores:
        jerarquia+=1
        for palo in palos:
            carta=numero,palo,jerarquia
            lista_cartas.append(carta)
     
    rd.seed(3)
    rd.shuffle(lista_cartas)
    return lista_cartas

#%%
def repartir(lista):
    mazo1=[]
    mazo2=[]
    for i, carta in enumerate(lista):
        if i%2 == 0:
            mazo1.append(carta)
            
        if i%2 != 0:  
            mazo2.append(carta)
            
    return f"MAZO !1: {mazo1}  MAZO 2: {mazo2}"


#%%
# def jugar(mazo1,mazo2):

#     while mazo1 and mazo2:
#         cartas_mesa =  []
    
#         c1=mazo1.jugar_carta("boca arriba")
#         cartas_mesa.append(c1)
#         c2=mazo2.jugar_carta("boca arriba")
#         cartas_mesa.append(c2)
#         '''Tomo la carta de mas arriba de cada mazo
#         y las agrego a carta_mesa respectivamente'''
#         if cartas_mesa[-2] > cartas_mesa[-1]:
#             for i in cartas_mesa:
#                 mazo1.agregarFrente(i)
#             #self.mazo1.Jugador_gana(cartas_mesa)
#         elif cartas_mesa[-1] > cartas_mesa[-2]: 
#             for i in cartas_mesa:
#                 mazo2.agregarFrente(i)
#             #self.mazo1.Jugador_gana(cartas_mesa)
#         else:
#             for carta in range(0,3):
#                 c3 = mazo1.removerFinal()
#                 cartas_mesa.append(c3)
#                 c4 = mazo2.removerFinal()
#                 cartas_mesa.append(c4)
#              #remueve la carta de arriba
#             cartas_mesa.append(c1)
            
#             cartas_mesa.append(c2)
            
#         return cartas_mesa

#%%

lista=crear_mazo()
print(lista)
print()
repartir_ = repartir(lista)
print(repartir_)