







def run():
 print("¡Adivina la palabra!")
 numb = []
 with open("./archivos/data.txt","r",encoding="utf-8")as f:
     for line in f:
         numb(line)
         print(numb)



if __name__=='__main__':
    run()