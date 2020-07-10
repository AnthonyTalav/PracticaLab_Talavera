#Autor: Anthony Talavera Carranza

def esPrimo(numero):
    if(numero%2==0):
        print("El número "+str(numero)+" es primo")
    else:
        print("El número "+str(numero)+" no es primo")


numero=int(input("Ingrese el número para ver si es primo o no ☺: "))

esPrimo(numero)

    