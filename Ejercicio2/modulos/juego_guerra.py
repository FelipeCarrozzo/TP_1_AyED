from Ejercicio2.modulos.ClaseMazoDEF import Mazo


class JuegoGuerra(Mazo):
    
    def __init__(self):
        self.mazomesa = Mazo() 
        self.mazo1 = Mazo()
        self.mazo2 = Mazo()
        
    
    
    def IniciarJuego(self): #Llamo al método "crear_mazo" 
        def crear_mazo(self,semilla):    
            valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
            palos = ['♠', '♥', '♦', '♣']
            
            for numero in valores:
                for palo in palos:
                    carta_nueva = (numero+palo)
                    self.mazo.append(carta_nueva)
            rd.seed(semilla)
            rd.shuffle(self.mazo) 
            return self.mazo
    
    
    
    
    
        mazo = self.mazomesa.crear_mazo(3)
        
    def repartir(self):
        pass
    
if __name__ == "__main__":
    mazogral=JuegoGuerra()
    mazogral.IniciarJuego()
    print(mazogral)