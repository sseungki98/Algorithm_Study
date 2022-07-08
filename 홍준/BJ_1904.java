import java.io.*;

public class BJ_1904 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		br.close();
		int dp[]=new int[N+1];
		dp[0]=1;
		dp[1]=1;
		for(int i=2;i<N+1;i++) {
			dp[i]=(dp[i-1]+dp[i-2])%15746;
		}
		System.out.println(dp[N]);
		
	}
}
