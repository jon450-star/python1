def run():
    my_list=[1, "HELLO", True , 4.5]
    my_ditcionart = {"Firstname": "Facundo", "lastname": "Garcia"}

    super_list= [
        {"Firstname": "Carlos", "lastname": "Gomez"},
        {"Firstname": "Jonathan", "lastname": "Perez"},
        {"Firstname": "Javier", "lastname": "Montalco"},
        {"Firstname": "Diana", "lastname": "Rojas"},
        {"Firstname": "Facundo", "lastname": "Garcia"},  
    ]

    super_dic= {
        "naturales" : ["1","2","3","4","5","6","7","8"],
        "num_enteros": [-1,-2,1,2,3,4,0],
        "floating_numb" : [4.5,3.5,8.4,2.65]

    }


    for key, value in super_dic.items():
        print(key, ":", value)
    




if __name__=='__main__':
    run()