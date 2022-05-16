// Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

void FillArrayRandom(int[,] array, int minValue, int maxValue)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            array[i, j] = new Random().Next(minValue, maxValue);
    }
}
void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            System.Console.Write($"{array[i, j],4}");
        System.Console.WriteLine();
    }
    System.Console.WriteLine();
}
int MinSumInRow(int[,] array)
{
    int result = 100;
    int index = 0;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        int sum = 0;
        for (int j = 0; j < array.GetLength(1); j++)
        {
            sum += array[i, j];            
        }
        if (result > sum)
            {
                result = sum;
                index = i;
            }
        System.Console.WriteLine($"Сумма чисел в ряду {i} = " + sum);       
    }
    System.Console.WriteLine($"Наименьшая сумма в ряду № {index} и равна " + result);
    return result;
}



int[,] array = new int[4, 10];
FillArrayRandom(array, 1, 20);
PrintArray(array);
MinSumInRow(array);
