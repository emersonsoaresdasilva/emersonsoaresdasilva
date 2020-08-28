//Incluindo biblioteca local.
#include<locale.h>

//Abertura do programa.
main () {

//Selecionando a linguagem.
setlocale(LC_ALL,"Portuguese");

//Declarando as variáveis.
int num1,cont,resultado;

//Declarando variável de repetição / Respostas dado em letras.
char repetir;

//Laço de repetição.
do{
    //Comando de sistema para limpar a tela.
	//Solicitando um número para o usuário.
	printf("Digite um número: ");
	//Liberando o teclado para digitar.
	scanf("%i",&num1);
	//Laço de repetição da tabuada.
	for(cont=0;cont<=10;cont++){
	//Fazendo a conta da tabuada.
    resultado=num1*cont;
    //Mostrando a tabuada na tela.
    printf("\n%i X %i = %i", num1,cont,resultado);
}
    printf("\nDeseja repetir o programa?(S)Sim (N)Não\n");
    repetir=getch();
    //Condição da repetição.
}while(repetir=='s'||repetir=='S');
}