# with open("./datos/datos.txt") as datos:
#     n_lineas = sum(1 for linea in datos)

# with open("./datos/datos.txt") as datos, open("./datos/f1.txt","w") as f1, open("./datos/f2.txt.txt","w")as f2:
#     f=datos.readline()


def dividir_archivo (archivo,F1,F2):
    with open(archivo) as datos, open(F1,"w") as f1, open(F2,"w")as f2:
        dato1 = datos.readline()
        f1.write(dato1)
        dato2 = datos.readline()
        archi_aux = f1
        while dato2:   #mientras exista
            if dato2<dato1:
                if archi_aux == f2:
                    archi_aux = f1
                else:
                    archi_aux = f2
                    
            archi_aux.write(dato2)
            dato1 = dato2
            dato2 = datos.readline()
        return dato1, dato2

def mezclar_archivos(archivo1,archivo2,archivo_salida):
    with open(archivo1,"r") as f1, open(archivo2,"r") as f2, open(archivo_salida, "w")as f:
        dato1 = f1.readline()        # es el primer dato de f1
        dato2 = f2.readline()        # es el primer dato de f2
        dato_aux = dato1             # es el dato que queremos escribir en la lista de salida 
          
        sublistaf1 = True
        sublistaf2 = True
        while dato1 and dato2:    #mientras existan datos en dato1 y dato2 
            
            if dato2 < dato1:
                dato_aux = dato2
                dato2 = f2.readline()
                if dato2 < dato_aux:
                    
                    sublistaf2 = False 
            else:
                dato_aux = dato1
                dato1 = f1.readline()       
                if dato1 < dato_aux:
                    
                    sublistaf1 = False
                    
            if sublistaf1 == False:
                f.write(dato_aux)
                while dato_aux < dato2:
                    dato_aux = dato2
                    dato2 = f2.readline()
                    f.write(dato_aux)
                
                
            elif sublistaf2 == False:
                f.write(dato_aux)
                while dato_aux < dato1:
                    dato_aux = dato1
                    dato1 = f1.readline()
                    f.write(dato_aux)
                
            if sublistaf1 != False and sublistaf2 != False:
                f.write(dato_aux)
            else:
                sublistaf1 = True    
                sublistaf2 = True
            
        while dato2 and dato1 == None:  #No anda este while
            dato_aux = dato2
            dato2 = f2.readline()
            f.write(dato_aux)
        while dato1 and dato2 == None:
            dato_aux = dato1
            dato1 = f1.readline()
            f.write(dato_aux)
        
        
if __name__ == '__main__':
    datos = dividir_archivo("./datos.txt","./f1.txt","./f2.txt")
    print(datos)
    
    
