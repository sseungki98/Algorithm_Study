import java.io.*;
import java.util.*;

public class BJ_22869 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int k=Integer.parseInt(st.nextToken());
		int visited[]=new int[n];
		int A[]=new int[n];
		st=new StringTokenizer(br.readLine());
		for(int i=0;i<n;i++)
			A[i]=Integer.parseInt(st.nextToken());
		
		if(step(n,0,A,k,visited))
			System.out.println("YES");
		else
			System.out.println("NO");	
	}
	public static boolean step(int last,int now,int A[],int max,int visit[]) {
		visit[now]=1;
		if((last-now-1)*(1+Math.abs(A[now]-A[last-1]))<=max)
			return true;
		else {
			boolean reach=false;
			for(int i=now+1;i<=now+max;i++) {
				if(i>=last)
					break;
				if(visit[i]==1)
					continue;
				if((i-now)*(1+Math.abs(A[now]-A[i]))<=max) {
					reach=step(last,i,A,max,visit);
				}
				if(reach==true)
					break;
				}
			return reach;
		}
	}

}

