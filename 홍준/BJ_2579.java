import java.io.*;
import java.util.*;

public class BJ_2579 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int weight[]=new int[N];
		int a=0;
		for(int i=0;i<N;i++) {
			weight[i]=Integer.parseInt(br.readLine());
		}
		int dp[]=new int[N];
		if(N>=3) {
		  dp[0]=weight[0];
		  dp[1]=weight[0]+weight[1];
		  if(weight[0]+weight[2]>=weight[1]+weight[2]) {
			dp[2]=weight[0]+weight[2];
		  }
		  else
			  dp[2]=weight[1]+weight[2];
		  for(int i=3;i<N;i++) {
			  if(dp[i-3]+weight[i-1]+weight[i]>=dp[i-2]+weight[i]) {
				  dp[i]=dp[i-3]+weight[i-1]+weight[i];
			  }
			  else
			  {
				dp[i]=dp[i-2]+weight[i];
			  }
		  }
		  System.out.println(dp[N-1]);
		}
		else {
			for(int i=0;i<N;i++)
				a+=weight[i];
			System.out.println(a);
		}
      }
	}
