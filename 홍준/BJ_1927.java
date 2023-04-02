import java.io.*;
import java.util.*;

public class BJ_1927 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        PriorityQueue<Integer> minqueue=new PriorityQueue<>();
        int input;
        for(int i=0;i<n;i++){
            input=Integer.parseInt(br.readLine());
            if(input>0){
                minqueue.add(input);
            }
            else{
                if(minqueue.isEmpty()){
                    System.out.println(0);
                }
                else
                    System.out.println(minqueue.poll());
            }
        }
        br.close();

    }
}
