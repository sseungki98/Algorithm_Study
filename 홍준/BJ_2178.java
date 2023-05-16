import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ_2178 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int map[][]=new int[N+1][M+1];
        String line;
        for(int i=1;i<=N;i++){
            line=br.readLine();
            for(int j=1;j<=M;j++){
                if(Character.getNumericValue(line.charAt(j - 1))!=0)
                    map[i][j]=N*M;
                else
                    map[i][j]=0;
            }
        }
        travel(1,1,map,0,N,M);
        System.out.println(map[N][M]);

    }
    public static void travel(int a,int b,int[][]map,int step,int N,int M){
        if(map[a][b]<=step+1)
            return;
        else {
            step = step + 1;
            map[a][b]=step;
        }

        if(a+1<=N)
            travel(a+1,b,map,step,N,M);
        if(a-1>=1)
            travel(a-1,b,map,step,N,M);
        if(b+1<=M)
            travel(a,b+1,map,step,N,M);
        if(b-1>=1)
            travel(a,b-1,map,step,N,M);

    }
}
