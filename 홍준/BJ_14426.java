import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BJ_14426 {
    static class Node {

        Map<Character, Node> childNode = new HashMap<>();
    }

    static class Trie {

        Node root = new Node(); 

     
        public void insert(String str) {

            Node node = root;
            int size = str.length();

            for (int i = 0; i < size; i++) {
                node = node.childNode.computeIfAbsent(str.charAt(i), key -> new Node());
            }
        }

        public boolean search(String str) {

            Node node = root;
            int size = str.length();

            for (int i = 0; i < str.length(); i++) {

                node = node.childNode.getOrDefault(str.charAt(i), null);


                if (node == null) {
                    return false;
                }
            }

            return true;
        }
    }


        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int ans=0;
            Trie trie = new Trie();

            for (int i = 0; i < N; i++) {
                trie.insert(br.readLine());
            }

            for (int i = 0; i < M; i++) {
                String line = br.readLine();

                if (trie.search(line)) {
                    ans++;
                }
            }

            System.out.println(ans);
        }
    }
