

casas = ["Miranha", "doente verde", "Venoninho"]

print(casas[2])

casa_cor = {"Miranha": ["vermelho", "azul", "branco"],
            "doente verde": "verde",
            "venoninho": "preto"}

print(casa_cor["Miranha"])

print(casa_cor.items())

for nome, cor in casa_cor.items():
    print(nome)
    print(cor)
