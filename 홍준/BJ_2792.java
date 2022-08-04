import java.io.*;
import java.util.*;

public class BJ_2792 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int num=Integer.parseInt(st.nextToken());
		int jam[]=new int[num];
		int middle=0;
		int a=0;
		int ans=0;
		int min=1;
		int max=0;
		for(int i=0;i<num;i++) {
			jam[i]=Integer.parseInt(br.readLine());
			if(jam[i]>max)
				max=jam[i];
		}
		br.close();
		while(min<=max) {
			a=0;
			middle=(min+max)/2;
			for(int i=0;i<num;i++) {
				if(jam[i]%middle==0)
					a=a+(jam[i]/middle);
				else
					a=a+(jam[i]/middle)+1;
			}
			if(a>n)
				min=middle+1;
			else {
				max=middle-1;
				ans=middle;
			}
				
		}
		System.out.println(ans);
	}

}
