list=[] #cantida de caracteres

while True:
    add=input("ingrese una palabra: ")
    if add=="":
        break
    list.append(add)

for x in list:
    char=0
    for i in x:
        if i in x:
            char+=1
    print(x,"la cantidad de caracteres que tiene la palabra es: ", char)


