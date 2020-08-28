//Abertura do programa.
main () {

//Declarando variáveis (int).
	int valor;
	printf("Digite um numero de 01 a 07.\n\n");
	scanf("%d", &valor);
	switch (valor){		
		case 1 :
			printf("Domingo.");
			break;
			
		case 2 :
			printf("Segunda-feira.\n");
			break;
			
		case 3 :
			printf("Terça-feira.\n");
			break;
			
		case 4 :
			printf("Quarta-feira.\n");
			break;
			
		case 5 :
			printf("Quinta-feira.\n");
			break;
			
		case 6 :
			printf("Sexta-feira.\n");
			break;
			
		case 7 :
			printf("Sabado.\n");
			break;
	
	    default :
	    	printf("Valor invalido!\n");
	}
	getch();
}