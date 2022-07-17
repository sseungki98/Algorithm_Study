import java.io.*;

public class BJ_3085 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		char W[][]=new char[N][N];
		int side[][]=new int[N*N][2];
		int up[][]=new int[N*N][2];
		String line;
		char before;
		char tmp[]=new char[1];
		int max=1;
		int cnt=1;
		int a=0;
		int b=0;
		for(int i=0;i<N;i++) {
			line=br.readLine();
			before=line.charAt(0);
			W[i][0]=line.charAt(0);
			for(int j=1;j<N;j++) {
				W[i][j]=line.charAt(j);
				if(before!=W[i][j]) {
					side[a][0]=i;
					side[a][1]=j;
					a++;
				}
				before=W[i][j];
			}
		}
		for(int i=0;i<N;i++) {
			for(int j=1;j<N;j++) {
				if(W[j][i]!=W[j-1][i]) {
					up[b][0]=j;
					up[b][1]=i;
					b++;
				}
			}
		}
		br.close();
		for(int i=0;i<a;i++) {
			tmp[0]=W[side[i][0]][side[i][1]];
			W[side[i][0]][side[i][1]]=W[side[i][0]][side[i][1]-1];
			W[side[i][0]][side[i][1]-1]=tmp[0];
			for(int j=0;j<N;j++) {
				for(int k=0;k<N-1;k++) {
				if(W[j][k]==W[j][k+1])
					cnt++;
				else {
					if(cnt>max)
						max=cnt;
					cnt=1;
				}		
				}
				if(cnt>max)
					max=cnt;
				cnt=1;
			}
			if(max==N)
				break;
			for(int j=0;j<N;j++) {
				for(int k=0;k<N-1;k++) {
				if(W[k][j]==W[k+1][j])
					cnt++;
				else {
					if(cnt>max)
						max=cnt;
					cnt=1;
				 }
				}
				if(cnt>max)
					max=cnt;
				cnt=1;
			}
			if(max==N)
				break;
			tmp[0]=W[side[i][0]][side[i][1]];
			W[side[i][0]][side[i][1]]=W[side[i][0]][side[i][1]-1];
			W[side[i][0]][side[i][1]-1]=tmp[0];
		}
		if(max<N) {
		for(int i=0;i<b;i++) {
			tmp[0]=W[up[i][0]][up[i][1]];
			W[up[i][0]][up[i][1]]=W[up[i][0]-1][up[i][1]];
			W[up[i][0]-1][up[i][1]]=tmp[0];
			for(int j=0;j<N;j++) {
				for(int k=0;k<N-1;k++) {
				if(W[j][k]==W[j][k+1])
					cnt++;
				else {
					if(cnt>max)
						max=cnt;
					cnt=1;
				}	
				}
				if(cnt>max)
					max=cnt;
				cnt=1;
			}
			if(max==N)
				break;
			for(int j=0;j<N;j++) {
				for(int k=0;k<N-1;k++) {
				if(W[k][j]==W[k+1][j])
					cnt++;
				else {
					if(cnt>max)
						max=cnt;
					cnt=1;
				}	
				}
				if(cnt>max)
					max=cnt;
				cnt=1;
			}
			if(max==N)
				break;
			tmp[0]=W[up[i][0]][up[i][1]];
			W[up[i][0]][up[i][1]]=W[up[i][0]-1][up[i][1]];
			W[up[i][0]-1][up[i][1]]=tmp[0];
		}
		}
		
		System.out.println(max);
	}

}
