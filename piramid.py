bloques = int(input("ingrese la cantidad de bloques:"))
fila = 1
utilizado = 0

while True:
    utilizado += fila
    if utilizado > bloques:
        break
    fila += 1

print("la altura de la piramide es:", fila)
