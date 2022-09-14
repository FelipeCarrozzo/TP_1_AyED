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
        
        
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, valor):    
        self._dato = valor
        
    @property
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self,valor):
        self._siguiente = valor
        
    @property
    def anterior (self):
        return self._anterior
    
    @anterior.setter
    def anterior (self,valor):
        self._anterior = valor
        
    def __str__(self):
        return str(self.dato)
#%% creacion de la lista doble. enlazada
class ListaDobleEnlazada:

    def __init__(self):
        self.cabeza = None  
        self.cola = None
        self._tamanio = 0  
    
    def __iter__(self):
        nodo = self.cabeza
        while nodo:
            yield nodo 
            nodo=nodo.siguiente
        
    def __str__(self):
        lista = [str(nodo) for nodo in self]
        return str(lista)
            
    def esta_vacia(self):
        return self.tamanio == 0 
    
    @property
    def tamanio(self):
        
        return self._tamanio
        
        
    def agregar(self, item):
        nuevo_nodo=Nodo(item)
        if self.tamanio==0:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo 
            self.cabeza=nuevo_nodo 
        
        self._tamanio+=1 
        
        
    def anexar(self,item):
        nuevo_nodo=Nodo(item)
        if self.tamanio == 0:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
            
        self._tamanio+=1
       
    def insertar(self,posicion,item):
        nuevo_nodo=Nodo(item)
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError 
            
        if posicion == 0:
            self.agregar(item)
            
        elif posicion == self.tamanio-1:
            self.cola.anterior.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola.anterior
            nuevo_nodo.siguiente = self.cola
            self.cola.anterior = nuevo_nodo
            
                
            
        else:
            temp=self.cabeza
            for i in range (posicion):
                   temp=temp.siguiente
            temp.anterior.siguiente = nuevo_nodo
            nuevo_nodo.anterior = temp.anterior
            nuevo_nodo.siguiente = temp
            temp.anterior = nuevo_nodo
            
    def extraer(self, posicion=-1):
        if posicion < -1 or posicion >= self.tamanio:
            raise IndexError 
        elif posicion == -1:
            eliminado = self.cola
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        else:
            actual = self.cabeza
            previo = None
            
            for i in range(posicion): 
                previo = actual
                actual = actual.siguiente
            eliminado = actual
            if previo == None:
                self.cabeza = actual.siguiente
            else:
                previo.siguiente=actual.siguiente
        
        self._tamanio -=1                      
        return eliminado    
                  
    def copiar(self):
        
        copia_lista = ListaDobleEnlazada()
        temp = self.cabeza
        for i in range(self._tamanio+1):
            copia_lista.anexar(temp.dato)
            temp = temp.siguiente
        return copia_lista 
            
    # def invertir(self):
            
    def concatenar(self,lista):
        
        lista_actual = self
        lista_pasada = lista
        temp = lista.cabeza
        for i in range(lista.tamanio):
            self.anexar(temp.dato)
            temp = temp.siguiente 
        return self
        
    
    # def concatenar2(self,lista):
        
    #     self.cola.siguiente = lista
    #     lista.cabeza.anterior = self
        
    #     nuevo_tamanio = self._tamanio + lista._tamanio
        
    #     return self,nuevo_tamanio
    
    
    
        
        
        
        
        
        
        
            
            
            
            
if __name__ == "__main__":

          

    nodo1 = Nodo(5)
    # print(nodo1.siguiente)
    
    lista1 = ListaDobleEnlazada()
    
    # print(lista1.tamanio())
    
    lista1.agregar(1)
    lista1.agregar(5)
    lista1.agregar(15)
    
    lista1.anexar(-5)
    lista1.anexar(-10)
    
    lista1.insertar(2,7)
   
    print(lista1)
    print(lista1.extraer(2))
    print(lista1)
    lista2 = ListaDobleEnlazada()
    lista2.agregar(1)
    lista2.agregar(2)
    lista2.agregar(3)
    print(lista2)
    print(lista1.concatenar(lista2))
    print(lista1.tamanio)
    # print(lista1.copiar())
    # print(lista1.tamanio())
    
    
    
    
    