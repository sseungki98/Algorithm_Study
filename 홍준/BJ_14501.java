import java.io.*;
import java.util.*;

public class BJ_14501 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int day[][]=new int[N][2];
		for(int i=0;i<N;i++) {
			StringTokenizer st=new StringTokenizer(br.readLine());
			day[i][0]=Integer.parseInt(st.nextToken());
		    day[i][1]=Integer.parseInt(st.nextToken());
		}
		br.close();
		int max=0;
		int answer=0;
		for(int i=0;i<N;i++) {
			answer=0;
			answer=check(answer,day,i,N);
			if(answer>max)
				max=answer;
		}
		System.out.println(max);
	}
		
	public static int check(int ans,int day[][],int i,int N) {
		if(i+day[i][0]>N)
			return ans;
		int sum=0;
		int a;
		for(int j=i+day[i][0];j<N;j++) {
			a=0;
			a=check(ans,day,j,N);
			if(a>sum)
				sum=a;
			
		}
		ans=ans+day[i][1]+sum;
		return ans;
	}
}

