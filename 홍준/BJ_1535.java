import java.io.*;
import java.util.*;
public class BJ_1535 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		int hp=100;
		int happiness=0;
		int max=0;
		ArrayList <Integer> happy=new ArrayList<Integer>();
		ArrayList <Integer>damage=new ArrayList<Integer>();
		ArrayList <Integer>visit;
		StringTokenizer st=new StringTokenizer(br.readLine());
		StringTokenizer st2=new StringTokenizer(br.readLine());
		for(int i=0;i<n;i++) {
			damage.add(Integer.parseInt(st.nextToken()));
			happy.add(Integer.parseInt(st2.nextToken()));
		}
		for(int i=0;i<n;i++) {
			visit=new ArrayList<Integer>();
			happiness=0;
			happiness=greet(n,hp,happiness,damage,happy,i);
			if(happiness>max)
				max=happiness;
		}
		System.out.println(max);
		
		

	}
	public static int greet(int n,int hp,int happiness,ArrayList<Integer> damage,ArrayList<Integer> happy,int i) {
		if(hp-damage.get(i)<=0)
			return happiness;
		hp=hp-damage.get(i);
		happiness=happiness+happy.get(i);
		int og=happiness;
		int max=happiness;
		for(int j=i+1;j<n;j++) {
			happiness=og;
			happiness=greet(n,hp,happiness,damage,happy,j);
			if(happiness>max)
				max=happiness;
		}
		return max;
	}

}
