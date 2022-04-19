int x = 65699;

if (x<100)
{
    System.Console.WriteLine("Третьей цифры нет");
}

if (x<1000 && x>=100 )
{
    int y = x%10;
    System.Console.WriteLine(y);
}
if (x<10000 && x>=1000 )
{
    int z = x%100/10;
    System.Console.WriteLine(z);
}
if (x<100000 && x>=10000 )
{
    int q = x%1000/100;
    System.Console.WriteLine(q);
}