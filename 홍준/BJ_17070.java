import java.io.*;
import java.util.*;

public class BJ_17070 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		StringTokenizer st;
		int W[][]=new int[n][n];
		for(int i=0;i<n;i++) {
			st=new StringTokenizer(br.readLine());
			for(int j=0;j<n;j++)
				W[i][j]=Integer.parseInt(st.nextToken());
		}
		int x=0;
		int y=1;
		int cnt=0;
		x=0;
		y=1;
		cnt=find(W,1,x,y,n,cnt);
		System.out.println(cnt);
	}
	public static int find(int W[][],int dir,int x,int y,int n,int cnt) {
		if(dir==1) {
			if(y+1<n) {
				if(W[x][y+1]!=1) {
					if(x==n-1&&y+1==n-1)
						cnt=cnt+1;
					else
						cnt=find(W,1,x,y+1,n,cnt);
					}
				if(x+1<n) {
						if(W[x+1][y+1]!=1&&W[x+1][y]!=1&&W[x][y+1]!=1) {
							if(x+1==n-1&&y+1==n-1)
								cnt=cnt+1;
							else
								cnt=find(W,3,x+1,y+1,n,cnt);
						}
					}
				}
			return cnt;	
		}
		else if(dir==2) {
			if(x+1<n) {
				if(W[x+1][y]!=1) {
					if(x+1==n-1&&y==n-1)
						cnt=cnt+1;
					else {
						cnt=find(W,2,x+1,y,n,cnt);
					}
				}
				if(y+1<n) {
					if(W[x+1][y+1]!=1&&W[x+1][y]!=1&&W[x][y+1]!=1){
						if(x+1==n-1&&y+1==n-1)
							cnt=cnt+1;
						else {
							cnt=find(W,3,x+1,y+1,n,cnt);
							}
						}
					}
				}
			return cnt;	
			}
		else {
			if(x+1<n&&y+1<n) {
				if(W[x+1][y+1]!=1&&W[x+1][y]!=1&&W[x][y+1]!=1){
					if(x+1==n-1&&y+1==n-1)
						cnt=cnt+1;
					else {
						cnt=find(W,3,x+1,y+1,n,cnt);
						}
					}
				if(W[x+1][y]!=1) {
					if(x+1==n-1&&y==n-1)
						cnt=cnt+1;
					else {
						cnt=find(W,2,x+1,y,n,cnt);
						}
					}
				if(W[x][y+1]!=1) {
					if(x==n-1&&y+1==n-1)
						cnt=cnt+1;
					else {
						cnt=find(W,1,x,y+1,n,cnt);
					}
				}
				
			}
			else if(x+1<n) {
				if(W[x+1][y]!=1) {
					if(x+1==n-1&&y==n-1)
						cnt=cnt+1;
					else {
						cnt=find(W,2,x+1,y,n,cnt);
						}
					}
			}
			else if(y+1<n) {
				if(W[x][y+1]!=1) {
					if(x==n-1&&y+1==n-1)
						cnt=cnt+1;
					else {
						cnt=find(W,1,x,y+1,n,cnt);
					}
				}
			}
			return cnt;
		}
	}
}
