import java.io.*;
import java.util.*;

public class Main{

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int k=Integer.parseInt(st.nextToken());
		ArrayList <Integer> num=new ArrayList<Integer>();
		int cnt=0;
		Integer prime=0;
		int a=0;
		int b=1;
		int remove=0;
		for(int i=2;i<=n;i++)
			num.add(i);
		while(cnt<k) {
			if(find(num.get(a))) {
				b=1;
				prime=num.get(a);
				while(prime*b<=n) {
					if(num.contains(Integer.valueOf(prime*b))) {
						remove=prime*b;
						num.remove(Integer.valueOf(prime*b));
						cnt++;
						if(cnt==k)
							break;
					}
					b++;
				}
				a=0;
			}
			else
				a++;
		}
		System.out.println(remove);
		

	}
	public static boolean find(Integer num) {
		int cnt=2;
		for(int i=2;i<=(num/2);i++) {
			if(num%i==0)
				cnt++;
		}
		if(cnt==2)
			return true;
		else
			return false;
	}

}
