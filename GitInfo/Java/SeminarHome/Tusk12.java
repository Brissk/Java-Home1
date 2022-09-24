package Java.SeminarHome;

// Описать класс для работы с бинарным деревом  
public class Tusk12 {
       public static void main(String[] args) {
        
        Tree tree = new Tree(4,8);
        tree.displayInfo();
    }
}

class Tree {
    int left;
    int right;

    public Tree() {

    }
    public Tree(int left) {
        this.left = left;
    }
    public Tree(int left,int right) {
        this.left = left;
        this.right = right;
    }
    void displayInfo(){
        System.out.printf("Left: %d, Right: %d", left,right);
    }
}

int treeView(){
    
}
