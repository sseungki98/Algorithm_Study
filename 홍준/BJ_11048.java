import java.io.*;
import java.util.StringTokenizer;

public class BJ_11048 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        int maze[][]=new int[n][m];
        int dp[][]=new int[n][m];
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<m;j++){
                maze[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        dp[0][0]=maze[0][0];
        for(int i=1;i<m;i++){
            dp[0][i]=dp[0][i-1]+maze[0][i];
        }
        for(int i=1;i<n;i++){
            dp[i][0]=dp[i-1][0]+maze[i][0];
            for(int j=1;j<m;j++){
                dp[i][j]=Math.max(dp[i-1][j],dp[i][j-1])+maze[i][j];
            }
        }
        System.out.println(dp[n-1][m-1]);
        br.close();
    }
}
