import java.io.*;
import java.util.*;

public class BJ_11279 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        PriorityQueue<Integer> maxqueue=new PriorityQueue<>(Collections.reverseOrder());
        int input;
        for(int i=0;i<n;i++){
            input=Integer.parseInt(br.readLine());
            if(input>0){
                maxqueue.add(input);
            }
            else{
                if(maxqueue.isEmpty()){
                    System.out.println(0);
                }
                else
                    System.out.println(maxqueue.poll());
            }
        }
        br.close();

    }
}
