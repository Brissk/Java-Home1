package Java.Seminar;

/**
 * App
 */
public class App {

  static int solve(int start, int end, int com1, int com2) {

    int[] ways = new int[end + 1];
    ways[start] = 1;

    for (int index = start + com1; index <= end; index++) {

      if (index % com2 == 0) {
        ways[index] = ways[index - com1] + ways[index / com2];
      } else {
        ways[index] = ways[index - com1];
      }
    }
    System.out.println(print(ways));
    return ways[end];
  }

  static String print(int[] items) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < items.length; i++) {

      sb.append(String.format("(%d)%d ", i, items[i]));
    }
    return sb.toString();
  }

  public static void main(String[] args) {
     System.out.println(solve(5, 15, 2, 3));
     System.out.println(solve1(5, 15, 2, 3));

  }

  static int solve1(int start, int end, int com1, int com2) {
    int count = 1;
    if((end-start) % com1 != 0) count = 0;
    for (int i = start; i <= end; i+=com1) {
      
      if(end-(i * com2) % com1 == 0) count++;
      
    }
    return count;
  }
}

/*
 * for (int i = start; i <= end; i++) {
 * 
 * if (end % com2 == 0) {
 * ways[index] = ways[index - com1] + ways[index / com2];
 * } else {
 * ways[index] = ways[index - com1];
 * }
 * 
 * List<Integer> list = new ArrayList<>();
 */
