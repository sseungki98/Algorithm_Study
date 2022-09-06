import java.io.*;
import java.util.*;

public class BJ_11000 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int lec[][]=new int[n][2];
		StringTokenizer st;
		int cnt=0;
		PriorityQueue<Integer> fin=new PriorityQueue<Integer>();
		for(int i=0;i<n;i++) {
			st=new StringTokenizer(br.readLine());
			lec[i][0]=Integer.parseInt(st.nextToken());
			lec[i][1]=Integer.parseInt(st.nextToken());
		}
		br.close();
		Arrays.sort(lec,new Comparator<int[]>() {
			public int compare(int o1[],int o2[]) {
				if(o1[0]==o2[0])
					return o1[1]-o2[1];
				return o1[0]-o2[0];
			}
		});
		while(cnt<n) {
			if(fin.isEmpty()) {
				fin.add(lec[cnt][1]);
				cnt++;
			}
			else {
				if(fin.peek()<=lec[cnt][0])
					fin.poll();
				fin.add(lec[cnt][1]);
				cnt++;
			}
		}
		System.out.println(fin.size());
	}
}

