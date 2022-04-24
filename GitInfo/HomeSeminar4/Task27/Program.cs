// Задача 27  Напишите функцию, которая принимает на вход число и выдаёт сумму цифр в числе.

int Summary(int x)
{
    int result = 0;

    for (int i = 0; x != 0 ;i++)
    {
        result += (x % 10);
        x /= 10;
    }

    return result;

}

System.Console.WriteLine(Summary(452));
System.Console.WriteLine(Summary(82));
System.Console.WriteLine(Summary(9012));
