/* Задача 2: Напишите программу, которая выводит
случайное трёхзначное число и удаляет вторую цифру
этого числа.*/

int x = new Random().Next(100,1000);

System.Console.WriteLine(x);

int y = x%10;
int z = x/100;

System.Console.WriteLine($"{z}{y}");



