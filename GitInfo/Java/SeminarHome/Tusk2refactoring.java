
package Java.SeminarHome;

/* Задача 2:

 */
import java.util.*;

public class Tusk2refactoring {

    public static void main(String[] args) {
        System.out.println(transform(1, 7, 2, 1));

    }

    public static String transform(double a, double b,int c, int d) {
        
        StringBuilder sb = new StringBuilder(); // Рефакторинг)))
        Scanner iScanner = new Scanner(System.in);
        System.out.print("Введите a: ");
        a = iScanner.nextDouble();
        System.out.print("Введите b: ");
        b = iScanner.nextDouble();
        iScanner.close();
        
        while (a != b) {
            if (a >= b) {
                System.out.println("Решения не существует");
                break;
            }
            while (a * c < b) {
                a *= c;
                sb.append("k1");
            }
            if (a < b) {
                a += d;
                sb.append("k2");
            }
        }
        return sb.toString();
    }
}

