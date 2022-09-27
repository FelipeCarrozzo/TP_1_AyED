# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:22:23 2022

ESTE "MAZO" ANDA BIEN.
"""
import random as rd
class Mazo:
    
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        return str(self.mazo) 
    
    
    
    
    
    
if __name__ == "__main__":
    obj=Mazo()
    obj.crear_mazo(5)
    print(obj)