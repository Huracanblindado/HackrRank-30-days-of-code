import sys

n = int(sys.stdin.readline().strip())
agenda = {}

for _ in range(n):
    linea = sys.stdin.readline().strip().split()
    agenda[linea[0]] = linea[1]

for linea in sys.stdin:
    nombre_buscado = linea.strip()
    if not nombre_buscado:
        continue
    if nombre_buscado in agenda:
        print(f"{nombre_buscado}={agenda[nombre_buscado]}")
    else:
        print("Not found")