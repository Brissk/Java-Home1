// Задача 62: Заполните спирально массив 4 на 4.

// первый вариант

/* void FillArray(int[,] array)
{
    int index = 1;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {array[i, j] = index; index++;}
    }
    index = 4;
    for (int i = 0; i < array.GetLength(0) - 1; i++)
    {
        for (int j = array.GetLength(1) - 1; j > array.GetLength(1) - 2 ; j--)
        {array[i, j] = index; index++;}
    }
    index = 7;
    for (int i = array.GetLength(0) - 1; i > array.GetLength(0) - 2; i--)
    {        
        for (int j = array.GetLength(1) - 1; j >= 0; j--)
        { array[i, j] = index; index++;}
    }
    index = 10;
    for (int i = 0; i < 1 ; i++)
    {        
        for (int j = 3; j >= 1; j--)
        { array[j, i] = index; index++;}
    }
    index = 12;
    for (int i = 1; i < array.GetLength(0)-2; i++)
    {
        for (int j = 0; j < array.GetLength(1)-1; j++)
        { array[i, j] = index; index++;}
    }
    index = 15;
    for (int i = 2; i < array.GetLength(0) - 1; i++)
    {        
        for (int j = 2; j > 0; j--)
        { array[i, j] = index;  index++;}
    }
} */
void PrintArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write($"{array[i, j],3}");
        Console.WriteLine();
    }
}


// второй вариант

void FillArray1(int[,] array)
{
    int index = 1;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            if (array[i, j] == 0 && j < array.GetLength(1) && i < 1)
            { array[i, j] = index; index++; }
            else if (array[i, j] == 0 && i > 0 && j > 2)
            { array[i, j] = index; index++; }
    }
    for (int i = array.GetLength(0) - 1; i >= 0; i--)
    {
        for (int j = array.GetLength(1) - 1; j >= 0; j--)
            if (array[i, j] == 0 && j < array.GetLength(1) && i > 2)
            { array[i, j] = index; index++; }
            else if (array[i, j] == 0 && i > 0 && j < 1)
            { array[i, j] = index; index++; }
    }
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            if (array[i, j] == 0 && j < array.GetLength(1) && i < 2)
            { array[i, j] = index; index++; }
            else if (array[i, j] == 0 && i > 0 && j > 1)
            { array[i, j] = index; index++; }
    }
    for (int i = array.GetLength(0) - 1; i >= 0; i--)
    {
        for (int j = array.GetLength(1) - 1; j >= 0; j--)
            if (array[i, j] == 0 && j < array.GetLength(1) && i > 1)
            { array[i, j] = index; index++; }           
    }
}

int[,] array = new int[4, 4];
FillArray1(array);
PrintArray(array);