package Algo_study;
import java.io.*;
import java.util.StringTokenizer;

public class Q2491 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		String line=br.readLine();
		br.close();
		StringTokenizer st=new StringTokenizer(line);
		int num[]=new int[N];
		int j=0;
		while(st.hasMoreTokens()) {
			num[j]=Integer.parseInt(st.nextToken());
			j++;
		}
		int cnt=1;
		int status=1;
		int max=2;
		int special=1;
		
		for(int i=0;i<N-1;i++) {
			if(num[i]<num[i+1]) {
				if(status==1) {
					cnt++;
				}
				else {
					if(max<cnt) {
						max=cnt;
					}
					status=1;
					cnt=1;
					i=i-special;
					special=1;
				}
			}
			else if(num[i]>num[i+1]) {
				if(status==0) {
					cnt++;
				}
				else {
					if(max<cnt) {
						max=cnt;
					}
					status=0;
					cnt=1;
					i=i-special;
					special=1;
				}
			}
			else{
				cnt++;
				special++;
			}
		}
		if(max<cnt)
			max=cnt;
		System.out.println(max);
	}
}
