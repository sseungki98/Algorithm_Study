import java.io.*;
import java.util.*;
public class BJ_15903 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int swap=Integer.parseInt(st.nextToken());
        PriorityQueue<Long> number=new PriorityQueue<>();
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            number.add(Long.valueOf(Integer.parseInt(st.nextToken())));
        }
        Long tmp;
        for(int i=0;i<swap;i++){
            tmp=number.poll()+number.poll();
            number.add(tmp);
            number.add(tmp);
        }
        tmp= Long.valueOf(0);
        while(!number.isEmpty())
            tmp+= number.poll();
        System.out.println(tmp);
    }
}
