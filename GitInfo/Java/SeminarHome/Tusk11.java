/* Задача 4:
Реализовать волновой алгоритм 
*/
package Java.SeminarHome;

public class Tusk11 {

    public static void main(String[] args) {

        leeAlgo();
    }

    static void leeAlgo() {
        System.out.println("Изначальный массив");
        int[][] array = new int[15][15];
        int startX = 2;
        int startY = 0;
        array[startX][startY] = -3; // Точка отсчёта, начало
        int endX = 9;
        int endY = 13;
        array[endX][endY] = -4; // Конечная точка
        array[8][1] = -2;
        array[7][1] = -2;
        array[0][2] = -2;
        array[1][2] = -2;
        array[2][2] = -2;
        array[3][2] = -2;
        array[5][3] = -2;
        array[5][4] = -2;
        array[6][3] = -2;
        array[7][3] = -2;
        array[8][3] = -2;
        array[0][5] = -2;
        array[1][5] = -2;
        array[2][5] = -2;
        array[3][5] = -2;
        array[3][7] = -2;
        array[4][7] = -2;
        array[5][7] = -2;
        array[6][7] = -2;
        array[7][7] = -2;

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.printf("%2d ", array[i][j]);
            }
            System.out.println();
        }
        if (startX - 1 != -1 && array[startX - 1][startY] != -2)
            array[startX - 1][startY] = 1;

        if (startY + 1 != -1 && array[startX][startY + 1] != -2)
            array[startX][startY + 1] = 1;

        if (startX + 1 != -1 && array[startX + 1][startY] != -2)
            array[startX + 1][startY] = 1;

        if (startY - 1 != -1 && array[startX][startY - 1] != -2)
            array[startX][startY - 1] = 1;

        int stepsCount = 0;
        for (int i = 1; i < 20; i++) {
            for (int j = 0; j < array.length; j++) {
                for (int k = 0; k < array[0].length; k++) {
                    if (array[j][k] == i) {
                        if (j - 1 != -1 && array[j - 1][k] != -2 && array[j - 1][k] == 0)
                            array[j - 1][k] = i + 1;
                        else if (j - 1 != -1 && array[j - 1][k] == -4) {
                            stepsCount = i + 1;
                        }

                        if (k + 1 != array[0].length && array[j][k + 1] != -2 && array[j][k + 1] == 0)
                            array[j][k + 1] = i + 1;
                        else if (k + 1 != array[0].length && array[j][k + 1] == -4) {
                            stepsCount = i + 1;
                        }

                        if (j + 1 != array.length && array[j + 1][k] != -2 && array[j + 1][k] == 0)
                            array[j + 1][k] = i + 1;
                        else if (j + 1 != array.length && array[j + 1][k] == -4) {
                            stepsCount = i + 1;
                        }

                        if (k - 1 != -1 && array[j][k - 1] != -2 && array[j][k - 1] == 0)
                            array[j][k - 1] = i + 1;
                        else if (k - 1 != -1 && array[j][k - 1] == -4) {
                            stepsCount = i + 1;
                        }
                    }

                }

            }
            if (stepsCount != 0)
                break;
        }
        System.out.println();
        System.out.println("Минимальное число ходов: " + stepsCount);
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.printf("%2d ", array[i][j]);
            }
            System.out.println();
        }
        for (int i = stepsCount-1; i > 0; i--) {
            if (endX-1 != -1 && array[endX-1][endY] == i)
            {array[endX-1][endY] = -4;endX-=1;}
            else if (endY+1 != array[0].length && array[endX][endY+1] == i)
            {array[endX][endY+1] = -4;endY+=1;}
            else if (endX+1 != array.length && array[endX+1][endY] == i)
            {array[endX+1][endY] = -4; endX+=1;}
            else if (endY-1 != -1 && array[endX][endY-1] == i)
            {array[endX][endY-1] = -4;endY-=1;}
        }
        System.out.println();
        System.out.println("Самый короткий маршрут(показан числом -4)");
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[0].length; j++) {
                System.out.printf("%2d ", array[i][j]);
            }
            System.out.println();
        }
    }
}
