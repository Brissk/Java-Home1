// Задача 52: Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.

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
string Average(int[,] array)
{

    string result = string.Empty;
    for (int i = 0; i < array.GetLength(1); i++)  
    {
        double sum = 0;
        for (int j = 0; j < array.GetLength(0); j++)  
            sum = (sum + array[j, i]);            

        sum = Math.Round(sum / array.GetLength(0), 1);
        result += sum + "   ";        
    }
    return result;
}

int[,] array = new int[3, 4];
FillArrayRandom(array);
PrintArray(array);
System.Console.WriteLine(Average(array));