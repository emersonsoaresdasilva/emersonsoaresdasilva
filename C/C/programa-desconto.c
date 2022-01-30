// Programa 10% de desconto.

//Incluindo a biblioteca.
#include<locale.h>

//Inicio do Programa.
main () {
    //Números de ponto flutuante.
    float valor,valorf;
    //Selecionando a linguagem.
    setlocale(LC_ALL,"Portuguese");
    printf("Digite o valor do produto: \n");
    scanf("%f", &valor);
    valorf=(valor-(valor*0.1));
    printf("Valor do produto: \tR$ %.2f\n", valor);
    printf("Valor do produto com desconto: \tR$ %.2f\n\n", valorf);
}