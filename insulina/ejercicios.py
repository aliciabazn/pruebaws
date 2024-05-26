age = 7
if age > 18:
    print("adult")
else:
    print("child")
    
    
bananas=1
if bananas >= 5:
    print("I have a large bunch of bananas")
elif 2 < bananas <= 4:
    print("I have a small bunch of bananas")
else:
    print("I do not have enought bananas ")
    
#bucle while
counter = 0
while counter <= 3:
    print("I love potatoes")
    counter = counter + 1
    
dinero = 297
while dinero >= 295: #dinero es mayor o igual que 295
    print("tengo sufienciente dinero")
    dinero = dinero - 1
    
tiempo = 0
while tiempo <= 5:
    print("Es temprano")
    tiempo = tiempo + 1
    
    
misAmigosYCosas = ["Brenda", "Doriane", "Marcela", "Alejandro", "Alito", "Juan", 2024, 2023]
print(misAmigosYCosas)
print(misAmigosYCosas[0])
print(misAmigosYCosas[1])
    

# bucle for
for num in [1, 2, 3]:
    print(num)
    
for i in range(0,5):
    print(i)
#en un for, lo que va después del in deberá ser siempre un iterable. Objetos que puedan ser indexados/ iterables.
#Los iteradores son objetos que hacen referencia a un elemento, y que tienen un método next que permite hacer referencia al siguiente.
for i in "Python":
    print(i) 
from collections import Iterable
print(isinstance(tiempo, Iterable)) #False
print(isinstance(misAmigosYCosas, Iterable)) #True


it = iter(misAmigosYCosas)
print(it) #es un iterador
print(next(it))
print(next(it))
print(next(it))


#anidar for útil si queremos iterar algún objeto que en cada elemento, tiene a su vez otra clase iterable. 
lista = [[56, 1],
         [12, 5],
         [9, 4]]

for i in lista:
    print(i)
    
for i in lista:
    for x in i:
        print(x)
        
texto = "Amorosa"
for s in texto[::-1]:
    print(s)
    
#diccionario
DicAlicia = {
    "Edad": "28",
    "Nombre": "Alicia",
    "Documento": "Y9761699D"
    
} 
print(DicAlicia)

d2 = dict({
    "Edad": "28",
    "Nombre": "Alicia",
    "Documento": "Y9761699D"})
print(d2)

#acceder y modificar algun elemento:
print(d2["Edad"]) #28
print(d2["Nombre"])
print(d2["Documento"]) 

print("------------")

d2["Edad"] = "25"

print(d2)
print(d2["Edad"])
print("------------")
#itinerar un diccionario
#asi imprimimos clave
for x in d2:
    print(x)
print("------------")

#asi imprimimos clave
for x in d2:
    print(d2[x])
    
print("------------")

#O si queremos imprimir el key y el value a la vez.
for clave, valor in d2.items():
    print(clave, valor)
    
    
#input
#input("Cual es tu nombre?: ")


age = 100
if age > 18:
        print('Adult')
elif age > 65:
        print('Senior Citizen')
else:
        print('Child')