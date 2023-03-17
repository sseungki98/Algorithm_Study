import java.io.*;
import java.util.Arrays;

public class BJ_9657 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        String winner[]={"0","SK","CY","SK","SK"};
        String dp[]= Arrays.copyOf(winner,n+1);
        String answer="";
        if(n>4) {
            for(int i=5;i<n+1;i++) {
                if (dp[i - 1] == "CY" || dp[i - 3] == "CY" || dp[i - 4] == "CY")
                    dp[i] = "SK";
                else
                    dp[i] = "CY";
            }
        }
        System.out.print(dp[n]);
    }
}
