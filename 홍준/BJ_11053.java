	import java.io.*;
	import java.util.*;
	
	public class BJ_11053 {
	
		public static void main(String[] args)throws IOException {
			// TODO Auto-generated method stub
			BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
			int n=Integer.parseInt(br.readLine());
			int A[]=new int[n];
			int dp[]=new int[n];
			int max=0;
			StringTokenizer st=new StringTokenizer(br.readLine());
			for(int i=0;i<n;i++) {
				A[i]=Integer.parseInt(st.nextToken());
			}
			dp[0]=1;
			for(int i=1;i<n;i++) {
					dp[i]=1;
					for(int j=i-1;j>=0;j--) {
						if(A[i]>A[j])
							dp[i]=Math.max(dp[i],dp[j]+1);
					}
				if(dp[i]>dp[max])
					max=i;
			}
			System.out.println(dp[max]);
		}
	}
