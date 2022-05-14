// Задача 50: Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, 
// и возвращает значение этого элемента или же указание, что такого элемента нет.

void FillArrayRandom(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            array[i, j] = new Random().Next(0, 10);
    }
}
void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i, j] + " ");
        Console.WriteLine();
    }
}

void FindArrayElement(int[,] array, int a, int b)
{
    try
    {
        System.Console.WriteLine(array[a, b]);
    }
    catch (System.Exception)
    {
        System.Console.WriteLine("Такого числа в массиве нет");        
    } 
}

int a, b;
Console.WriteLine("Введите индекс первого элемента:");
a = int.Parse(Console.ReadLine());
Console.WriteLine("Введите индекс второго элемента:");
b = int.Parse(Console.ReadLine());

int[,] array = new int[3, 4];
FillArrayRandom(array);
PrintArray(array);
FindArrayElement(array, a, b);