// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

void Distance(int x1,int x2,int y1,int y2,int z1,int z2)
{
     double S = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2);
  
    S = Math.Sqrt(S);

    System.Console.WriteLine(Math.Round(S,2));

}

Distance(3,2,6,1,8,-7);
Distance(7,1,-5,-1,0,9);
