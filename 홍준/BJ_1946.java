import java.io.*;
import java.util.*;

public class BJ_1946 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int test=Integer.parseInt(br.readLine());
		StringTokenizer st;
		int max[]=new int[test];
		int size=0;
		int score[];
		int cnt=0;
		int delete[];
		int a=0;
		int idx=0;
		for(int i=0;i<test;i++) {
			size=Integer.parseInt(br.readLine());
			score=new int[size];
			delete=new int[size];
			for(int j=0;j<size;j++) {
				st=new StringTokenizer(br.readLine());
				idx=Integer.parseInt(st.nextToken())-1;
				score[idx]=Integer.parseInt(st.nextToken());						
			}
			a=score[0];
			for(int j=1;j<size;j++) {
				if(delete[j]==1)
					continue;
				if(score[j]>a&&delete[j]==0) {
					cnt++;
					delete[j]=1;
				}
				else
					a=score[j];
			}
			
			max[i]=(size-cnt);
			cnt=0;
		}
		for(int i=0;i<max.length;i++) {
			System.out.println(max[i]);
		}

	}

}

