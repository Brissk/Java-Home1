package Java.SeminarHome;
public class Tusk13 {

    public static void main(String[] args) {
  
      MyStack ms = new MyStack();
  
      System.out.println("7 строка " + ms.print());
      ms.push(1);
      ms.push(12);
      ms.push(123);
      ms.push(1234);
  
      System.out.println("12 строка " + ms.print());
      System.out.println(ms.pop());
      System.out.println("14 строка " + ms.print());
  
      System.out.println(ms.pop());
      System.out.println("17 строка " + ms.print());
  
      System.out.println(ms.pop());
      System.out.println("20 строка " + ms.print());
  
      // Node root = new Node("5");
  
      // Node l1 = new Node("3");
      // Node l11 = new Node("1");
      // Node r12 = new Node("2");
  
      // Node r2 = new Node("7");
      // Node l21 = new Node("6");
      // Node r21 = new Node("11");
      // Node l221 = new Node("10");
  
      // r2.left = l21;
      // r2.right = r21;
  
      // l1.left = l11;
      // l1.right = r12;
  
      // root.right = r2;
      // root.left = l1;
      // r21.left = l221;
  
      // Iterr.View(root, "");
    }
  
  }
  
  class MyStack {
    private int[] storage = new int[100];
    private int count = 0;
  
    int push(int item) {
      storage[count++] = item;
      return item;
    }
  
    int pop() {
      return storage[--count];
    }
  
    String print() {
      String res = "";
      for (int i = 0; i < count; i++) {
        res += storage[i] + " ";
      }
      return res;
    }
  }
  
  class MyList {
    int value;
    MyList next;
  }
  
  // class Node {
  // public Node(String v) {
  // value = v;
  // }
  
  // String value;
  // Node left;
  // Node right;
  // }
  
  // class Iterr {
  // static void View(Node n, String space) {
  // if (n != null) {
  // System.out.printf("%s%s\n", space, n.value);
  
  // if (n.left != null) {
  // View(n.left, space + " ");
  // }
  // if (n.right != null) {
  // View(n.right, space + " ");
  // }
  // }
  // }
  // }
  

  