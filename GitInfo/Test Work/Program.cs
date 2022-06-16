// Написать программу, которая из имеющегося массива строк формирует массив из строк, длина которых меньше либо равна 3 символа. 
// Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
// При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

string[] FindThreeOrLess(string[] array)
{
    string s = string.Empty;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= 3)
            s += array[i] + " ";
    }
    string[] threeOrLessArray = s.Split();
    return threeOrLessArray;
}

void PrintArray(string[] array)
{
    for (int i = 0; i < array.Length - 1; i++)
        Console.Write(array[i] + " ");
}

string[] array1 = new string[] { "hello", "2", "world", ":-)" };
string[] array2 = new string[] { "1234", "1567", "-2", "computer science" };
string[] array3 = new string[] { "Russia", "Denmark", "Kazan" };

FindThreeOrLess(array1);
PrintArray(FindThreeOrLess(array1));
System.Console.WriteLine();
FindThreeOrLess(array2);
PrintArray(FindThreeOrLess(array2));
System.Console.WriteLine();
FindThreeOrLess(array3);
PrintArray(FindThreeOrLess(array3));