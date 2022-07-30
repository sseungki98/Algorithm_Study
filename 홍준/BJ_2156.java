
import java.io.*;
import java.util.Arrays;

public class BJ_2156 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int grape[]=new int[n];
		int dp[]=new int[n];
		for(int i=0;i<n;i++) {
			grape[i]=Integer.parseInt(br.readLine());
		}
		br.close();
		dp[0]=grape[0];
		if(n>1) {
			dp[1]=dp[0]+grape[1];
			if(n>2) {
				if(dp[1]>=grape[0]+grape[2]&&dp[1]>=grape[1]+grape[2])
					dp[2]=dp[1];
			    else if(grape[0]+grape[2]>dp[1]&&grape[0]+grape[2]>grape[1]+grape[2])
				    dp[2]=dp[0]+grape[2];
			    else
				    dp[2]=grape[1]+grape[2];
				for(int i=3;i<n;i++) {
					if(dp[i-1]>=dp[i-2]+grape[i]&&dp[i-1]>=dp[i-3]+grape[i]+grape[i-1])
						dp[i]=dp[i-1];
					else if(dp[i-2]+grape[i]>dp[i-1]&&dp[i-2]+grape[i]>dp[i-3]+grape[i-1]+grape[i])
						dp[i]=dp[i-2]+grape[i];
					else
						dp[i]=dp[i-3]+grape[i-1]+grape[i];
					}
				}
			}
		System.out.println(dp[n-1]);
	}

}
