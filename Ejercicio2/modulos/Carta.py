
class Carta:
    def __init__(self, valor = 0, palo = 0, jerarquia=0, estado = "Boca abajo"):
        '''
        Parameters
        ----------
        valor : TYPE str
            Número de la carta. Por defecto es 0.
        palo : TYPE str
            Palo de la carta. Por defecto default is 0.
        estado : TYPE optional
            Por defecto es "Boca abajo".
        jerarquia : TYPE optional
            Por defecto es 0.

        Returns
        -------
        None.

        '''
        self._valor = valor
        self._palo = palo
        self._estado = estado
        self._jerarquia = jerarquia
            
    def __str__(self):
        if self._estado == "Boca abajo":
            return "-X"    #pregunta si la carta está boca abajo, no muestra el valor ni el palo. 
        else:
            return str(self._valor)+","+ str(self._palo)
        
    def __lt__(self,otro):
        return self.jerarquia < otro.jerarquia
        
    def __gt__(self,otro):
        return self.jerarquia > otro.jerarquia

    
#%%    
    @property
    def valor(self):
        return self._valor
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter 
    def estado(self,nuevo_estado):
        self._estado = nuevo_estado
    
    @property
    def jerarquia(self):
        return self._jerarquia
    
    
if __name__  == "__main__":
    carta=Carta(5,6,3,"A")
    print(carta)
    
    
    