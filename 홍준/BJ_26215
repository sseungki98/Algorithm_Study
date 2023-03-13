import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BJ_26215 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int house=Integer.parseInt(br.readLine());
        int time=0;
        int max=0;
        int sum=0;
        int rest=0;
        Integer snow[]=new Integer[house];
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<house;i++){
            snow[i]=Integer.parseInt(st.nextToken());
            sum+=snow[i];
            if(snow[i]>max)
                max=snow[i];
        }
        if(max>1440){
            time=-1;
        }
        else {
            rest=sum-max;
            if(max>=rest)
                time=max;
            else {
                time = max + ((rest - max) / 2) + ((rest - max) % 2);
            }
        }
        if(time>1440){
            time=-1;
        }
        System.out.print(time);


    }
}
