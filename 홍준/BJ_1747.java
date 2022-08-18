import java.io.*;

public class BJ_1747 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		br.close();
		String tmp;
		int answer=0;
		int same=0;
		if(n==1)
			n=2;
		if(n<=3) {
			answer=1;
		}
		while(answer==0) {
			same=0;
			tmp=Integer.toString(n);
			for(int i=0;i<tmp.length()/2;i++) {
				if(tmp.charAt(i)!=tmp.charAt(tmp.length()-1-i)) {
					same=1;
					break;
				}
			}
			if(same==0) {
				for(int i=2;i<=n/2;i++) {
					if(n%i==0) {
						n++;
						break;
					}
					if(i==n/2) {
						answer=1;
					}
				}
			}
			else
				n++;		
		}
		System.out.println(n);
	}
}
