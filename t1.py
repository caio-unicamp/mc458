n,num_op = input().split()
n = int(n)
num_op = int(num_op)

# Inicializa os vetores com o tamanho N e todos os valores negativos

set_vec = [-1]*n
pos_vec = [-1]*n
qtd_inserida = 0

for i in range(num_op):
    comando = input().split()

    if comando[0] == 'l':   # Reinicializa S para vazio no comando l e consequentemente o vetor de posições e a quantidade de valores inseridos também
        qtd_inserida = 0
    else:
        instr = comando[0]
        elem = int(comando[-1])
        # Confere se o número está em S no comando de pertinência
        if instr == 'p' :
            # Se o índice x no vetor de posição armazena um número menor que a qtd de números no vetor set e se o valor nessa posição corresponde ao elemento pedido então ele pertence ao conjunto
            if pos_vec[elem] < qtd_inserida and  elem == set_vec[pos_vec[elem]]:
                print("1")
            else:   
                print("0")

        elif instr == 'i':
            if pos_vec[elem] < qtd_inserida and set_vec[pos_vec[elem]] == elem:  # Se o índice x já está ocupado por um número menor que a quantidade de valores inseridos e x está nesse índice do vetor set é porque x já está contido no conjunto S
                continue
            else:   # Caso contrário altera o valor no vetor S e no vetor de posições e por fim incrementa o valor de elementos inseridos no conjunto S para salvar na próxima iteração
                pos_vec[elem] = qtd_inserida
                set_vec[qtd_inserida] = elem
                qtd_inserida += 1

        elif instr == 'r':  # Aqui é basicamente o caminho contrário da instrução 'i', mudando apenas que não se deve remover sempre o último e sim o elemento requisitado e trazendo o último elemento para o lugar do elemento retirado
            if pos_vec[elem] >= qtd_inserida or set_vec[pos_vec[elem]] != elem:
                continue
            else:
                qtd_inserida -= 1
                set_vec[pos_vec[elem]] = set_vec[qtd_inserida]
                pos_vec[set_vec[qtd_inserida]] = pos_vec[elem]
