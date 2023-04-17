import java.io.*;
import java.util.StringTokenizer;

public class BJ_1991 {
    static class Node{
        String name;
        Node left;
        Node right;

        public Node(String name) {
            this.name = name;
            this.left = null;
            this.right = null;
        }
    }

    static class Tree{
        Node root=new Node(".");

        public void createNode(String mid,String left,String right){
            if(root.name.equals(".")){
                if(!mid.equals("."))
                    root=new Node(mid);
                if(!left.equals("."))
                    root.left=new Node(left);
                if(!right.equals("."))
                    root.right=new Node(right);
            }
            else find(root,mid,left,right);
        }

        public void find(Node node,String mid,String left,String right){
            if(node==null)
                return;
            if(mid.equals(node.name)){
                if(!left.equals("."))
                    node.left=new Node(left);
                if(!right.equals("."))
                    node.right=new Node(right);
            }
            find(node.left,mid,left,right);
            find(node.right,mid,left,right);
        }
        public void preOrder(Node node){
            System.out.print(node.name);
            if(node.left!=null)
                preOrder(node.left);
            if(node.right!=null)
                preOrder(node.right);
        }
        public void inOrder(Node node){
            if(node.left!=null)
                inOrder(node.left);
            System.out.print(node.name);
            if(node.right!=null)
                inOrder(node.right);
        }
        public void postOrder(Node node){
            if(node.left!=null)
                postOrder(node.left);
            if(node.right!=null)
                postOrder(node.right);
            System.out.print(node.name);

        }

    }

    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        Tree tree=new Tree();
        StringTokenizer st;
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            tree.createNode(st.nextToken(),st.nextToken(),st.nextToken());
        }
        tree.preOrder(tree.root);
        System.out.println();

        tree.inOrder(tree.root);
        System.out.println();

        tree.postOrder(tree.root);
        System.out.println();

    }
}

