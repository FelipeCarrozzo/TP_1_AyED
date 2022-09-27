from Ejercicio1.Modulos.LDE import Nodo

class Carta:
    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
    
    def __init__(self, valor = 0, palo = 0):
        
        self._valor = valor
        self._palo = palo
        self._cara = "-X"
    
            
    def __str__(self):
       return str(self.valores[self._valor]+self.palos[self._palo])
   
    def __cmp__(self, otro):

       
        if self.valor > otro.valor: 
            return 1
        if self.valor < otro.valor: 
            return -1
   
    @property
    def valor(self):
        return self._valor
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def cara(self):
        return self._cara
    
    
