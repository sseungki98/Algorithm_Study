import java.io.*;
import java.util.*;

public class BJ_16953 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int a=Integer.parseInt(st.nextToken());
		int b=Integer.parseInt(st.nextToken());
		br.close();
		int answer=0;
		int cnt=0;
		while(answer==0) {
			if(a==b) {
				answer=1;
				break;
			}
			if(b==0) {
				answer=-1;
				break;
			}
			
			if(b%2==0) {
				b=b/2;
				cnt++;
			}
			else {
				if((b-1)%10==0) {
					b=(b-1)/10;
					cnt++;
				}
				else
					answer=-1;
			}
		}
		if(answer==-1)
			System.out.println(answer);
		else
			System.out.println(cnt+1);


	}

}
