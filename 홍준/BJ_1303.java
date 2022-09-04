import java.io.*;
import java.util.*;

public class BJ_1303 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		char W[][]=new char[m][n];
		int visited[][]=new int[m][n];
		int cnt=0;
		double Wcnt=0;
		double Bcnt=0;
		String line;
		for(int i=0;i<m;i++) {
			line=br.readLine();
			for(int j=0;j<n;j++) {
				W[i][j]=line.charAt(j);
			}
		}
		for(int i=0;i<m;i++) {
			for(int j=0;j<n;j++) {
				if(visited[i][j]==1)
					continue;
				if(W[i][j]=='B') {
					cnt=1;
					cnt=find(W,visited,'B',m,n,i,j,cnt);
					Bcnt=Bcnt+Math.pow(cnt,2);
				}
				else if(W[i][j]=='W') {
					cnt=1;
					cnt=find(W,visited,'W',m,n,i,j,cnt);
					Wcnt=Wcnt+Math.pow(cnt, 2);
				}
			}
		}
		System.out.println((int)Wcnt+" "+(int)Bcnt);

	}
	public static int find(char W[][],int visited[][],char team,int m,int n,int x,int y,int cnt) {
		if(visited[x][y]==1) //이미 방문했던곳인 경우 
			return cnt;
		else
			visited[x][y]=1; //방문하지 않았던곳일 경우 
		
		if(y<n-1) { //오른쪽칸을 확인한다 
			if(W[x][y+1]==team&&visited[x][y+1]==0) {
			    cnt++;
			    cnt=find(W,visited,team,m,n,x,y+1,cnt);
			    }
			}
		if(x<m-1) { //아래칸을 확인한다 
			if(W[x+1][y]==team&&visited[x+1][y]==0) {
				cnt++;
				cnt=find(W,visited,team,m,n,x+1,y,cnt);	
				}
			}
		if(x>0) { //위에칸을 확인한다 
			if(W[x-1][y]==team&&visited[x-1][y]==0){
				cnt++;
				cnt=find(W,visited,team,m,n,x-1,y,cnt);
				}
			}
		if(y>0) {//왼쪽칸을 확인한
			if(W[x][y-1]==team&&visited[x][y-1]==0) {
				cnt++;
				cnt=find(W,visited,team,m,n,x,y-1,cnt);
			}
		}
		
		return cnt;
	}

}
