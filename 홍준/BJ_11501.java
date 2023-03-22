import java.io.*;
import java.util.StringTokenizer;

public class BJ_11501 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int test=Integer.parseInt(br.readLine());
        StringTokenizer st;
        int n;
        int price[];
        long benefit;
        int max;
        for(int i=0;i<test;i++){
            max=0;
            benefit=0;
            n=Integer.parseInt(br.readLine());
            price=new int[n];
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<n;j++){
                price[j]=Integer.parseInt(st.nextToken());
            }
            for(int j=n-1;j>=0;j--){
                if(max<price[j]){
                    max=price[j];
                }
                else{
                    benefit+=max-price[j];
                }
            }

            System.out.println(benefit);
        }
    }
}
