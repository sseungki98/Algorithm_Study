import java.io.*;

public class BJ_20365 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		char color[]=new char[N];
		int bchange=0;
		int rchange=0;
		String line=br.readLine();
		color[0]=line.charAt(0);
		
		for(int i=1;i<N;i++){
			color[i]=line.charAt(i);
			if(color[i]=='B') {
				if(color[i]!=(color[i-1])) {
					bchange++;
				}
			}
			else if(color[i]=='R') {
				if(color[i]!=(color[i-1])) {
					rchange++;
				}
			}
		}
		if(bchange>rchange) {
			System.out.println(bchange+1);
		}
		else
			System.out.println(rchange+1);
	}

}
