personas = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]

magos = []
cientificos = []
otros = []

for nombre in personas:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)


def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]


def imprimir_nombres(personas):
    for nombre in personas:
        print(nombre)


print("Lista completa:")
imprimir_nombres(personas)

print(" "*30)


hacer_grandioso(magos)


print("Magos grandiosos:")
imprimir_nombres(magos)
print(" "*30)


print("Cientificos:")
imprimir_nombres(cientificos)

print(" "*30)

print("Otros:")
imprimir_nombres(otros)

