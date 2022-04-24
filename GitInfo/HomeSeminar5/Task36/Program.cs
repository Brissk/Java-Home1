// Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.

void Random(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(0, 1000);
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

int NegativeSum(int[] array)
{
    int positive = 0;
    int negative = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] % 2 == 0) 
        positive++;
        else 
        negative += array[i];        
    }
    System.Console.WriteLine("Сумма нечётных чисел: " + negative);
    return negative;
}
int[] array = new int[4];
Random(array);
Print(array);
NegativeSum(array);