// Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.

int NumbersSum(int minValue, int maxValue)
{
    if (minValue > maxValue) return 0;

    else return minValue + NumbersSum(minValue + 1, maxValue);
}

System.Console.WriteLine(NumbersSum(1, 15));