//Incluindo biblioteca local.
#include<locale.h>

//Abertura do programa.
main () {

//Selecionando a linguagem.
setlocale(LC_ALL,"Portuguese");

//Declarando as vari�veis.
int num1,cont,resultado;

//Declarando vari�vel de repeti��o / Respostas dado em letras.
char repetir;

//La�o de repeti��o.
do{
    //Comando de sistema para limpar a tela.
	//Solicitando um n�mero para o usu�rio.
	printf("Digite um n�mero: ");
	//Liberando o teclado para digitar.
	scanf("%i",&num1);
	//La�o de repeti��o da tabuada.
	for(cont=0;cont<=10;cont++){
	//Fazendo a conta da tabuada.
    resultado=num1*cont;
    //Mostrando a tabuada na tela.
    printf("\n%i X %i = %i", num1,cont,resultado);
}
    printf("\nDeseja repetir o programa?(S)Sim (N)N�o\n");
    repetir=getch();
    //Condi��o da repeti��o.
}while(repetir=='s'||repetir=='S');
}