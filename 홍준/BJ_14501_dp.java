import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ_14501 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int work[][]=new int[n+1][2];
        int dp[]=new int[n+1];
        int max=0;
        StringTokenizer st;
        for(int i=1;i<=n;i++){
            st=new StringTokenizer(br.readLine());
            work[i][0]=Integer.parseInt(st.nextToken());
            work[i][1]=Integer.parseInt(st.nextToken());
        }
        for(int i=n;i>0;i--){
            if(i+work[i][0]-1>n){
                dp[i]=max;
                continue;
            }
            if(i+work[i][0]-1==n)
                dp[i]=Math.max(work[i][1],max);
            else {
                dp[i] = Math.max((work[i][1] + dp[i + work[i][0]]), max);
            }
            max=Math.max(dp[i],max);
        }
        System.out.println(dp[1]);

    }
}
