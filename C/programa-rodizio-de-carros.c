//Abertura do programa.
main () {

//Declarando variáveis (int).
	int valor;
	printf("Digite o último numero da placa do veiculo:\n\n");
	scanf("%d", &valor);
	switch ( valor ){
		case 1 :
			printf("O dia do seu rodizio é Segunda-feira.\n");
			break;
			
		case 2 :
			printf("O dia do seu rodizio é Segunda-feira.\n");
			break;
			
		case 3 :
			printf("O dia do seu rodizio é Terça-feira.\n");
			break;
			
		case 4 :
			printf("O dia do seu rodizio é Terça-feira.\n");
			break;
			
		case 5 :
			printf("O dia do seu rodizio é Quarta-feira.\n");
			break;
			
      	case 6 :
			printf("O dia do seu rodizio é Quarta-feira.\n");
			break;
			
		case 7 :
			printf("O dia do seu rodizio é Quinta-feira.\n");
			break;
			
		case 8 :
			printf("O dia do seu rodizio é Quinta-feira.\n");
			break;
			
		case 9 :
			printf("O dia do seu rodizio é Sexta-feira.\n");
			break;
		
		case 0 :
			printf("O dia do seu rodizio é Sexta-feira.\n");
			break;
		
	    default :
	    	printf("Número invalido!\n");
	}
	getch();
}