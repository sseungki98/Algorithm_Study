import java.io.*;
import java.util.*;

public class BJ_1026 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int a[]=new int[N];
		int b[]=new int[N];
		int tmp[]=new int[N];
		int storea[]=new int[N];
		int storeb[]=new int[N];
		Arrays.fill(storea,-1);
		Arrays.fill(storeb,-1);
		int[] sorta=new int[N];
		int[] sortb=new int[N];
		String line=br.readLine();
		String line2=br.readLine();
		StringTokenizer st=new StringTokenizer(line);
		StringTokenizer st2=new StringTokenizer(line2);
		for(int i=0;i<N;i++) {
			a[i]=Integer.parseInt(st.nextToken());
			b[i]=Integer.parseInt(st2.nextToken());
		}
		br.close();
		for(int x=0;x<N;x++) {
			sorta[x]=a[x];
			sortb[x]=b[x];
		}
		Arrays.sort(sorta);
		Arrays.sort(sortb);
		int j=0,q=0;
		while(j<N) {
			for(int k=0;k<N;k++) {
				if(a[j]==sorta[k]&&storea[k]==-1) {
					storea[k]=j;
					j++;
					break;
				}
			}
		}
		while(q<N) {
			for(int k=0;k<N;k++) {
				if(b[q]==sortb[k]&&storeb[k]==-1) {
					storeb[k]=q;
					q++;
					break;
				}
			}
		}
		for(int i=0;i<N;i++) {
			tmp[storeb[i]]=a[storea[N-1-i]];
		}
		a=tmp;
		int cnt=0;
		for(int i=0;i<N;i++) {
			cnt=cnt+(a[i]*b[i]);
		}
		System.out.println(cnt);
	}

}
