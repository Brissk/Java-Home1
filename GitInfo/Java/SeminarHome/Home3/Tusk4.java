/* Задача 4:
Реализовать алгоритм пирамидальной сортировки (HeapSort)
*/
package Java.SeminarHome.Home3;

public class Tusk4 {

    public static void main(String[] args) {
        Hanoi(3,1,3,2);
    }

    public static void Hanoi(int n, int A, int B, int C) {
        if (n != 0) {
            Hanoi(n - 1, A, C, B);
            System.out.printf("Move the plate from %d to %d",A,B);
            System.out.println();
            Hanoi(n - 1, C, B, A);
        }

    }
}
