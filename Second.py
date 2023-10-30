import random

min1=int(input("Dame el numero minimo del ratio de aleatorios entre 0 y 50 \n que debe debe ser mayor que 0 y menor que 50 : "))    
max1=int(input(f"Dame el numero maximo del ratio de aleatorios entre {min1} y 500\n que debe ser mayor que el primer número y menor que 500: "))
a=random.randint(min1,max1)
print(a)
intentos = 10

userDato=int(input("Adivina el numero: "))
while userDato != a or intentos!=0:
    intentos=-1
    userDato=int(input(f"ERROR tienes {intentos} restantes,Adivina el numero"))

print(f"Has hacertado tu numero era{userDato} y el aleatorio entre {max1} y {min1} era {a}")