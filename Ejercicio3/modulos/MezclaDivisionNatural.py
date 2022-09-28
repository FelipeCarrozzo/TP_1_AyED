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
# def mezclar_archivos(archivo1,archivo2,archivo_salida):
#     with open(archivo1,"r") as f1, open(archivo2,"r") as f2, open(archivo_salida)as f:
#         while archivo1:
#             pass
    
        
# def mezclar_archivos(archivo1,archivo2,archivo_salida):
#     with open(archivo1,"r") as f1, open(archivo2,"r") as f2, open(archivo_salida, "w")as f:
#         dato1 = f1.readline()        # es el primer dato de f1
#         dato2 = f2.readline()        # es el primer dato de f2
#         dato3 = f2.readline()
#         dato_aux = dato1             # es el dato que queremos escribir en la lista de salida 
#         while dato3:    #mientras existan datos en f2 
#             if dato3 > dato2:             #comparo el segundo dato de f2 con el primero de f2 para saber si son un grupo
#                 if dato2 < dato1:             #si el primer numero de f2 archivo es menor al primer numero de f1
#                     if dato_aux == dato1:      # que se cambie el dato que queremos escribir. si es dato1:
#                         dato_aux = dato2       # que cambie a dato2, porque es menor que dato1
#                         dato2 = dato3      # que avance al segundo dato de f2 para comparar con dato1 (de f1)
#                         dato3 = f2.readline()
#                     else:
#                         dato_aux = dato1      #si el primer numero de f1 es menor que el primero de f2, que se escriba
                        
#             f.write(dato_aux)
        
        
if __name__ == '__main__':
    datos = dividir_archivo("./datos.txt","./f1.txt","./f2.txt")
    print(datos)
    
    
