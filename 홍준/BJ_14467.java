import java.util.*;
import java.io.*;

public class BJ_14467 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int path[]=new int[10];
		int check[]=new int[10];
		int a,b;
		int cnt=0;
		String line=new String();
		Arrays.fill(path,-1);
		for(int i=0;i<N;i++) {
			line=br.readLine();
			StringTokenizer st=new StringTokenizer(line);
			a=Integer.parseInt(st.nextToken());
			b=Integer.parseInt(st.nextToken());
			if(check[a-1]==1&&path[a-1]!=b) {
				cnt++;
				path[a-1]=b;
			}
			else if(check[a-1]==0) {
				check[a-1]=1;
				path[a-1]=b;
			}
		}
		br.close();
		System.out.println(cnt);
	}
}
