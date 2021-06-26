from functools import reduce


def run():
    
    palindrome = lambda string: string == string [::-1]
    print(palindrome('ana'))

    my_list = [1,2,3,4,5,6,13,18,21,24,26]
    odd = [i for i in my_list if i%2 !=0]
    print (odd)

    odd2 = list(filter(lambda x : x%2 !=0 , my_list))
    print (odd2)
#---------------------------------------------------

    my_list2 = [1,2,3,4,5]
    odd3 = [i**2 for i in my_list2]
    print(odd3)

    odd4 = list(map(lambda x : x**2, my_list2))
    print(odd4)

#-----------------------------------------------------

    my_list3 = [2,5,10,4,20]
    longitud = len(my_list3)
    numero = 2**longitud
    print(numero)

    
    my_list4 = [2,5,10,4,20]

    all_multiplied = reduce(lambda a,b: a+b, my_list4)

    print(all_multiplied)


if __name__ == "__main__":
    run()
