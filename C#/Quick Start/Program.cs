using System;

public class Program
{
	public static void Main()
	{
		Console.WriteLine(" ------------------------------------------------");
		Console.WriteLine("|                                                |");
		Console.WriteLine("| Seja bem-vindo ao meu primeiro programa em C#. |");
		Console.WriteLine("|                                                |");
		Console.WriteLine(" ------------------------------------------------");
		string username = null;
		string password = null;

		DateTime timeUtc = DateTime.UtcNow;
		TimeZoneInfo kstZone = TimeZoneInfo.FindSystemTimeZoneById("E. South America Standard Time");
		DateTime dateTimeBrasilia = TimeZoneInfo.ConvertTimeFromUtc(timeUtc, kstZone);

		do
		{
			Console.Write("\nDigite o seu usuário: ");
			username = Console.ReadLine();
			Console.Write("Digite a sua senha: ");
			password = Console.ReadLine();

			if (username != "Emerson" || password != "!is@C#")
				Console.Clear();
				Console.WriteLine("\nUsuário ou senha incorretos, tente novamente!");
		}
		while (username != "Emerson" || password != "!is@C#");
			Console.Clear();
			Console.WriteLine("\nLogin efetuado com sucesso!");
			Console.WriteLine("\nAcessado em: " + dateTimeBrasilia.ToString("dd/MM/yyyy HH:mm:ss"));
			Console.ReadKey();
	}
}

