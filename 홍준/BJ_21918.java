import java.io.*;
import java.util.*;

public class BJ_21918 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int inst,x,y;
		int num,inum;
		String Line=br.readLine();
		StringTokenizer st=new StringTokenizer(Line);
		num=Integer.parseInt(st.nextToken());
		inum=Integer.parseInt(st.nextToken());
		int light[]=new int[num];
		Line=br.readLine();
		st=new StringTokenizer(Line);
		for(int i=0;i<num;i++) {
			light[i]=Integer.parseInt(st.nextToken());
		}
		for(int j=0;j<inum;j++) {
			Line=br.readLine();
			st=new StringTokenizer(Line);
			inst=Integer.parseInt(st.nextToken());
			x=Integer.parseInt(st.nextToken());
			y=Integer.parseInt(st.nextToken());
			switch(inst) {
			case 1:
				light[x-1]=y;
				break;
			case 2:
				for(int i=x-1;i<=y-1;i++) {
					if(light[i]==0)
						light[i]=1;
					else
						light[i]=0;
				}
				break;
			case 3:
				for(int i=x-1;i<=y-1;i++) {
					light[i]=0;
				}
				break;
			case 4:
				for(int i=x-1;i<=y-1;i++) {
					light[i]=1;
				}
				break;				
			}
		}
		br.close();
		for(int a=0;a<num;a++)
			System.out.print(light[a]+" ");				
	}

}
