
class Carta:
       
    
    def __init__(self, valor = 0, palo = 0, estado = "Boca abajo",jerarquia=0):
        '''
        Parameters
        ----------
        valor : TYPE str
            Número de la carta. Por defecto es 0.
        palo : TYPE str
            Palo de la carta. Por defecto default is 0.
        estado : TYPE, optional
            DESCRIPTION. The default is "Boca abajo".
        jerarquia : TYPE, optional
            DESCRIPTION. The default is 0.

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
        return str(self._valor) + str(self._palo)
       
        
       
    
    
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
    obj=Carta(2,2)
    print(obj)
    
    
    