from os import replace
import random
from functools import reduce
import os, sys
import time

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def read():   
    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        words = [i.replace('\n','') for i in f]
        
        words2 = list (normalize(random.choice(words)))
        print(words2)
        
        words2.pop(len(words2)-1)
        #ran.pop(len(ran)-1)
        print(words2)
        #print(words2)
        
        #words4= len(words2)
        #print(words4)
        
        words5= ["_ "]*(len(words2))
        print(words5)
        print(" ".join(words5),"\n")
        
    index=0
    Valor=[]
    letra= input("ingresa una letra: ").lower()
    words5[index] = letra
    Valor.append(0)
    print(Valor)  
    if letra.isalpha()==True and len(letra)==1:
        print(letra)
    else:
        print("no es letra")
    
    

def juego1():   
    pass
    




def run():
    read()






if __name__=='__main__':
    run()