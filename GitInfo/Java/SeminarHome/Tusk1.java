/* Задача 1:
Реализовать функцию возведения числа а в степень b. a, b ∈ Z. Сводя количество выполняемых действий к минимуму. 
входные данные находятся в файле input.txt в виде
b 3
a 10
Результат нужно сохранить в файле output.txt
*/
package Java.SeminarHome;

import java.io.*;

public class Tusk1 {

    public static void main(String[] args) {
        System.out.println(gradeNumber(3, 10));
        writeFile();
    }

    public static double gradeNumber(double a, double b) {
        double result = Math.pow(a, b);
        return result;
    }
    

    public static void writeFile() {

    try(

    FileOutputStream fos = new FileOutputStream("C:/Users/cobra/GitInfo/Java/SeminarHome/input.txt"))
    {
        String text = "Hello world!";
        //double text = gradeNumber(3, 10);
        // перевод строки в байты
        byte[] buffer = text.getBytes();

        fos.write(buffer, 0, buffer.length);
        System.out.println("The file has been written");
    }catch(
    IOException ex)
    {

        System.out.println(ex.getMessage());
    }

}

}