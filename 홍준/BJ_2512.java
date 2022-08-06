import java.io.*;
import java.util.*;

public class BJ_2512 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int country[]=new int[n];
		StringTokenizer st=new StringTokenizer(br.readLine());
		int max=0;
		int min=1;
		int middle=0;
		int cnt=0;
		int sum=0;
		int answer=0;
		for(int i=0;i<n;i++) {
			country[i]=Integer.parseInt(st.nextToken());
			if(max<country[i])
				max=country[i];
			sum=sum+country[i];
		}
		int money=Integer.parseInt(br.readLine());
		br.close();
		if(sum<=money)
			answer=max;
		else {
			while(min<=max) {
				cnt=0;
				middle=(min+max)/2;
				for(int i=0;i<n;i++) {
					if(country[i]<middle) {
						cnt=cnt+country[i];
					}
					else
						cnt=cnt+middle;
				}
				if(cnt<=money) {
					min=middle+1;
					answer=middle;
				}
				else if(cnt>money) {
					max=middle-1;
				}
			}
		}
		System.out.println(answer);		
	}

}
