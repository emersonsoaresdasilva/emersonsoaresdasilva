﻿using DocumentFormat.OpenXml.Office2010.ExcelAc;
using System;
using System.Net;
using System.Collections.Generic;
using System.Linq;
using System.Net.Sockets;

public class Program
{
	public static void Main()
	{
		Console.WriteLine(" ------------------------------------------------");
		Console.WriteLine("|                                                |");
		Console.WriteLine("| Seja bem-vindo ao meu primeiro programa em C#. |");
		Console.WriteLine("|                                                |");
		Console.WriteLine(" ------------------------------------------------");
        TimeZoneInfo kstZone = TimeZoneInfo.FindSystemTimeZoneById("E. South America Standard Time");
        DateTime timeUtc = DateTime.UtcNow;
		DateTime dateTimeBrasilia = TimeZoneInfo.ConvertTimeFromUtc(timeUtc, kstZone);

        string password;
        string username;
        bool admin = false;
        //List<string> logs = new List<string>();
        //foreach (var log in logs){
        //    Console.WriteLine($"Último acesso: {logs}");
        //}

        do
        {
            Console.Write("\nDigite o seu usuário: ");
            username = Console.ReadLine();
            Console.Write("Digite a sua senha: ");
            password = Console.ReadLine();

            if (username != "Emerson" || password != "!is@C#") 
            {
                Console.Clear();
                Console.WriteLine("\nUsuário ou senha incorretos, tente novamente!");
            }
            else
            {
                Console.Clear();
                Console.WriteLine($"{username} logou com sucesso!", admin = true);
                Console.WriteLine($"\nAcessado em: {dateTimeBrasilia.ToString("dd/MM/yyyy HH:mm:ss")} - Horário em Brasília - DF");
                Console.WriteLine($"\nEndereço IP Local: {Dns.GetHostAddresses(Dns.GetHostName()).Where(address => address.AddressFamily == AddressFamily.InterNetwork).First()} - Desktop: {Environment.MachineName}");
                Console.ReadKey();
            }
        }
        while (admin == false);
	}
}