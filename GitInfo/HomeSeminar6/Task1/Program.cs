// Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.

int PositiveNumber(string s)
{
    string [] stringArray = new string [s.Length];
    stringArray = s.Split();
    
    int positive = 0;    
    for (int i = 0; i < stringArray.Length; i++)
    {        
        if(int.Parse(stringArray[i]) > 0)
        positive++;                       
    }
    System.Console.WriteLine("Количество положительных чисел: " + positive); 
    return positive;
}

PositiveNumber("0 7 8 -2 -2");