deudores = {}

print("\n--- Datos de Deudores ---")
for i in range(2):
    rut = input("Ingrese el RUT del deudor " + str(i+1) + ": ")
    deuda = float(input("Ingrese la deuda de " + rut + ": "))
    deudores[rut] = deuda

print("\n--- Procesamiento de abonos ---")
while True:
    rut = input("Ingrese el RUT del deudor (o presione Enter para terminar): ")
    if rut == "":
        break
    
    if rut in deudores:
        abono = float(input("Ingrese el monto del abono para " + rut + ": "))
        deudores[rut] -= abono
        
        if deudores[rut] <= 0:
            del deudores[rut]
            print("La deuda de " + rut + " ha sido saldada. Se ha eliminado del registro.")
        else:
            print("Deuda restante de " + rut + ": " + str(deudores[rut]))
    else:
        print("RUT no encontrado en el registro de deudores.")

print("\nDeudores restantes:")
for rut, deuda in deudores.items():
    print("RUT: " + rut + ", Deuda: " + str(deuda))