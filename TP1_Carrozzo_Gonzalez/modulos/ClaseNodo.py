# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:56:04 2022

@author: alumno
"""
#%%  creación del nodo
class Nodo:
    
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
        
#%% creacion de la lista doble. enlazada
class ListaDobleEnlazada:

    def __init__(self):
        self.cabeza = None  
        self.cola = None
        self.tamanio = 0 # 
    
    def esta_vacia(self):
        return self.tamanio == 0 
    
    @property
    def tamanio(self):
        
        return self._tamanio
        
    @tamanio.setter
    def tamanio(self,tam):
        self._tamanio = tam 
        
    def agregar(self, item):
        nuevoNodo=Nodo(item)
        if self.tamanio==0:
            self.cabeza=nuevoNodo
            self.cola=nuevoNodo
        else:
            
            nuevoNodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevoNodo 
            self.cabeza=nuevoNodo 
        
        self.tamanio+=1 
        
        
    def anexar(self,item):
        nuevoNodo=Nodo(item)
        if self.tamanio ==0:
            self.cabeza=nuevoNodo
            self.cola=nuevoNodo
        else:
            nuevoNodo.siguiente = self.cola 
            self.cola.anterior = nuevoNodo
            self.cola=nuevoNodo
        self.tamanio+=1
       
    def insertar(self,posicion,item):
        nuevoNodo=Nodo(item)
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError 
            
        if posicion == 0:
            self.agregar(item)
            
        elif posicion == self.tamanio:
            self.anexar(item)
            
        else:
            
            temp=self.cabeza
            for _ in posicion-1:
                   temp=temp.siguiente
            nuevoNodo.siguiente=temp 
            temp.anterior.siguiente=nuevoNodo 
            nuevoNodo.anterior=temp.anterior 
            temp.anterior=nuevoNodo 

#%%
          

nodo1 = Nodo(5)
# print(nodo1.siguiente)
lista1 = ListaDobleEnlazada()
# print(lista1.tamanio())

# lista1.agregar("Algoritmo")
# print(lista1.tamanio())
