package Java.Seminar;

/* Найти наибольшую общую последовательность
 */

import java.util.ArrayList;
import java.util.List;

public class TuskS2 {
    public static void main(String[] args) {
        func(2, 7, 1    , 2);
        List<String> people = new ArrayList<String>();
        people.add("Tom");
        people.add("Alice");
        people.add("Kate");
        people.add("Sam");
    }

    public static int transform(int start, int end, int com1, int com2) {
        int[] ways = new int[end + 1];
        ways[start] = 1;
        for (int i = start + com1; i <= end; i++) {
            if (i % com2 == 0) {
                ways[i] = ways[i - com1] + ways[i / com2];
            } else {
                ways[i] = ways[i - com1];
            }
        }
        return ways[end]; // Количество маршрутов из "start" в "end"
    }

    static void func(int start, int end, int com1, int com2){
        
        int [][] array = new int [transform(2, 7, 1, 2)][end];

        for (int i = 0; i < array.length; i++){
            for (int j = 0; j < array[i].length; j++) {
                if (start + com1 <= end) {
                    array[i][j] = start+com1;
                    start++;
                }
                if (start * com2 <= end) {
                    ++i;
                    array[i][j] = start*com2;
                    start++;
                }
            }
        
        }
        for (int i=0; i<array.length; i++) {
            for (int j=0; j<array[i].length; j++)
                System.out.print(array[i][j] + " ");
            System.out.println();
        }

    }
}
// Распечатка двумерного массива