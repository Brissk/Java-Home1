// Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.

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
void SortArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1) - 1; j++)
        {
            int minPositionRow = i;
            int minPositionColumn = j;
            for (int k = j + 1; k < array.GetLength(1); k++)
            {
                if (array[i, k] < array[minPositionRow, minPositionColumn])
                {
                    minPositionRow = i; 
                    minPositionColumn = k;
                }
            }
            int temp = array[i,j];
            array[i,j] = array[minPositionRow,minPositionColumn];
            array[minPositionRow,minPositionColumn] = temp;
        }
    }
}



int[,] array = new int[4, 4];
FillArrayRandom(array, 1, 10);
PrintArray(array);
SortArray(array);
PrintArray(array);