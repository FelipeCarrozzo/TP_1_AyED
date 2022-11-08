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
    
    """MÉTODOS MÁGICOS PARA COMPARACIONES, USADOS EN EL JUEGOGUERRA"""
    def __eq__(self, otro):
        return self._dato == otro._dato
    
    def __lt__(self,otro):
        return self._dato < otro._dato
        
    def __gt__(self,otro):
        return self._dato > otro._dato
    
#%% creacion de la lista doblemente enlazada

class ListaDobleEnlazada:

    def __init__(self):
        self.cabeza = None  
        self.cola = None
        self._tamanio = 0  
    
    def __iter__(self):
        
        nodo = self.cabeza
        while nodo:
            yield nodo 
            nodo = nodo.siguiente 
        
    def __str__(self):
        return str([nodo.dato for nodo in self])
         
    def esta_vacia(self):
        return self.tamanio == 0 
 
    @property
    def tamanio(self):
        return self._tamanio
        
#%%
    def agregar(self, item):
        '''
        Parameters
        ----------
        item : any TYPE 
            
        MÉTODO AGREGAR(item): AGREGA UN ELEMENTO (Nodo)
        AL PRINCIPIO DE LA LISTA DOBLEMENTE ENLAZADA
        Returns
        -------
        None.

        '''
        nuevo_nodo=Nodo(item)
        
        if self.tamanio==0:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo 
            self.cabeza=nuevo_nodo 
        
        self._tamanio+=1 
        
        
    def anexar(self,item):
        '''
        Parameters
        ----------
        item : any TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        -------
        Método anexar(item): anexa un elemento (nodo) 
        en el extremo final de la lista doblemente enlazada'''
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
        '''
        Parameters
        ----------
        posicion : int
            ES LA POSICION DENTRO DE 
            LA LDE EN LA QUE SE INSERTARÁ EL ELEMENTO.
        item :  any TYPE
            ES EL ELEMENTO QUE SE INSERTARÁ DENTRO DE LA LDE
            EN LA POSICIÓN INDICADA.

        Raises
        ------
        IndexError
            DEVUELVE UN IndexError SI LA POSICIÓN ES UN ENTERO NEGATIVO
            O SI ES MAYOR AL TAMAÑO DE LA LDE.

        -------
        None.

        '''
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
            self._tamanio +=1 

        else:
            temp=self.cabeza
            for i in range (posicion):
                   temp=temp.siguiente
            temp.anterior.siguiente = nuevo_nodo
            nuevo_nodo.anterior = temp.anterior
            nuevo_nodo.siguiente = temp
            temp.anterior = nuevo_nodo
            self._tamanio +=1
   
    def extraer(self, posicion=-1):
        '''
        Parameters
        ----------
        posicion : TYPE int
             Por defecto es -1.

        Raises
        ------
        IndexError
            Mientras que la posición pasada sea menor a
            -1 o sea mayor al tamaño de la lista, devuelve
            un IndexError.

        Returns
        -------
        any TYPE 
            Retorna el elemento que eliminó en la posición indicada.

        '''
        if posicion < -1 or posicion >= self._tamanio:
            raise IndexError 
            
        elif posicion == 0:
            temp = self.cabeza 
            self.cabeza = temp.siguiente 
            self._tamanio -= 1
            return temp
        
        
        elif posicion == self._tamanio -1 or posicion == -1:
            temp = self.cola
            self.cola = temp.anterior 
            self._tamanio -=1
            return temp 
        
        else:
            actual = self.cabeza 
            for i in range(posicion):
                actual = actual.siguiente 
                
            actual.anterior.siguiente = actual.siguiente 
            actual.anterior = actual.siguiente 
            self._tamanio -=1
            return actual 
        
        self._tamanio -=1                      
            
          
    def copiar(self):
        '''
        Returns
        -------
        copia_lista : any TYPE
            Retorna una copia idéntica de la lista.

        '''
        
        copia_lista = ListaDobleEnlazada()
        for nodo in self:
            copia_lista.anexar(nodo.dato)
        return copia_lista 
            
    def concatenar(self,lista):
        '''
        Parameters
        ----------
        lista : any TYPE

        Returns
        -------
        any TYPE
            Retorna dos listas concatenadas.

        '''
        temp = lista.cabeza

        for i in range(lista.tamanio):
            self.anexar(temp.dato)
            temp = temp.siguiente 
        return self 
   
    
    def __add__(self,lista):
        '''
        Parameters
        ----------
        a : lista 
            Usando el caracter "+" se concatenan las listas.

        Returns
        -------
        list

        '''
        return self.concatenar(lista)
        
    
    def invertir(self):
        '''
        Returns
        -------
        Retorna la lista con su orden invertido.

        '''
        nodo1 = self.cabeza 
        nodo2 = nodo1.siguiente 
        temp = self.cabeza
        
        nodo1.siguiente = None 
        nodo1.anterior = nodo2 
        
        while nodo2 != None:
            nodo2.anterior = nodo2.siguiente 
            nodo2.siguiente = nodo1
            nodo1 = nodo2 
            nodo2 = nodo2.anterior 
        self.cabeza = nodo1 
        self.cola = temp 
    
    
    def ordenar (self):
        '''el método de ordenamiento implementado fue el de burbuja. 
        Este, toma de a dos elementos y los compara: si el primero 
        es más chico que el segundo, está ordenado y el cambio 
        no se produce. De lo contrario, invierte las posiciones 
        de estos dos elementos. '''
        extremo = None
        while self.cabeza != extremo:
            actual = self.cabeza 
            temp = self.cabeza 
            
            while temp.siguiente != extremo: 
                cambio = temp.siguiente 
                if temp.dato > cambio.dato:
                    temp.siguiente = cambio.siguiente 
                    cambio.siguiente = temp 
                    if temp != self.cabeza:
                        actual.siguiente = cambio 
                    else:
                        self.cabeza = cambio
                    aux = temp
                    temp = cambio 
                    cambio = aux
                actual = temp 
                temp = temp.siguiente 
            extremo = temp
        return self 
#%%          
            
if __name__ == "__main__":

    nodo1 = Nodo(5)
    # print(nodo1.siguiente)
    
    lista1 = ListaDobleEnlazada()
    
    lista1.agregar(1)
    lista1.agregar(5)
    lista1.agregar(15)
    lista1.anexar(-5)
    lista1.anexar(-10)
    lista1.insertar(2,7)
    print(lista1)
    #print(lista1.invertir())
    # print(lista1.ordenar())
    
    lista2 = ListaDobleEnlazada() 
    
    lista2.agregar(1)
    lista2.agregar(2)
    lista2.agregar(3)
    lista2.agregar(4)
    lista2.agregar(5)
    print(lista2)
    lista2.insertar(4, "fito")
    print(lista1.concatenar(lista2))
    
    # print(lista2.invertir())
    # print(lista2.ordenar())
    
    print(lista1+lista2)
    # print(lista3.ordenar())
    
    
    # print(lista1.extraer())


