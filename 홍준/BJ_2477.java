import java.io.*;
import java.util.*;


public class BJ_2477 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int width=0;
		int height=0;
		int full=0;
		int minusx=0;
		int minusy=0;
		int minus;
		int cntx=0;
		int cnty=0;
		int x=0;
		int y=0;
		int N=Integer.parseInt(br.readLine());
		int in[][]=new int[6][2];
		for(int i=0;i<6;i++) {
			StringTokenizer st=new StringTokenizer(br.readLine());
			in[i][0]=Integer.parseInt(st.nextToken());
			in[i][1]=Integer.parseInt(st.nextToken());
			if(in[i][0]==1||in[i][0]==2) {
				if(in[i][1]>width) {
					width=in[i][1];
					x=i;
				}
			}
			if(in[i][0]==3||in[i][0]==4) {
				if(in[i][1]>height) {
					height=in[i][1];
					y=i;
				}
			}		
		}
		br.close();
		full=width*height;
		int j;
		switch(in[x][0]*in[y][0]) {
		case 3:
			if(x==5)
				j=0;
			j=x+1;				
			while(minusy==0||minusx==0) {
				if(j>5)
					j=0;
				if(in[j][0]==4) {
					cnty++;
					if(cntx==1)
						minusy=in[j][1];
				}
				else if(in[j][0]==2) {
					cntx++;
					if(cnty==1)
						minusx=in[j][1];
				}
				j++;
			}
			break;
		case 4:
			if(y==5)
				j=0;
			j=y+1;				
			while(minusy==0||minusx==0) {
				if(j>5)
					j=0;
				if(in[j][0]==3) {
					cnty++;
					if(cntx==1)
						minusy=in[j][1];	
				}
				else if(in[j][0]==2) {
					cntx++;
					if(cnty==1)
						minusx=in[j][1];
				}
				j++;
			}
			break;
		case 6:
			if(y==5)
				j=0;
			j=x+1;				
			while(minusy==0||minusx==0) {
				if(j>5)
					j=0;
				if(in[j][0]==4) {
					cnty++;
					if(cntx==1)
						minusy=in[j][1];
				}
				else if(in[j][0]==1) {
					cntx++;
					if(cnty==1)
						minusx=in[j][1];
				}
				j++;
			}
			break;
		case 8:
			if(x==5)
				j=0;
			j=x+1;
			while(minusy==0||minusx==0) {
				if(j>5)
					j=0;
				if(in[j][0]==3) {
					cnty++;
					if(cntx==1)
						minusy=in[j][1];
				}
				else if(in[j][0]==1) {
					cntx++;
					if(cnty==1)
						minusx=in[j][1];
				}
				j++;
			}
			break;
		
		}
		minus=minusx*minusy;
		System.out.println(N*(full-minus));
		
		}
		

	}


