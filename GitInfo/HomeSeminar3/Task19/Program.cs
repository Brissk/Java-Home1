// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.

void Polindrom(int x)
{
     int a = x / 10000;
    int b = x % 10;
    int c = x / 1000 % 10;
    int d = x % 100 /10;
  
    if (a == b && c == d)    
    {
        System.Console.WriteLine("Да");
    }
    else
    {
        System.Console.WriteLine("Нет");
    }

}

Polindrom(14212);
Polindrom(23432);
Polindrom(12821);