import java.io.*;
import java.util.*;

public class BJ_1590 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int now;
		int N;
		StringTokenizer st=new StringTokenizer(br.readLine());
		N=Integer.parseInt(st.nextToken());
		now=Integer.parseInt(st.nextToken());
		int bus[][]=new int[N][3];
		for(int i=0;i<N;i++) {
			st=new StringTokenizer(br.readLine());
			bus[i][0]=Integer.parseInt(st.nextToken());
			bus[i][1]=Integer.parseInt(st.nextToken());
			bus[i][2]=Integer.parseInt(st.nextToken());
		}
		br.close();
		int min=1000000;
		int time=0;
		for(int i=0;i<N;i++) {
			if(bus[i][0]<now) {
				if(bus[i][0]+bus[i][1]*(bus[i][2]-1)>=now) {
					for(int j=1;j<=bus[i][2];j++) {
						if(bus[i][0]+bus[i][1]*j>=now&&bus[i][0]+bus[i][1]*j<=1000000) {
							time=bus[i][0]+bus[i][1]*j;
						    break;
						    }	
				    }
					if(time>=now) {
						time=time-now;
						if(time<min)
							min=time;
					}
				}
			}
			else if(bus[i][0]>=now) {
				time=bus[i][0]-now;
				if(time<min)
					min=time;
				
			}
		}
		if(min==1000000)
			System.out.println(-1);
		else
			System.out.println(min);
	}

}
