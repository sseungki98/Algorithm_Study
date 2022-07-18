import java.io.*;
import java.util.Arrays;

public class BJ_1058 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		char Friend[][]=new char[N][N];
		int visited[]=new int[N];
		String line;
		int cnt=-1;
		int max=0;
		for(int i=0;i<N;i++) {
			line=br.readLine();
			for(int j=0;j<N;j++) {
				Friend[i][j]=line.charAt(j);
			}
		}
		for(int i=0;i<N;i++) {
			visited[i]=1;
			for(int j=0;j<N;j++) {
				if(Friend[i][j]=='Y') {
					visited=Find(Friend,j,N,visited);					
				}		
			}
			for(int j=0;j<N;j++) {
				if(visited[j]==1)
					cnt++;
			}
			if(cnt>max)
				max=cnt;
			Arrays.fill(visited,0);
			cnt=-1;
		}
		System.out.println(max);

	}
	public static int[] Find(char Friend[][],int i,int N,int visit[]) {
		visit[i]=1;
		for(int k=0;k<N;k++) {
			if(Friend[i][k]=='Y'&&visit[k]==0) {
				visit[k]=1;
			}
		}
		
		return visit;
	}

}
