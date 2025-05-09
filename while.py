# # promedio
# cant=int=(input("ingrese la cantidad de notas"))
# suma=0
# for i in range(cant):
#     print("ingrese una nota")
#     nota=float(input())
#     suma+=nota

# prom=suma/cant
# print("el promedio es", prom)
sueldo=0
bono=0
goles=int(input("cuantos goles hizo su jugador?, (desde 1 hasta 10)"))
if goles>=1 and goles<=3:
    bono=4
elif goles>=4 and goles<=6:
    bono=6
elif goles>=7:
    bono=8

if goles>=1 and goles<=3:
    sueldo=1000
elif goles>=4 and goles<=6:
    sueldo=2000
elif goles>=7:
    sueldo=3000