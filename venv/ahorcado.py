import random
from functools import reduce
import os, sys
import time
#import threading
#from time import time


def read():
    palabras=[]
    with open("./archivos/data.txt", "r",encoding="utf-8") as f:
        for line in f:
            palabras.append(line)
    return palabras


def azar(x):
    ran=list(normalize(random.choice(x)))
    ran.pop(len(ran)-1)
    return(ran) 


def normalize(s):
    replacements=(
        ("á", "a"),
        ("é","e"),
        ("í","i"),
        ("ó","o"),
        ("ú","u"),
    )
    for a,b in replacements:
        s=s.replace(a,b)
    return s


def dibujo(i):
    if i==0:
        print("""""
         VAMOS BIEN, NO DEJES QUE ME AHORQUEN
            +---+
                !
                !
                !
                !
                !
                !
        ---------
        ---------""")
    elif i==1:
        print(""" 
        OH! OH! CUIDADO
            +---+
           /    !
                !
                !
                !
                !
                !
        ---------
        ---------
        
        """)
    elif i==2:
        print(""" 
        CONCENTRATE!!
            +---+
           /    !
          O     !
                !
                !
                !
                !                
        ---------
        ---------
        
        """)
    elif i==3:
        print("""
        NO TE EQUIVOQUES MAS POR FAVOR
            +---+
           /    !
          O     !
          |     !
                !
                !
                !
        ---------
        ---------
        
        """)
    elif i==4:
        print("""
        TENGO MIEDO
            +---+
           /    !
          O     !
         /|\    !
                !
                !
                !
        ---------
        ---------
        
        """)
    elif i==5:
        print("""
        NO ME QUIERO IR
            +---+
           /    !
          O     !
         /|\    !
         /      !
                !
                !
        ---------
        ---------
        
        """)
    elif i==6:
        print("""
        HASTA LA VISTA BABY
            +---+
           /    !
          o     !
         /|\    !
         / \    !
                !
                !
        ---------
        ---------
        
        """)
    elif i==7:
        print("""
        ESTOY VIVO

            \O/
             |
            / \ 
                
        """)
    elif i==8:
        print("""
        ADIOS
            +---+
           /    !
          o     !
         /|\    !
         / \    !
                !
                !
        ---------
        ---------
        
        """)


 
def run():
    os.system("clear")
    print("¡ADIVINA LA PALABRA!", "\n")
    word=azar(read())
    print(word)
    #print(len(word))
    new=["_ "]*(len(word))
    print(" ".join(new),"\n")
    error=0
    while error !=6 and new !=word:
        print("RECUERDA QUE SOLO TIENES 20 SEGUNDOS POR LETRA, APÚRATE","\n")

        inicio_time=time.time()
        letra=input("Ingresa una letra: ").lower()
        try:
            if letra.isalpha()==True and len(letra)==1:
            
                index=0
                valor=[]
                
                #errror=0
                
                for i in word:
                    if i==letra:
                        new[index]=letra
                        valor.append(0)
                    else:
                        valor.append(1)         
                    index+=1
                    os.system("clear")

                
                    

                valor_multiplicado=reduce(lambda a,b: a*b,valor)
                if valor_multiplicado==1:
                    error+=1
                    os.system("clear")
                print("PRUEBA OTRA VEZ")
                dibujo(error)
                                 
                print(" ".join(new),"\n")
               

            else:
                raise ValueError("Ingrese una letra, no otros valores")
            
        except ValueError as ve:
            print(ve)

        final_time=time.time()
        total_time=final_time-inicio_time
                
        if total_time>20:            
            os.system("clear")
            dibujo(8)
            print("SE TE ACABÓ EL TIEMPO","\U0001F62D") 
            sys.exit() 
        #print(total_time)

    if new==word:
        os.system("clear")
        dibujo(7)
        print("FELICIDADES, GANASTE Y GRACIAS A TI NO ME HAN AHORCADO", "\U0001F600"),"\n"
    else:
        os.system("clear")
        dibujo(8)
        print("PERDISTE, ME AHORCARON","\U0001F62D","\n")    


if __name__== "__main__":
    run()
