# include <stdio.h>

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
void le(Node *raiz){
    int peso;
    char flag;


    scanf("%d %c", &peso, &flag);
    raiz = criaNo(peso);

    // Esquerda
    scanf(" "); // Ignora espaço pós flag
    if (flag == 'T'){
        le(raiz->esq);   // Chama recursivamente
    }

    // Direita
    scanf("%c ", &flag); // Ignora espaço pós Flag
    if (flag == 'T'){
        le(raiz->dir);   // Chama recursivamente
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

int acha_maior_peso(Node *raiz, int maior_total, int maior_lado){
    int aux_total = maior_total;
    int aux_lado = maior_lado;
    
    if (raiz->esq){ // Esquerda não nula
        maior_lado = acha_maior_peso(raiz->esq, aux_total, aux_lado); 
        if (maior_lado > 0){
            maior_total += maior_lado;
        }
    }
    
    int aux_esq = maior_total;
    
    if (raiz->dir){ // Direita não nula
        maior_lado = acha_maior_peso(raiz->dir, maior_total, maior_lado);
        if (maior_lado > 0){
            maior_total += maior_lado;
        }
    }
    
    // if (aux_esq + aux_inicio > maior_total){
    //     maior_total = aux;
    // }    

    maior_total += raiz->peso;
    return maior_total; 
}

int main(){ 
    char *sequencia;
    Node *raiz = NULL;
    int maior_peso;

    le(raiz);    

    maior_peso = acha_maior_peso(raiz, 0, 0);    
    maior_peso = (maior_peso >= 0) ? maior_peso : 0;    // Se for negativo o caminho é vazio e vai pra 0 o peso máximo
    printf("%d", maior_peso);

    libera(raiz);

    return 0;
}