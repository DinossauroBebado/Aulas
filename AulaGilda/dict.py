'''artistas = ["justin bieber", "michael jackson", "katy perry"]

musicas = [12, 6776, 57]'''

#print(musicas[artistas.index("justin bieber")])


artistas_premiados = {"justin bieber": [12, "candense"],
                      "michael jackson": 6776,
                      "katy perry": 57}

print(artistas_premiados["justin bieber"])

print(artistas_premiados.items())

for art, premios in artistas_premiados.items():
    if art == "justin bieber":
        print(("{} tem {} musicas").format(art, premios[0]))
    else:
        print(("{} tem {} musicas").format(art, premios))

musicas_rank = {1: 'sorry', 2: 'baby', 3: 'never say never'}

rank = list(musicas_rank.keys())

mus = list(musicas_rank.values())

pos = mus.index("baby")


print(musicas_rank[rank[pos]])
print(rank[pos])
