"""
print("Ingrese el primer numero");
numero1 = int(input())
print("Ingrese el segundo numero")
numero2 = int(input())
suma= numero1+numero2
print("El resultado de la suma es: ",suma)
resta=numero1=numero2
print("El resultado de la resta es: ",resta)
multiplicacion = numero1 * numero2
print("El resultado de la multiplicacion es: ",multiplicacion)
division = numero1 / numero2
print("El resultado de la division es: ",division)

"""

#condicionales
"""
numero1 = int(input("Ingrese el primer numero"))
numero2 = int(input("Ingrese el segundo numero"))
if numero2==0:
    print("La division por cero no es posible")
else:
    division=numero1/numero2
    print("La division es ",division)
"""

"""
nombre=input("Ingrese su nombre ")
edad = int(input("Ingrese su edad"))
if edad >= 110:
    print("Hola ",nombre,"Usted ha ingresado una edad rara ")
elif edad >= 60:
    print("Hola",nombre,"Usted es un adulto mayor ")
elif edad>= 18:
    print("Hola",nombre,"usted es un adulto ")
else:
    print("Hola ",nombre,"Usted es menor de edad")
#condicionales anidados  
"""

#comparador logico and se tiene que cumplir los dos 
"""
user = input ("Ingrese su usuario ")
password = int(input("Ingrese el password"))
if user == "lili" and password == 123:
    print("Bienvenido")
else:
    print("usuario o contraseña incorrecta")

"""
# comparador or compara que almenos 1 cumpla con la condicion 
"""
user = input ("Ingrese su usuario ")
telefono = int(input("Ingrese el telefono"))
if user == "lili" and telefono == 123:
    print("Bienvenido")
else:
    print("usuario o telefono incorrecta")
"""
#Ciclo for contar siempre y cuando donde empezamos y donde terminamos 
for i in range(1,5,1):
    if i % 2 == 0:
        print(i)










