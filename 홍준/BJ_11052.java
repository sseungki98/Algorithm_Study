import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ_11052 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int dp[]=new int[n+1];
        StringTokenizer st=new StringTokenizer(br.readLine());
        dp[0]=0;
        for(int i=1;i<=n;i++){
            dp[i]=Integer.parseInt(st.nextToken());
        }

        for(int i=1;i<=n;i++){
            dp[i]=calculate(dp,i);
        }
        System.out.println(dp[n]);

    }
    public static int calculate(int dp[],int i){
        for(int j=i;j>0;j--){
            dp[i]=Math.max(dp[i],dp[i-j]+dp[j]);
        }
        return dp[i];
    }
}
