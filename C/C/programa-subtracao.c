// Programa de subtra��o.

//Incluindo a biblioteca.
#include<locale.h>

//Inicio do Programa.
main () {
    //N�meros de ponto flutuante.
	float num1,num2,resultado;
	//Idioma do texto.
	setlocale(LC_ALL,"Portuguese");
	//Imprimir na tela.
	printf("\nDigite o Primeiro n�mero: ");
	//Leitura dos dados.
	scanf("%f",&num1);
	//Imprimir na tela.	
	printf("Digite o Segundo n�mero: ");
	//Leitura dos dados.	
	scanf("%f",&num2);
	//Resultado = num1 - num2, resultando na substra��o.
	resultado=num1-num2;
	//Imprimir na tela.	
	printf("O resultado de %.2f - %.2f � igual � %.2f\n\n",num1,num2,resultado);
	//Comando de sistema (pause).
	system("pause");
}