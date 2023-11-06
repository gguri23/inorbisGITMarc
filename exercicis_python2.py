def Sum_hundred_first_numbers():
    summation=0
    for i in range(0,101):
        summation=summation+1
    return summation


def Corrector():
    result=Sum_hundred_first_numbers()
    if(result==5050):
        print("TEST OK")
    else:
        print("TEST NOT OK")


Corrector()