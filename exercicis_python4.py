from array import array

def OddEven(number):
    if number %2==0 :
        return True
    else:
        return False
    return


def Corrector():
    array_numbers=[22,33,44,50,100,55,74,73,2]
    array_result=[True,False,True,True,True,False,True,False,True]
    array_result_student=[]
    for number in array_numbers:
        array_result_student.append(OddEven(number))

    if(array_result==array_result_student):
        print("TEST OK")
    else:
        print("TEST NOT OKAY")


Corrector()