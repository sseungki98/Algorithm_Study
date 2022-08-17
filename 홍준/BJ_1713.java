import java.io.*;
import java.util.*;

public class BJ_1713 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int recom=Integer.parseInt(br.readLine());
		int idx=0;
		Integer a;
		ArrayList<Integer> frame=new ArrayList<Integer>();
		ArrayList<Integer> cnt=new ArrayList<Integer>();
		StringTokenizer st=new StringTokenizer(br.readLine());
		br.close();
		for(int i=0;i<recom;i++) {
			a=Integer.valueOf(st.nextToken());
			if(frame.contains(a)) {
				idx=frame.indexOf(a);
				cnt.set(idx,cnt.get(idx)+1);
			}
			else {
				if(frame.size()<n) {
					frame.add(a);
					cnt.add(1);
				}
				else {
					idx=cnt.indexOf(Collections.min(cnt));
					frame.remove(idx);
					cnt.remove(idx);
					frame.add(a);
					cnt.add(1);
				}
			}
		}
			
		Collections.sort(frame);
		for(int i=0;i<frame.size();i++) {
			System.out.print(frame.get(i)+" ");
		}

	}

}
