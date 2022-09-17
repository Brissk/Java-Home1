/* Задача 4:
Реализовать волновой алгоритм 
*/
package Java.SeminarHome;

// import java.util.*;

public class Tusk11 {

    public static void main(String[] args) {

        leeAlgo();

    }

    static void leeAlgo() {
        int[][] array = new int [10][10];
        for (int i = 0; i < array.length; i++) { 
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(" " + array[i][j] + " ");
            }
            System.out.println();
        }
    }
}
