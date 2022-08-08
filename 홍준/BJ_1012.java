import java.util.*;
import java.io.*;

public class BJ_1012 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int test=Integer.parseInt(br.readLine());
		int x=0;
		int y=0;
		int a=0;
		int b=0;
		int cnt[]=new int[test];
		Integer cabbage[][];
		ArrayList<Integer[]> safe=new ArrayList<Integer[]>();
		for(int i=0;i<test;i++) {
			safe=new ArrayList<Integer[]>();
			StringTokenizer st=new StringTokenizer(br.readLine());
			x=Integer.parseInt(st.nextToken());
			y=Integer.parseInt(st.nextToken());
			a=Integer.parseInt(st.nextToken());
			cabbage=new Integer[a][2];
			for(int j=0;j<a;j++) {
				st=new StringTokenizer(br.readLine());
				cabbage[j][0]=Integer.parseInt(st.nextToken());
				cabbage[j][1]=Integer.parseInt(st.nextToken());	
			}
			b=0;
			while(b<a) {
				if(!safe.contains(cabbage[b])) {
					cnt[i]++;
					find(cabbage,safe,cnt[i],a,b);
				}
				b++;
			}
		}
			
		for(int i=0;i<test;i++) {
			System.out.println(cnt[i]);
		}
		
	}
	public static void find(Integer cabbage[][],ArrayList<Integer[]> safe,int cnt,int a,int b ) {
			for(int j=0;j<a;j++) {
				if(!safe.contains(cabbage[j])) {
					if(Math.abs(cabbage[b][0]-cabbage[j][0])+Math.abs(cabbage[b][1]-cabbage[j][1])==1) {
						safe.add(cabbage[j]);
						find(cabbage,safe,cnt,a,j);
					}
				}
		}
	}

}
