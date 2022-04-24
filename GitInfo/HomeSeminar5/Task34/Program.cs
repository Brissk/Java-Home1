// Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.



void Random(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(100, 1000);
    }
}

void Print(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}
int PositiveNumber(int[] array)
{
    int positive = 0;
    int negative = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] % 2 == 0) 
        positive++;
        else 
        negative++;        
    }
    System.Console.WriteLine("Количество положительных чисел: " + positive);
    return positive;
}

int[] array = new int[4];
Random(array);
Print(array);
PositiveNumber(array);