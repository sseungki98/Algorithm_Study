import java.io.*;
import java.util.*;


public class BJ_1388 {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int y=Integer.parseInt(st.nextToken());
		int x=Integer.parseInt(st.nextToken());
		char tile[][]=new char[y][x];
		int cnt=0;
		String line;
		for(int i=0;i<y;i++) {
			line=br.readLine();
			for(int j=0;j<x;j++) {
				tile[i][j]=line.charAt(j);
				if(tile[i][j]=='-') {
					if(j>0) {
						if(tile[i][j]!=tile[i][j-1])
							cnt++;
					}
					else
						cnt++;
				}
				
				else if(tile[i][j]=='|') {
					if(i>0) {
						if(tile[i][j]!=tile[i-1][j])
							cnt++;
					}
					else
						cnt++;
				}
			}
		}
		br.close();
		System.out.println(cnt);
	}

}
