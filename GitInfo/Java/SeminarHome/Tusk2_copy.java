
package Java.SeminarHome;

public class Tusk2_copy {

    public static void main(String[] args) {
        System.out.println(transform(2, 7, 1, 2));
    }

    public static int transform(int start, int end, int com1, int com2) {
        int [] ways = new int [end+1];
        ways[start] = 1;
        for (int i = start+com1; i <= end; i++) {
            if(i%com2==0){
                ways[i] = ways[i-com1] + ways[i/com2];
            }
            else{
                ways[i] = ways[i-com1];
            }
        }
        return ways[end]; //Количество маршрутов из "start" в "end"
    }

}

/* public static int transform1(int start, int end, int c, int len ) {
    if(len == 0){

    }
} */
