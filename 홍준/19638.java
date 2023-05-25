import java.io.*;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BJ_19638 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int centi=Integer.parseInt(st.nextToken());
        int limit=Integer.parseInt(st.nextToken());
        double tmp;
        PriorityQueue <Integer>troll=new PriorityQueue<>(n,Collections.reverseOrder());
        for(int i=0;i<n;i++)
            troll.add(Integer.parseInt(br.readLine()));

        if(troll.peek()>=centi) {
            for (int i = 0; i < limit; i++) {
                if(troll.peek()==1) {
                    System.out.println("NO");
                    System.out.println(troll.peek());
                    break;
                }
                tmp = troll.poll() / 2;
                troll.add((int) Math.round(tmp));
                if (centi > troll.peek()) {
                    System.out.println("YES");
                    System.out.println(i+1);
                    break;
                }
                if (i == limit - 1 && centi <= troll.peek()) {
                    System.out.println("NO");
                    System.out.println(troll.peek());
                    break;
                }
            }
        }
        else{
            System.out.println("YES");
            System.out.println(0);
        }


    }
}
