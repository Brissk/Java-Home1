/* Задача 4:
Написать программу, показывающую последовательность действий для игры “Ханойская башня”
*/
package Java.SeminarHome;


public class Tusk4 {

    public static void main(String[] args) {
    }

    public static String hanoiTower(int n) {

        int x = n;
        int y = 0;
        int z = 0;
        StringBuilder sb = new StringBuilder();
        while(z!=x){
            if(y==z){
                
            }
            if (x % 2 == 0) {
                x -= 1;
                y += 1;
                sb.append("1->2");
            }
            
        }
        return "";

    }
}
