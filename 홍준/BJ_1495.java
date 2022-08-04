import java.io.*;
import java.util.*;

public class BJ_1495 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int n=Integer.parseInt(st.nextToken());
		int s=Integer.parseInt(st.nextToken());
		int m=Integer.parseInt(st.nextToken());
		ArrayList<ArrayList<Integer>> dp=new ArrayList<>();
		ArrayList<Integer> cas=new ArrayList<Integer>();
		int ans=0;
		int vi[]=new int[n];
		int min[]=Arrays.copyOf(vi, n);
		int len=0;
		Arrays.sort(min);
		st=new StringTokenizer(br.readLine());
		for(int i=0;i<n;i++) {
			vi[i]=Integer.parseInt(st.nextToken());
		}
		if(s+vi[0]>m&&s-vi[0]<0) {
			ans=-1;
		}
		else {
			if(s+vi[0]>m) {
				cas.add(s-vi[0]);
				}
			else if(s-vi[0]<0){
				cas.add(s+vi[0]);
				}
			else {
				cas.add(s-vi[0]);
				cas.add(s+vi[0]);
			}
		}
		dp.add(cas);
		for(int i=1;i<n;i++) {
			len=cas.size();
			cas=new ArrayList<Integer>();
			for(int j=0;j<len;j++) {
				if(!(dp.get(0).get(j)-vi[i]<0&&dp.get(0).get(j)+vi[i]>m)){
					if(dp.get(0).get(j)-vi[i]<0) {
						if(!(cas.contains(dp.get(0).get(j)+vi[i])))
								cas.add(dp.get(0).get(j)+vi[i]);
					}
					else if(dp.get(0).get(j)+vi[i]>m) {
						if(!cas.contains(dp.get(0).get(j)-vi[i]))
							cas.add(dp.get(0).get(j)-vi[i]);
					}
					else {
						if(!cas.contains(dp.get(0).get(j)+vi[i]))
							cas.add(dp.get(0).get(j)+vi[i]);
						if(!cas.contains(dp.get(0).get(j)-vi[i]))
							cas.add(dp.get(0).get(j)-vi[i]);
						}		
					}
				}
			if(cas.size()==0) {
				ans=-1;
				break;
				}
			dp.add(cas);
			dp.remove(0);
			}
		if(ans==-1) {
			System.out.println(ans);
		}
		else {
			Collections.sort(dp.get(0));
			len=dp.get(0).size();
			System.out.println(dp.get(0).get(len-1));
		}
		}

	}

