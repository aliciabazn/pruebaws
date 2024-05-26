#bloques de codigo que ejecutan una tarea específica cuando la llaman.
#ejemplos:
def demo(x):
    y = x + 3
    return y
print(demo(2))

def llorar(x):
    y = "Alicia ama a: " + x
    return y
print(llorar("Nala"))
print("------------")
print("------------")

a = 3
b = 2
c = 1

def demo():
    y =(a+b+c)
    return y
demo
#or
print(demo())
#or 
result = demo()
print(result)

print("------------")

#defines the value  of pi
pi = 3.14159
#calculates the area of a circle for a given radius
def calculate_radius_area(radius):
    return pi*radius**2
r = int(input("Enter the radius of a circle: "))
area =calculate_radius_area(r)
print(area)

print(llorar("Nala"))