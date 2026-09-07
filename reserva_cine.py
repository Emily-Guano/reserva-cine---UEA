# Reserva de Cine - UEA
# Estudiante: Emily Guano
# Objetivo: Sistema de reserva 3 filas x 4 columnas

# 1. Crear sala 3x4 con ceros (0 = libre, 1 = reservado)
asientos = [[0 for _ in range(4)] for _ in range(3)]

print("Sala inicial (0=libre, 1=reservado):")
for fila in asientos:
    print(fila)

# 2. Solicitar fila y columna
fila = int(input("\nIngrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# 3. Validar y registrar reserva
if 0 <= fila < 3 and 0 <= columna < 4:
    if asientos[fila][columna] == 0:
        asientos[fila][columna] = 1
        print(f"\nAsiento [{fila}][{columna}] reservado con éxito!")
    else:
        print("\n¡Ese asiento ya estaba reservado!")
else:
    print("\nError: Fila o columna fuera de rango.")

# 4. Mostrar sala completa 3x4
print("\nEstado final de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
