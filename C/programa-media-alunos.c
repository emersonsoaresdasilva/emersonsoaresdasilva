int main (void)
{
	float nota1=0,nota2=0,media=0;
	int resp;
	do
	{
	printf("Digite a primeira nota: ");
	scanf("%f",&nota1);
	printf("Digite a segunda nota: ");
	scanf("%f",&nota2);
	media=(nota1+nota2)/2;
	printf("Média do aluno = %f\n",media);
	printf("Digite 01 para continuar ou 02 para sair.\n");
	scanf("%d",&resp);
	}while (resp==01);
}