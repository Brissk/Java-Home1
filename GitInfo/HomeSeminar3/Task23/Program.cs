// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

void Cubic(int x)
{
    int i = 1;
    int square = 0;
     while ( i <= x)
     {
         square = i*i*i;
         i++;
         System.Console.WriteLine(square);
     }    

}

Cubic(5);