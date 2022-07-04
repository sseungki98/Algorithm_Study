import java.io.*;
import java.util.StringTokenizer;

public class BJ_1018 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String Line=br.readLine();
		StringTokenizer st=new StringTokenizer(Line);
		int M=Integer.parseInt(st.nextToken());
		int N=Integer.parseInt(st.nextToken());
		char R[][]=new char[M][N];
		for(int i=0;i<M;i++) {
			for(int j=0;j<N;j++) {
				if((j+i)%2==1) {
					R[i][j]='W';
				}
				else
					R[i][j]='B';
			}
		}
		char W[][]=new char[M][N];
		int cnt=0;
		for(int i=0;i<M;i++) {
			Line=br.readLine();
			for(int j=0;j<N;j++) {
				W[i][j]=Line.charAt(j);
			}
		}
		br.close();
		int a=M-8;
		int b=N-8;
		int min=64;
		for(int i=0;i<=a;i++) {
			for(int j=0;j<=b;j++) {
				for(int k=0+i;k<8+i;k++) {
					for(int p=0+j;p<8+j;p++) {
						if(W[k][p]!=R[k][p])
							cnt++;
					}
				}
				if((64-cnt)<cnt)
					cnt=64-cnt;
				if(cnt<min)
					min=cnt;
				cnt=0;
			}
		}		    	
		System.out.println(min);
	}
}
