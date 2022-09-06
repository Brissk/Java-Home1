/* Задача 3:
Написать программу вычисления n-ого треугольного числа
*/
package Java.SeminarHome;

import java.util.Scanner;

public class Tusk3 {

    public static void main(String[] args) {
        System.out.println(triangleNumber(5));
    }

    public static double triangleNumber(double n) {
        Scanner iScanner = new Scanner(System.in);
        System.out.print("Введите a: ");
        n = iScanner.nextDouble();
        iScanner.close();
        
        return 0.5*n*(n+1);
    
}
}