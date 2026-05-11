# def pd_mochila(c,w,n,W):
#     z = [[0]*W]*n
#     for i in range(1,n):
#         for d in range(1,W):
#             z[i][d] = z[i-1][d]
#             if w[i] <= d and z[i-1][d-w[i]] + c[i] > z[i][d]:
#                 z[i][d] = z[i-1][d-w[i]] + c[i]

#     return z[n][W]

# def r(num:int, U:int, notas:list)->tuple:
#     total = 0
#     min_num = 0
#     idx = num - 1
#     while ((total < U) and (idx >= 0)):
#         if notas[idx] > U:  # Se a nota é maior que o valor total não deve ser usada
#             idx -= 1
#         else:   # C.C adiciona aquela nota ao total e acrescenta a quantidade de notas usadas
#             total += notas[idx]
#             min_num += 1

#     if total == 0:
#         total = -1

#     return total, min_num

valor = int(input())
num_notas = int(input())
notas = list(map(int,input().split()))
notas.sort()



# O valor pago U pode ser um pouco maior que V. 
# O limite máximo necessário é V + max(notas)
limite_busca = valor + 2001 

# Inicializa a tabela DP com infinito
# dp[i] guardará o número mínimo de notas para o valor i
float_inf = float('inf')
dp = [float_inf] * (limite_busca + 1)
dp[0] = 0 # Para o valor 0 inicializa com 0 notas

# Programação Dinâmica Bottom-Up 
for nota in notas:
    for i in range(nota, limite_busca + 1):
        if dp[i - nota] + 1 < dp[i]:
            dp[i] = dp[i - nota] + 1

# Busca o primeiro valor U >= V que seja possível pagar (dp[U] < inf)
for u in range(valor, limite_busca + 1):
    if dp[u] != float_inf:
        print(f"{u} {dp[u]}")
        break




# while True:
#     total,minimo = r(num_notas, valor, notas)
#     if total == -1:
#         valor += 1
#         continue
#     else:
#         print(total, minimo)
#         break