conjuntos = int(input())

def ordena(dados: list, num_s: int) -> list:
    """
    Função para ordenar o cojunto de dados de forma a deixar em ordem crescente de inversões existentes em cada fita de DNA e nao alterando a ordem em caso de empate
    """
    for i in range(num_s):
        for j in range(num_s - 1, i, -1):
            if dados[i][1] > dados[j][1]:
                aux = dados[i]
                dados[i] = dados[j]
                dados[j] = aux

    return dados

for i in range (conjuntos): # Leitura de todo o conjunto de dados
    input() # Ignora pulo de linha
    tam, num_s = list(map(int,input().split()))
    dados = []
    for _ in range(num_s):
        dna = input()   # Lista de tuplas em um conjunto de dados que armazena (Fita de DNA, Número de inversões)
        inversoes = 0
        for j in range(tam):
            for k in range(tam - 1, j, -1):
                if dna[j] > dna[k]:
                    inversoes += 1
        dados.append((dna, inversoes))
    dados_ordenados = ordena(dados=dados, num_s=num_s)

    for j in dados_ordenados:
        print(j[0])

    if conjuntos == 1:
        continue
    else:
        print()
    
