valor = int(input())
num_notas = int(input())
notas = list(map(int,input().split()))
notas.sort()

# O valor pago U pode ser um pouco maior que V. 
# O limite máximo necessário é V + max(notas)
limite_busca = valor + 2001 

# Inicializa a tabela rn com infinito
# rn[i] guardará o número mínimo de notas para o valor i
float_inf = float('inf')
rn = [float_inf] * (limite_busca + 1)
rn[0] = 0 # Para o valor 0 inicializa com 0 notas

# Programação Dinâmica Bottom-Up 
for nota in notas:
    for i in range(nota, limite_busca + 1):
        if rn[i - nota] + 1 < rn[i]:
            rn[i] = rn[i - nota] + 1

# Busca o primeiro valor U >= V que seja possível pagar (rn[U](r(n,U)) < inf)
for u in range(valor, limite_busca + 1):
    if rn[u] != float_inf:
        print(f"{u} {rn[u]}")
        break
