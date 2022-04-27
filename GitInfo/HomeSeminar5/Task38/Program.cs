// Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.

void Random(double[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().NextDouble()*1000;
    }
}

void Print(double[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}
double Maximum(double[] array)
{    
    double max = 0;
    for (int i = 0; i < array.Length; i++)
    {        
        if(array[i] > max) max = array[i];
    }
    return max;
}
double Minimum(double[] array)
{    
    double min = array[0];
    for (int i = 0; i < array.Length; i++)
    {        
        if(array[i] < min) min = array[i];
    }
    return min;
}
double[] array = new double[4];
Random(array);
Print(array);
System.Console.WriteLine(Maximum(array)-Minimum(array));






