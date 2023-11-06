#Suspès, Aprovat, Bé, Notable, Excel·lent
def Grades(grade):
    if grade<=4:
        grade="Suspès"
    elif (grade>=5) and (grade<6):
        grade="Aprovat"
    elif (grade>=6) and (grade<7):
        grade="Bé"
    elif (grade>=7) and (grade<9):
        grade="Excel·lent"

    return grade


def Corrector():
    array_result=[]
    array_grades=[2,3,4,10,8,5,1,7,6]
    array_correction=["Suspès","Suspès","Suspès","Excel·lent","Notable","Aprovat","Suspès","Notable","Bé"]

    for i in range(0,len(array_grades)):
        resultat=Grades(array_grades[i])
        array_result.append(resultat)

    if(array_result==array_correction):
        print("TEST OK")
    else:
        print("TEST NOT OK")


Corrector()