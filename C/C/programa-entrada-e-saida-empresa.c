//Incluir o programa na biblioteca.
#include<locale.h>

//Inicio do programa.
main(){
    //Declarando as vari�veis.
    int horaentrada,horasaida;
    //Selecionando a linguagem.
    setlocale(LC_ALL,"Portuguese");
    
    //Imprimir na tela e pular 02 linhas.
    printf("Programa hor�rio - Entrada e Sa�da.\n\n");
    
    //Solicitando um hor�rio para o usu�rio.
    printf("Digite o hor�rio de entrada: "); 
    
    //Liberar o teclado para o usu�rio digitar a hora.
    scanf("%i",&horaentrada);
    
    //Se o hor�rio de entrada for maior ou igual a 17.
    if(horaentrada<=17){
       //Conta de turno hora mais 06 trabalhadas.
       horasaida=horaentrada+6;
       //Exbir o hor�rio de sa�da na tela.
       printf("O hor�rio de sa�da ser� �s %i:00 horas\.n",horasaida);
	}
	else{
		//Conta com % � a divis�o inteira que retorna o que sobra da conta.
		horasaida=(horaentrada+6)%6;
		printf("A hora de sa�da ser� %i horas\n",horasaida);
	}
//Fim do programa
}