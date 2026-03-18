from os import system
system("cls")

while True:
    
    system("cls")
    n1=int(input("Ingrese un número:"))
    n2=int(input("Ingrese otro número:"))
    
    print("1. Sumar")
    print("2. Multiplicar")
    print("0. Salir")
    op=input("Ingrese una opción:")
    if op=="1":
        
        resultado=sumar(n1,n2)
        print("La suma es: ", resultado)
        
    if op=="2":
        resultado=multiplicar(n1,n2)
        print("La multiplición es: ", resultado)
        
    if op=="0":
        break 