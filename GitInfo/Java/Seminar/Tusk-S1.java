package Java.Seminar;

/* Найти длину наибольшой общей подпоследовательности
  **требуется восстановить эту подпоследовательность
 */
import java.util.*;

public class Tusk0 {
    public static void main(String[] args) {
        int [] a = new int [] {1,2,3,4,5};
        int [] b = new int [] {3,4,5,1,2};
        func(a);
        printArray(b);
    }


    static void func(int[]array){

        List<int[]> list = Arrays.asList(array);  
        
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list);
        }
       
    }

    static String printArray(int[] items) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < items.length; i++) {
    
          sb.append(String.format("(%d)%d ", i, items[i]));
        }
        return sb.toString();
      }
}