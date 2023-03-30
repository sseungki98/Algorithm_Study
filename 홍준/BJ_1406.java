import java.io.*;
import java.util.*;
import java.util.StringTokenizer;

public class BJ_1406 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Stack<Character> leftSt = new Stack<>();
        Stack<Character> rightSt = new Stack<>();
        StringTokenizer st;
        String line=br.readLine();
        for(int i=0;i<line.length();i++) {
            leftSt.push(line.charAt(i));
        }
        int inst=Integer.parseInt(br.readLine());
        for(int i=0;i<inst;i++){
            st=new StringTokenizer(br.readLine());
            switch (st.nextToken()){
                case("L"):
                    if(!leftSt.isEmpty())
                        rightSt.push(leftSt.pop());
                    break;
                case("D"):
                    if(!rightSt.isEmpty())
                        leftSt.push(rightSt.pop());
                    break;
                case("B"):
                    if(!leftSt.isEmpty()) {
                        leftSt.pop();
                    }
                    break;
                case("P"):
                    leftSt.push(st.nextToken().charAt(0));
                    break;
            }
        }
        while(!leftSt.isEmpty())
            rightSt.push(leftSt.pop());

        while(!rightSt.isEmpty())
            sb.append(rightSt.pop());
        System.out.println(sb);
        br.close();
    }
}
