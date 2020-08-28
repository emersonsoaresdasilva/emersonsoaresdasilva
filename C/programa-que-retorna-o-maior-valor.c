//Incluindo biblioteca local.
#include<locale.h>

//Abertura do programa.
main () {

//Declarando variáveis (int).
int valor1,valor2,valor3;

//O que o programa vai fazer?
printf("Retornando o maior valor.\n\n");

//Solicitar os números para o usuário.
printf("Digite o primeiro valor abaixo:\n\n");

//Liberar o teclado para que o usuário digite o valor.
scanf("%i",&valor1);

//Solicitar os números para o usuário.
printf("Digite o segundo valor:\n\n");

//Liberar o teclado para que o usuário digite o valor.
scanf("%i",&valor2);

//Solicitar os números para o usuário.
printf("Digite o ultimo valor.\n\n");

//Liberar o teclado para que o usuário digite o valor.
scanf("%i",&valor3);

//Comparar se o valor1 é maior do que o valor2 e o valor1 é maior do que o valor3.
if(valor1>valor2&&valor1>valor3){
	printf("O primeiro valor é maior.");
}
//Comparar se o valor2 é maior do que o valor1 e o valor2 é maior do que o valor3.
else if(valor2>valor1&&valor2>valor3){
	printf("O segundo valor é maior.");
}
//Comparar se o valor3 é maior do que o valor1 e o valor 3 é maior do que o valor2.
else if(valor3>valor1&&valor3>valor2){
	printf("O terceiro valor é maior.");
}
//Comparar se o valor1 é igual ao valor2.
else if(valor1==valor2)
printf("Valor 1 é igual ao valor 2.");

//Comparar se o valor1 é igual ao valor3.
else if (valor1==valor3)
printf("Valor 1 é igual ao valor 3.");

//Comparar se o valor2 é igual ao valor3.
else if(valor2==valor3)
printf("Valor 2 é igual ao valor 3.");

//Comparar se todos os valores são iguais.
else
	printf("Todos os valores são iguais");
}