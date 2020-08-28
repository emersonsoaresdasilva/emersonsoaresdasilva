//Incluindo biblioteca local.
#include<locale.h>

//Abertura do programa.
main () {

//Declarando variáveis (int,float).
int dias;
float anos;

//Selecionando a linguagem.
setlocale(LC_ALL,"Portuguese");

//Imprimindo na tela.
printf ("Entre com o número de dias: ");

//Obtendo os dados do usuário.
scanf ("%i",&dias);

//Convertendo dias em anos.
anos=(dias/365.25);

//Imprimindo na tela.
printf ("\n\n%d dias equivalem a %f anos.\n",dias,anos);

//Comando do sistema (pause).
system("pause");

//Fim do programa.
}