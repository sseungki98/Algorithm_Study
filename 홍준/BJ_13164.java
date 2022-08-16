import java.io.*;
import java.util.*;

public class BJ_13164 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int y[]=new int[n];
		int k=Integer.parseInt(st.nextToken());
		ArrayList<Integer> min=new ArrayList<Integer>();
		int answer=0;
		if(n==k) {
			System.out.println(0);
		}
		else {
			st=new StringTokenizer(br.readLine());
			for(int i=0;i<n;i++) {
				y[i]=Integer.parseInt(st.nextToken());
				if(i>0)
					min.add(Math.abs(y[i-1]-y[i]));	
			}
			Collections.sort(min);
			for(int j=0;j<n-k;j++)
				answer=answer+min.get(j);
			System.out.println(answer);
		}
	}

}
