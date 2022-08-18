import java.io.*;
import java.util.*;

public class BJ_1461 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		int place=0;
		int cnt=0;
		ArrayList<Integer> left=new ArrayList<Integer>();
		ArrayList<Integer> right=new ArrayList<Integer>();
		ArrayList<Integer> walk=new ArrayList<Integer>();
		st=new StringTokenizer(br.readLine());
		for(int i=0;i<n;i++) {
			place=Integer.parseInt(st.nextToken());
			if(place<0)
				left.add(place);
			else if(place>0)
				right.add(place);
		}
		Collections.sort(left);
		Collections.sort(right,Collections.reverseOrder());
		while(left.size()!=0||right.size()!=0) {
			if(left.size()>=m) {
				walk.add(Math.abs(left.get(0)));
				for(int i=0;i<m;i++)
					left.remove(0);
			}
			else if(0<left.size()&&left.size()<m) {
				walk.add(Math.abs(left.get(0)));
				left.clear();
			}
			if(right.size()>=m) {
				walk.add(right.get(0));
				for(int i=0;i<m;i++)
					right.remove(0);
			}
			else if(0<right.size()&&right.size()<m) {
				walk.add(right.get(0));
				right.clear();
			}		
		}
		Collections.sort(walk,Collections.reverseOrder());
		cnt=cnt+walk.get(0);
		walk.remove(0);
		while(walk.size()>0) {
			cnt=cnt+2*walk.get(0);
			walk.remove(0);
		}
		System.out.println(cnt);
	}

}
