// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.

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
            Console.Write($"{array[i, j],4}");
        Console.WriteLine();
    }
}

void MatrixMultiply(int[,] array1, int[,] array2)
{
    int[,] array3 = new int[array1.GetLength(0), array1.GetLength(1)];
    for (int i = 0; i < array3.GetLength(0); i++)
    {
        for (int j = 0; j < array3.GetLength(1); j++)
        {
            int result = 0;
            for (int k = 0; k < array3.GetLength(1); k++)
            {
                result += array1[i, k] * array2[k, j];
            }
            array3[i, j] = result;
        }
    }
    PrintArray(array3);
}

int[,] array1 = new int[4, 4];
int[,] array2 = new int[4, 4];
FillArrayRandom(array1);
FillArrayRandom(array2);
PrintArray(array1);
System.Console.WriteLine();
PrintArray(array2);
System.Console.WriteLine();
MatrixMultiply(array1, array2);

