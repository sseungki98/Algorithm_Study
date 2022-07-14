import java.io.*;
import java.util.*;


public class BJ_2477 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int width=0;//큰사각형의 가로
		int height=0;//큰사각형의 세로
		int full=0;//큰사각형의 넓이
		int minusx=0;//작은사각형의 가로
		int minusy=0;//작은사각형의 세로
		int minus;//작은사각형의 넓이
		int cntx=0;//큰사각형의 가로와 다른 가로를 만낫을때의 카운트
		int cnty=0;//큰사각형의 세로와 다른 세로를 만낫을때의 카운트
		int x=0;//큰사각형 가로의 인덱스
		int y=0;//큰사각형 세로의 인덱스
		int N=Integer.parseInt(br.readLine());//1제곱당 참외갯수
		int in[][]=new int[6][2];//입력
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
		}//최대 사각형의 가로와 세로 인덱스를 입력과 동시에 넣어줌
		br.close();
		full=width*height;
		int j;
		switch(in[x][0]*in[y][0]) {//나올수있는 방향경우의수 북서,서남,동북,남동의 경우로 나눔
		case 3://남동
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
		case 4://동북
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
		case 6://남서
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
		case 8://
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


