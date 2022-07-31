import java.io.*;
import java.util.*;

public class BJ_16935 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		int R=Integer.parseInt(st.nextToken());
		int inst;
		int y;
		int x;
		int W[][]=new int[n][m];
		int D[][]=new int[n][m];
		int a[]=new int[n];
		int b=0;
		for(int i=0;i<n;i++) {
			st=new StringTokenizer(br.readLine());
			for(int j=0;j<m;j++) {
				W[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		st=new StringTokenizer(br.readLine());
		br.close();
		for(int i=0;i<R;i++) {
			inst=Integer.parseInt(st.nextToken());
			y=W.length;
			x=W[0].length;
			switch(inst) {
			case 1:
                D=Arrays.copyOf(D,y);
				for(int j=0;j<y;j++) {
					D[j]=Arrays.copyOf(W[y-1-j],x);
				}
				W=D;
				break;
			case 2:
				a=Arrays.copyOf(a,x);
                D=Arrays.copyOf(D,y);
				for(int j=0;j<y;j++) {
					for(int k=0;k<x;k++) {
						a[k]=W[j][x-1-k];
					}
					D[j]=Arrays.copyOf(a,x);
				}
				W=D;
				break;
			case 3:
				a=Arrays.copyOf(a,y);
                D=Arrays.copyOf(D,x);
				for(int j=0;j<x;j++) {
					for(int k=y-1;k>=0;k--) {
						a[b]=W[k][j];
						b++;
					}
					b=0;
					D[j]=Arrays.copyOf(a,y);
				}
				W=D;
				break;
			case 4:
				a=Arrays.copyOf(a,y);
				D=Arrays.copyOf(D,x);
				for(int j=0;j<x;j++) {
					for(int k=0;k<y;k++) {
						a[b]=W[k][j];
						b++;
					}
					b=0;
					D[x-j-1]=Arrays.copyOf(a,y);
				}
				W=D;
				break;
			case 5:
				D=Arrays.copyOf(D,y);
				for(int k=0;k<y;k++) {
					D[k]=Arrays.copyOf(D[0],x);
				}
				for(int k=0;k<y/2;k++) {
					System.arraycopy(W[k],0,D[k],x/2,x/2);
					System.arraycopy(W[k],x/2,D[k+(y/2)],x/2,x/2);
					}
				for(int k=y/2;k<y;k++) {
					System.arraycopy(W[k],0,D[k-(y/2)],0,x/2);
					System.arraycopy(W[k],x/2,D[k],0,x/2);
					}
				W=D;
				break;
			case 6:
				D=Arrays.copyOf(D,y);
				for(int k=0;k<y;k++) {
					D[k]=Arrays.copyOf(D[0],x);
				}
				for(int k=0;k<y/2;k++) {
					System.arraycopy(W[k],0,D[k+(y/2)],0,x/2);
					System.arraycopy(W[k],x/2,D[k],0,x/2);
				}
				for(int k=y/2;k<y;k++) {
					System.arraycopy(W[k],0,D[k],x/2,x/2);
					System.arraycopy(W[k],x/2,D[k-(y/2)],x/2,x/2);
				}
				W=D;
				break;			
				}
			}
		y=W.length;
		x=W[0].length;
		for(int i=0;i<y;i++) {
			for(int j=0;j<x;j++) {
				System.out.print(W[i][j]+" ");
			}
			System.out.println("");
		}
		}
	}

