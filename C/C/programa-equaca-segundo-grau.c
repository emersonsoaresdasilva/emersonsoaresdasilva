//Incluindo biblioteca local.
#include<locale.h>

//Programa inicial.
main(){
    
//Selecionando a linguagem.
setlocale(LC_ALL,"Portuguese");
      //Declarando variáveis do tipo inteiro(int).
      int escolha;
      //Tipo racional - Números racionas que tem casas depois da virgula.
      float a,b,c,x1,x2,delta,yv,xv;
      //Tipo letras.
      char resp;
      //Inicio do laço de repetição (for, do, while).
      do{
          printf("Digite a opção desejada: \n");
          printf("01 - Programa de Equação do 2º grau.\n");
          printf("02 - Sobre.\n");
          //Liberando o teclado para digitar.
          scanf("%i",&escolha);
          //Escolha uma das opções.
          switch(escolha){
            //Caso ele digite 01, iniciar o programa.
          	case 01:
          		printf("Programa que resolve uma equação de 2º grau:\n");
          		printf("ax² + bx + c = 0\n");
          		printf("Digite o valor de a: ");
          		scanf("%f",&a);
          		//Enquanto "a" for 0 ele irar ficar repetindo.
          		while(a==0){
          			printf("Com o (a) = 0 não há uma equação do 2º grau.\n\n");
					printf("Digite outro número: ");
					scanf("%f",&a);
			      	}
					printf("Digite o valor de b: ");
					scanf("%f",&b);
					printf("Digite o valor de c: ");
					scanf("%f",&c);
					delta=pow(b,2)-4*a*c;
					xv=-b/(2*a);
					yv=-delta/(4*a);
					printf("A cordenadora cartesiana do vértice da parábola é (%.2f e %.2f).\n",xv,yv);
					printf("delta = %.2f \n",delta);
					if (delta<0){
						printf("Com delta negativo não há raízes no conjunto dos reais. \n");
					}
					else
					if(delta==0){
						printf("Com delta zerado só há uma raíz que é %.2f \n",-b/(2*a));
						}
					//Corresponde ao delta > 0.
					else
					{
					x1=(-b-sqrt(delta))/(2*a);
					x2=(-b+sqrt(delta))/(2*a);
					printf("Com delta positivo temos duas raízes:%.2f para x1 e %.2f para x2 \n",x1,x2);
					}
					break;
					case 02:
						printf("Desenvolvido por Emerson Soares.");
					break;
					default:
						        printf("\n\nPrograma inválido!\n\n");
				}
				printf("\nDeseja repetir o programa? (S)Sim (N)Não.\n");
				resp=getch();
			}while(resp=='s'||resp=='S');
	}