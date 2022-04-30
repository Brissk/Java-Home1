// Напишите программу, которая найдёт точку пересечения двух прямых, 
// заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.

double Cross(double b1, double k1, double b2, double k2)
{
    // k2 * x + b2 = k1 * x + b1;
    double x = (b2-b1) / (k1-k2);   
    double y = k2 * x + b2;

System.Console.WriteLine($"{x};{y}");
return x;
}

Cross(2, 5, 4, 9);