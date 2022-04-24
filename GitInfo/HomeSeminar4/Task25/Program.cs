// Задача 25  Напишите (функцию) цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.

double Grade(int A, int B)
{
    double result = Math.Pow(A,B);
    
    return result;
    
}

System.Console.WriteLine(Grade(2,4));
System.Console.WriteLine(Grade(3,5));