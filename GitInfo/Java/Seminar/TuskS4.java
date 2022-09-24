package Java.Seminar;

/* 
 */

// import java.util.ArrayList;

public class TuskS4 {
    public static void main(String[] args) {
        int [] array = new int[] {-3,0,2,4,5};
        int k = 7;
        int x = 0;
        int y = 0;
        for (int i = 0; i < array.length-1; i++) {
            for (int j = 1+i; j < array.length; j++) {
                if(array[i]+array[j] == k){
                    x = array[i];
                    y = array[j];
                    System.out.printf("%d + %d = %d\n", x,y,k);
                }               
            }
        }
        if(x == 0 && y == 0)
            System.out.println("Нет решения");
    }
}
    

   