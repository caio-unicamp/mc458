n,num_op = input().split()
n = int(n)
num_op = int(num_op)

s = set()

for i in range(num_op):
    comando = input().split()

    if comando[0] == 'l':   # Reinicializa S para vazio no comando l
        s = set()
    else:
        instr = comando[0]
        elem = int(comando[-1])
        # Confere se o número está em S no comando de pertinência
        if instr == 'p' :
            if elem in s:
                print("1")
                continue
            else:
                print("0")
                continue

        elif instr == 'i':
            s.add(elem)

        elif instr == 'r':
            s.discard(elem)
            

