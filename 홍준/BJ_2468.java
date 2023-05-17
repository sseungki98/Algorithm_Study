import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ_2468 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int min=100;
        int max=0;
        int map[][]=new int[n][n];
        int cnt=1;
        StringTokenizer st;
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<n;j++){
                map[i][j]=Integer.parseInt(st.nextToken());
                min=Math.min(min,map[i][j]);
                max=Math.max(max,map[i][j]);
            }
        }
        for(int i=min;i<max;i++){
            cnt=Math.max(cnt,travel(i,map,n));
        }
        System.out.println(cnt);

    }
    public static int travel(int rain,int[][]map,int n){
        int tmp[][]=new int[n][n];
        for(int i=0;i<n;i++)
            tmp[i]=Arrays.copyOf(map[i],n);
        int cnt=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(tmp[i][j]>rain){
                    cnt++;
                    visit(i,j,tmp,n,rain);
                }
            }
        }

        return cnt;
    }

    public static void visit(int a,int b,int[][] map,int n,int rain){
        if(map[a][b]<=rain)
            return;
        map[a][b]=0;
        if(a<n-1){
            visit(a+1,b,map,n,rain);
        }
        if(a>0){
            visit(a-1,b,map,n,rain);
        }
        if(b<n-1){
            visit(a,b+1,map,n,rain);
        }
        if(b>0){
            visit(a,b-1,map,n,rain);
        }
    }
}
