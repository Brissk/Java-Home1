// Задача 64: Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр.

int NumbersSum(int value)
{
    if (value == 0) return 0;

    else return value % 10 + NumbersSum(value / 10);
}

System.Console.WriteLine(NumbersSum(12345));