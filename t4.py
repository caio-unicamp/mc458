def r(num:int, U:int, notas:list)->tuple:
    total = 0
    min_num = 0
    idx = num - 1
    while ((total < U) and (idx >= 0)):
        if notas[idx] > U:  # Se a nota é maior que o valor total não deve ser usada
            idx -= 1
        else:   # C.C adiciona aquela nota ao total e acrescenta a quantidade de notas usadas
            total += notas[idx]
            min_num += 1

    if total == 0:
        total = -1

    return total, min_num

valor = int(input())
num_notas = int(input())
notas = list(map(int,input().split()))
notas.sort()


while True:
    total,minimo = r(num_notas, valor, notas)
    if total == -1:
        valor += 1
        continue
    else:
        print(total, minimo)
        break