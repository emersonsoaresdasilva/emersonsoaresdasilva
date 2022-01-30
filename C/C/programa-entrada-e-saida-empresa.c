//Incluir o programa na biblioteca.
#include<locale.h>

//Inicio do programa.
main(){
    //Declarando as variáveis.
    int horaentrada,horasaida;
    //Selecionando a linguagem.
    setlocale(LC_ALL,"Portuguese");
    
    //Imprimir na tela e pular 02 linhas.
    printf("Programa horário - Entrada e Saída.\n\n");
    
    //Solicitando um horário para o usuário.
    printf("Digite o horário de entrada: "); 
    
    //Liberar o teclado para o usuário digitar a hora.
    scanf("%i",&horaentrada);
    
    //Se o horário de entrada for maior ou igual a 17.
    if(horaentrada<=17){
       //Conta de turno hora mais 06 trabalhadas.
       horasaida=horaentrada+6;
       //Exbir o horário de saída na tela.
       printf("O horário de saída será às %i:00 horas\.n",horasaida);
	}
	else{
		//Conta com % é a divisão inteira que retorna o que sobra da conta.
		horasaida=(horaentrada+6)%6;
		printf("A hora de saída será %i horas\n",horasaida);
	}
//Fim do programa
}