import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int lights[]=new int[N];
		StringTokenizer st=new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			lights[i]=Integer.parseInt(st.nextToken());
		}
		int inst=Integer.parseInt(br.readLine());
		int sex;
		int num;
		for(int j=0;j<inst;j++) {
			st=new StringTokenizer(br.readLine());
			sex=Integer.parseInt(st.nextToken());
			num=Integer.parseInt(st.nextToken());
			int cnt=1;
			int tmp=0;
			if(sex==1) {
				while(num*cnt<=N) {
					if(lights[num*cnt-1]==0)
						lights[num*cnt-1]=1;
					else
						lights[num*cnt-1]=0;
					cnt++;
				}
			}
			else if(sex==2) {
				while((num-2-tmp)>=0&&num+tmp<N) {
					
				    if(lights[num-tmp-2]==lights[num+tmp]) {
				    	if(lights[num-tmp-2]==0) {
							lights[num-tmp-2]=1;
							lights[num+tmp]=1;
				    	}
						else {
							lights[num-tmp-2]=0;
						    lights[num+tmp]=0;
						}
						tmp++;
					}
				    else
				    	break;
				}
				if(lights[num-1]==0)
					lights[num-1]=1;
				else
					lights[num-1]=0;
			}
		}
		br.close();
		int a=0;
		for(int k=0;k<=(N-1)/20;k++) {
		  if(0<k)
			  System.out.print(System.lineSeparator());
		  while(a<20*(k+1)&&a<N) {
			  if(a==N-1||a==20*(k+1)-1)
				  System.out.print(lights[a]);
			  else
				  System.out.print(lights[a]+" ");
			  a++;
		  
		}
	}
	}

}
