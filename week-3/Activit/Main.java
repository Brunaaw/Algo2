public class Main {
    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();

        // Inserir elementos na árvore
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);

        // Exibir a árvore em ordem
        System.out.println("Árvore em ordem:");
        bst.inorder();

        // Buscar elementos
        System.out.println("Buscar 40: " + bst.search(40)); // true
        System.out.println("Buscar 90: " + bst.search(90)); // false

        // Remover um elemento
        System.out.println("Removendo 50...");
        bst.delete(50);

        // Exibir a árvore após a remoção
        System.out.println("Árvore após remoção:");
        bst.inorder();
    }
}