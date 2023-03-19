
import java.io.*;
import java.util.ArrayList;

public class BJ_13413 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int test=Integer.parseInt(br.readLine());
        int n;
        int B1;
        int B2;
        int cnt=0;
        String line1;
        String line2;
        for(int i=0;i<test;i++){
            cnt=0;
            B1=0;
            B2=0;
            n=Integer.parseInt(br.readLine());
            line1=br.readLine();
            line2=br.readLine();
            for(int j=0;j<n;j++){
                if(line1.charAt(j)!= line2.charAt(j)) {
                    cnt++;
                }
                if(line1.charAt(j)=='B')
                    B1++;
                if(line2.charAt(j)=='B')
                    B2++;
            }
            if(B1==B2){
                cnt=cnt/2;
            }
            else{
                cnt=Math.abs(B1-B2)+(cnt-Math.abs(B1-B2))/2;
            }
            System.out.println(cnt);
        }
    }
}
