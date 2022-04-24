// Задача 29  Напишите программу, которая задаёт массив из некоторого количества элементов и выводит их на экран с помощью функций. 
//            (можно спрашивать количество вводимых элементов и вводить все значения с клавиатуры)

// Первый вариант - 
/* string PrintArray(string x)
{
    System.Console.WriteLine("Введите числа через запятые:");
    x = Console.ReadLine();
    string result = string.Empty;

    for (int i = 0; i < x.Length ;i++)
    {
        result += x[i] + " ";
    }

    return result;

}

System.Console.WriteLine(PrintArray("5")); */

// Второй вариант

/* void PrintArray(int x)
{
    System.Console.WriteLine("Введите размер массива:");
    x = Convert.ToInt32(Console.ReadLine());
    int[] array = new int[x];

    for (int i = 0; i < x ;i++)
    {
        array[i] = new Random().Next(0,20);
        System.Console.Write($"{array[i]} " );
    }

}

PrintArray(5); */

// Третий авриант
void Print(int[] mas)
{
    for (int i = 0; i < mas.Length; i++)
    {
        Console.Write(mas[i] + " ");
    }
    Console.WriteLine();

}

void PrintArray(int x)
{
    System.Console.WriteLine("Введите размер массива:");
    x = Convert.ToInt32(Console.ReadLine());
    int[] array = new int[x];

    for (int i = 0; i < x; i++)
    {
        Console.WriteLine("Введите элемент массива:");
        array[i] = Convert.ToInt32(Console.ReadLine());
    }
    Print(array);
}


PrintArray(5);

