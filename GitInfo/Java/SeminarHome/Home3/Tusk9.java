/* Задача 4:
Реализовать алгоритм пирамидальной сортировки (HeapSort)
*/
package Java.SeminarHome.Home3;


public class Tusk9 {

    public static void main(String[] args) {
        int arr [] = {100,5,7,3,2,500,123,1,44,999,13,19}; // 12 elements
        heapSort(arr);
        System.out.println("HeapSort");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void heapSort(int [] arr) {

        int n = arr.length;
        for (int i = n/2-1; i >= 0; i--) {
            heapify(arr,i,n);
        }

        for (int i = n-1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;

            heapify(arr, 0, i);
        }
    }

    public static void heapify(int [] arr, int i, int n){
        int left = i*2+1;
        int right = i*2+2;
        int largest = i;
        if(left < n && arr[left] > arr[largest]){
            largest = left;
        }
        if(right < n && arr[right] > arr[largest]){
            largest = right;
        }
        if (i != largest){
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            heapify(arr, largest, n);
        } 
    }
}
