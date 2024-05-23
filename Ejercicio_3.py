n=int(input("ingrese la cantidad de alturas a promediar: "))
p=0
h=0 # h es una variable auxiliar, si el bucle se rompe antes de llegar a n, la ejecucion pasara por esta variable y dividira la suma de alturas por esta cantidad
suma=0

while p < n:

    q=float(input("ingrese altura: "))
    if q == 0:
        break
    suma+=q
    h+=1
    p+=1

    if n == h :
        prom=suma/n
    else:
        prom=suma/h

print("La altura promedio de las alturas es: ",prom)