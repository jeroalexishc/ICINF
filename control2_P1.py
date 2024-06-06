


list=[] # de 15 dias 

for x in range(1,3):
    add=int(input("ingresar puntaje del alumno: "))
    list.append(add)
    

for x in list:
    if x >= 60:
        print(x,"dia", add, "tuvo un puntaje mayor a 60")
    elif x < 60:
        print(x,"dia", add, "tuvo un puntaje menor a 60")



