from array import array

def OlderOrYounger(age):
    if age>=18:
        return True
    else:
        return False


def Corrector():
    ages=[18,32,16,43,8,82,2,4]
    array_booleanos_checking=[True,True,False,True,False,True,False,False]
    array_booleanos=[]
    for i in ages:
        result=OlderOrYounger(i)
    if(array_booleanos_checking==array_booleanos):
        print("TEST OK")
    else:
        print("TEST NOT OK")


Corrector()