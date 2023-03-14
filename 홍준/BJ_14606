import java.io.*;

public class BJ_14606 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int pizza=Integer.parseInt(br.readLine());
        int dp[]=new int[pizza+1];
        dp[0]=0;
        dp[1]=0;
        int b=0;
        int c=0;
        if(pizza>=2){
            dp[2]=1;
            for(int i=3;i<=pizza;i++){
                b=i/2+i%2;
                c=i/2;
                dp[i]=b*c+dp[b]+dp[c];
            }
        }
        System.out.print(dp[pizza]);

    }
}
