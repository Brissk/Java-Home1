package Java.Seminar;

import Java.Seminar.Tree.Iterr;

public class TuskS5 {

    public static void main(String[] args) {

         Tree root1 = new Tree(1);
        Tree l1 = new Tree(2);
        Tree r2 = new Tree(3);
        Tree l3 = new Tree(4);
        Tree r4 = new Tree(5);
        Tree l5 = new Tree(6);
        Tree r6 = new Tree(7);
        Tree l7 = new Tree(8);
        Tree r8 = new Tree(9);

        root1.left = l1;
        root1.right = r2;
        l1.left = l3;
        l1.right = r4;
        r2.left = l5;
        r2.right = r6;
        l3.left = l7;
        l3.right = r8; 
Iterr.View(root1, "");
 
        Tree root =
                new Tree(20,
                        new Tree(7,
                                new Tree(4, null, new Tree(6)), new Tree(9)),
                        new Tree(35,
                                new Tree(31, new Tree(28), null),
                                new Tree(40, new Tree(38), new Tree(52))));

                                System.out.println("Сумма дерева(прямой обход): " + root.sum());
    }
}

class Tree {
    Tree left;
    Tree right;
    int value;

    public Tree(int value) {
        this.value = value;
    }
    public Tree(int value, Tree left, Tree right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
    public int sum() {
        int summ = value;

        if (left != null) {
            summ += left.sum();
        }

        if (right != null) {
            summ += right.sum();
        }
        return summ;

    }

class Iterr {
    static void View(Tree n, String space) {
        if (n != null) {
            System.out.printf("%s%s\n", space, n.value);

            if (n.left != null) {
                View(n.left, space + " ");
            }
            if (n.right != null) {
                View(n.right, space + " ");
            }
        }
    }
}
}

/* class TreeLookUp extends Tree{
    static String s; 
    s = n.value;
    public static String LookUp(Tree n){
        if (n.left != null){
            s+=n.left.value;
            LookUp(n.left);
        }
        if (n.right != null){
            s+=n.right.value;
            LookUp(n.right);
        }
        return s;
    }
} */
