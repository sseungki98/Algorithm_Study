import java.io.*;
import java.util.*;

public class BJ_15724 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		int W[][]=new int[n][m];
		int S[][]=new int [n][m];
		for(int i=0;i<n;i++) {
			st=new StringTokenizer(br.readLine());
			for(int j=0;j<m;j++) {
				W[i][j]=Integer.parseInt(st.nextToken());
				if(j==0) {
					if(i==0) {
						S[i][j]=W[i][j];
					}
					else {
						S[i][j]=S[i-1][m-1]+W[i][j];
					}
				}
				else {
					S[i][j]=S[i][j-1]+W[i][j];
				}
			}
		}
		int cnt=Integer.parseInt(br.readLine());
		int sum=0;
		int fromx=0;
		int fromy=0;
		int tox=0;
		int toy=0;
		for(int i=0;i<cnt;i++) {
			sum=0;
			st=new StringTokenizer(br.readLine());
			fromx=Integer.parseInt(st.nextToken())-1;
			fromy=Integer.parseInt(st.nextToken())-1;
			tox=Integer.parseInt(st.nextToken())-1;
			toy=Integer.parseInt(st.nextToken())-1;
			if((toy-fromy)==(m-1)) {
				if(fromx==0)
					sum=S[tox][m-1];
				else {
					sum=S[tox][m-1]-S[fromx-1][m-1];
				}
			}
			else {
				if(fromy==0) {
					for(int j=fromx;j<=tox;j++) {
						if(j==0)
							sum=sum+S[j][toy];
						else
							sum=sum+S[j][toy]-S[j-1][m-1];
						}	
					}
				else {
					for(int j=fromx;j<=tox;j++) {
							sum=sum+S[j][toy]-S[j][fromy-1];
						}
					}
				}
			System.out.println(sum);
			}
		}

}
