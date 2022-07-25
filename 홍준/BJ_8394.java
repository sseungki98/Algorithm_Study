import java.io.*;

public class BJ_8394 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		br.close();
		int dp[]=new int[N+1];
		dp[0]=1;
		dp[1]=1;
		for(int i=2;i<=N;i++) {
		dp[i]=(dp[i-1]+dp[i-2])%10;//i-1은 새로운 사람이 악수를 안할때 i-2는 새로운 사람이 악수할때.
		}
		
		System.out.println(dp[N]);
	}

}
