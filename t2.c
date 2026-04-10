# include <stdio.h>
# include <stdlib.h>

typedef struct node {
   int peso;
   struct node *esq;
   struct node *dir;
} Node;


Node* criaNo(int peso) {
   Node* novo = (Node*)malloc(sizeof(Node));
   novo->peso = peso;
   novo->esq = NULL;
   novo->dir = NULL;
   return novo;
}

/**
 * Lê uma sequência S = p flagE SE flagD SD em que
 * 
 * - p pertence a [-10^4, 10^4]
 * @param raiz
 */
void le(Node **raiz){
    int peso;
    char flag;

    if (scanf("%d", &peso) != 1){
        return;
    }
    *raiz = criaNo(peso);

    // Esquerda
    scanf(" %c", &flag);
    if (flag == 'T'){
        le(&((*raiz)->esq));   // Chama recursivamente
    }

    // Direita
    scanf(" %c", &flag); // Ignora espaço pós Flag
    if (flag == 'T'){
        le(&((*raiz)->dir));   // Chama recursivamente
    }
}

/**
 * Libera recursivamente cada nó da árvore
 * @param raiz
 */
void libera(Node *raiz){ 
    if (raiz){
        libera(raiz->esq);
        libera(raiz->dir);
        free(raiz);
    }
}

int acha_maior_peso(Node *raiz, int *maior_total){
    int esq = 0, dir = 0;   // Inicializa como 0 os pesos dos filhos antes de ir até eles
    
    if (raiz->esq){ // Esquerda não nula
        esq = acha_maior_peso(raiz->esq, maior_total);
        esq = (esq > 0) ? esq : 0;
    }
        
    if (raiz->dir){ // Direita não nula
        dir = acha_maior_peso(raiz->dir, maior_total);
        dir = (dir > 0) ? dir : 0;  // Só acrescenta se for positivo
    }
    
    
    int aux_total = raiz->peso + esq + dir;
    
    if (aux_total > *maior_total){
        *maior_total = aux_total;
    }    

    return raiz->peso + (esq > dir ? esq : dir);
}

int main(){ 
    Node *raiz = NULL;
    int maior_peso = 0;

    le(&raiz);    

    acha_maior_peso(raiz, &maior_peso);    
    maior_peso = (maior_peso >= 0) ? maior_peso : 0;    // Se for negativo o caminho é vazio e vai pra 0 o peso máximo
    printf("%d\n", maior_peso);

    libera(raiz);

    return 0;
}