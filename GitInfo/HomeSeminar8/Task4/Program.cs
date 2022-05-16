// Задача 60: Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
// Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.

void FillArrayInARow(int[,,] array)
{
    int index = 10;
    for (int i = 0; i < array.GetLength(0); i++)
     {   for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
            {
                array[i, j, k] = i + j + k + index;
            }
            index+=2;
        }
        index+=2;
     }
}
void PrintArray(int[,,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
            {
                Console.WriteLine($"[{i},{j},{k}] - " + array[i, j, k] + " ");
            }
            Console.WriteLine();
        }
        Console.WriteLine();
    }
    System.Console.WriteLine();
}


int[,,] array = new int[3, 3, 3];
FillArrayInARow(array);
PrintArray(array);

