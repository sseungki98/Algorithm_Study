import java.io.*;
import java.util.*;
public class BJ_10815 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int num=Integer.parseInt(br.readLine());
		int card[]=new int[num];
		StringTokenizer st=new StringTokenizer(br.readLine());
		for(int i=0;i<num;i++) {
			card[i]=Integer.parseInt(st.nextToken());
		}
		int N=Integer.parseInt(br.readLine());
		int own[]=new int[N];
		int tmp[]=new int[N];
		int index[]=new int[N];
		int match[]=new int[N];
		st=new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			own[i]=Integer.parseInt(st.nextToken());
		}
		br.close();
		System.arraycopy(own, 0, tmp, 0, N);
		Arrays.sort(tmp);
		Arrays.sort(card);
		int a;
		for(int i=0;i<N;i++) {
			a=Arrays.binarySearch(tmp,own[i]);
			index[a]=i;
		}
		int c=0;
		int b=0;
		while(c<num&&b<N) {
			if(card[c]>tmp[b])
				b++;
			else if(card[c]<tmp[b])
				c++;
			else if(card[c]==tmp[b]) {
				match[index[b]]=1;
				b++;
				c++;
			}
		}
		for(int i=0;i<N;i++) {
			System.out.print(match[i]+" ");
		}
		
		
		

	}

}
