import java.io.*;
import java.util.*;

public class BJ_2217 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int loap[]=new int[N];
		for(int i=0;i<N;i++) {
			loap[i]=Integer.parseInt(br.readLine());
		}
		br.close();
		Arrays.sort(loap);
		int max=0;
		for(int j=0;j<N;j++) {
			if(max<(N-j)*loap[j])
				max=(N-j)*loap[j];
		}
		System.out.println(max);

	}

}
