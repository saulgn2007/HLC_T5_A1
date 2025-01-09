base = int (input("Ingrese la base del triángulo: "))
altura = int (input("Ingrese la aultura del triángulo: "))
precio = int (input("Ingrese el precio del metro cuadrado: "))

area = ((base*altura)/2)

precioTotal = (area*precio)

print("Area= ", area , "metros cuadrados. " , "Costo total= " , precioTotal , "unidades")