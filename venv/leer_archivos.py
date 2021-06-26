def read():
    numbers = []
    with open("./archivos/numbers2.txt","r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["KATIA","Carlos" , "Javier", "Eduardo","Rodrigo", "Rocío"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as h:
        for i in names:
            h.write(i)
            h.write("\n")


def run():
    write()
    read()

if __name__ == '__main__':
    run()


