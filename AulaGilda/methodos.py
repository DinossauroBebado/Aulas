artistas = ["justin bieber", "michael jackson", "katy perry"]

adj = ["ruim", 'BOM', "mediado"]

print(
    (artistas[0]).upper()
)

print(adj[1].lower())

for artista in artistas:
    if artista.find("k") >= 0:
        print(artista)

primeiro_nome_artista = []

for artista in artistas:
    primeiro_nome_artista.append(artista[0:artista.find(" ")])

print(primeiro_nome_artista)

print(artistas[1:2])

print(artistas[0].rstrip()+"oi")

numeros = [4, 65, 4, 4, 32, 3, 32, 5, 23]

org = numeros.sort()

print(org)
print("justin bieber" in artistas)
