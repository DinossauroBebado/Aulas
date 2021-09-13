

def checa3(macacos):
    if 3 in macacos:
        print(3)
    else:
        print("nao tem tres ")


def mais4(numeros):
    n = []
    for number in numeros:
        n.append(number + 4)

    return n


numeros = [1, 2, 3, 4, 5, 6, 7]

numero = [1, 2, 7, 4, 5, 8, 7]


checa3(numeros)


numeros_mais_4 = mais4(numeros)

print(numeros_mais_4)


def Animais(animal):
    print("{} é um animal".format(animal))


Animais("macaco")
Animais("Laio")
Animais("Unicornio")

print("macaco"+"banana")
