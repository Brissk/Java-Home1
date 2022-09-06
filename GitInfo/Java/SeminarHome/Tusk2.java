
package Java.SeminarHome;

/* Задача 2:
На вход некоторому исполнителю подаётся два числа (a, b). У исполнителя есть две команды
- команда 1 (к1): увеличить в с раза, а умножается на c
- команда 2 (к2): увеличить на d, к a прибавляется d
написать программу, которая выдаёт набор команд, позволяющий число a превратить в число b или сообщить, что это невозможно
Пример 1: а = 1, b = 7, c = 2, d = 1
ответ: к2, к2, к2, к2, к2, к2, k2 или к1, к1, к2, к2, к2 
Можно начать с более простого – просто подсчёта общего количесвтва вариантов 
Пример 2: а = 11, b = 7, c = 2, d = 1
ответ: нет решения. 
*Подумать над тем, как сделать минимальное количество команд
 */
import java.util.Scanner;

public class Tusk2 {

    public static void main(String[] args) {
        transform(1, 30, 2, 1);

    }

    public static String transform(double a, double b,int c, int d) {
        //int c отвечает за умножение и также является командой "к1"
        //int d отвечает за сложение и также является командой "к2"
        String s = "";
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
                s += "k1";
            }
            if (a < b) {
                a += d;
                s += "k2";
            }
        }
        System.out.println(s);
        return s;
    }
}

