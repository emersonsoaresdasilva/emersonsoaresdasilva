//Incluindo biblioteca local.
#include<locale.h>

//Abertura do programa.
main () {

//Declarando variáveis (int).
int valor1,valor2,valor3,resultado;

//Selecionando o idioma.
setlocale(LC_ALL,"Portuguese");

printf("Digite o valor do produto:\n\n");
scanf("%i",&valor1);
printf("Digite o valor do segundo produto:\n\n");
scanf("%i",&valor2);

resultado=valor1/valor2*valor3;
    if(valor1>valor2&&valor1>valor3);
    else if(valor2>valor1&&valor2>valor3);
    else if(valor3>valor1&&valor3>valor2);
    else{
	    printf("Os produtos tem o mesmo valor!\n\n");
}
}