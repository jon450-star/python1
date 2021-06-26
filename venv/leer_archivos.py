def read():
    numbers = []
    with open("./archivos/numbers2.txt","R") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    pass


def run():
    read()

if __name__ == "__main__":
    run()