def potencia(num, exp):
    # Exponente 0
    if exp == 0:
        return 1
    # Exponente 1
    elif exp == 1:
        return num
    # Exponentes positivos
    elif exp > 1:
        return num * potencia(num, exp - 1)
    # Exponentes negativos
    else:
        return 1 / potencia(num, -exp)

while True:
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es igual a {resultado}")