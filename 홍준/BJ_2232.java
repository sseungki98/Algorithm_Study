import java.io.*;
import java.util.*;

public class BJ_2232 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int bomb[]=new int[n];
		ArrayList <Integer>explode=new ArrayList<Integer>();
		for(int i=0;i<n;i++) {
			bomb[i]=Integer.parseInt(br.readLine());
		}
		br.close();
		if(n==1)
			explode.add(1);
		else if(n>=2) {
			if(bomb[0]>=bomb[1]) 
				explode.add(1);
			for(int i=1;i<n-1;i++) {
				if(bomb[i]>=bomb[i-1]&&bomb[i]>=bomb[i+1])
					explode.add(i+1);
				}
			if(bomb[n-1]>=bomb[n-2])
				explode.add(n);
			}
		for(int i=0;i<explode.size();i++) {
			System.out.println(explode.get(i));
		}
		}
	}

