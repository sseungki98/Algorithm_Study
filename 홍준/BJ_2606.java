import java.io.*;
import java.util.StringTokenizer;

public class BJ_2606 {
	public static void main (String[] args) throws IOException {
		// TODO Auto-generated method stub
     BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
     int N=Integer.parseInt(br.readLine());
     int V=Integer.parseInt(br.readLine());
     int a,b;
     String line=new String();
     int W[][]=new int[N][N];
     int visited[]=new int[N];
     visited[0]=1;
     int cnt=0;
     for(int i=0;i<V;i++) {
    	 line=br.readLine();
    	 StringTokenizer st=new StringTokenizer(line);
    	 a=Integer.parseInt(st.nextToken());
    	 b=Integer.parseInt(st.nextToken());
    	 W[a-1][b-1]=1;
    	 W[b-1][a-1]=1;
     }
     br.close();
     visited=find(W,N,visited,0);
     for(int j=0;j<N;j++) {
    	 if(visited[j]==1) {
    		 cnt++;
    	 }
     }
     System.out.println(cnt-1);
     
	}
	public static int[] find(int W[][],int N,int visit[],int start) {
		for(int j=1;j<N;j++) {
			if(W[start][j]==1&&visit[j]==0) {
				visit[j]=1;
				visit=find(W,N,visit,j);
			}
		}
		return visit;
 }
}
