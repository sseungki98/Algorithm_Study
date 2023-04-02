import java.io.*;
import java.util.*;
public class BJ_2075 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue <Integer>maxqueue=new PriorityQueue<>(Collections.reverseOrder());
        StringTokenizer st;
        int n=Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++)
                maxqueue.add(Integer.parseInt(st.nextToken()));
        }
        for(int i=0;i<n-1;i++)
            maxqueue.remove();
        System.out.println(maxqueue.poll());
    }

}
