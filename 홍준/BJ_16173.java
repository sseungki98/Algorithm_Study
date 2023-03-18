import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BJ_16173 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        StringTokenizer st;
        int tile[][]=new int[n][n];
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<n;j++)
                tile[i][j]=Integer.parseInt(st.nextToken());
        }
        jump(tile[0][0],n,2*(n-1),0,0,tile);
        if(tile[n-1][n-1]==101) {
            System.out.println("HaruHaru");
        }
        else
            System.out.println("Hing");

    }

    public static void jump(int life,int n,int distance,int i,int j,int tile[][]){
        if(i+life>=n&&j+life>=n)
            return;
        if(life>distance) {
            tile[i][j]=101; 
            return;
        }
        if(life==distance){
            tile[n-1][n-1]=101;
            return;
        }
        if(life>0){
            if(i+life<n) {
                jump(tile[i+life][j], n, distance - life, i + life, j, tile);
            }
            if(j+life<n) {
                jump(tile[i][j+life], n, distance - life, i, j + life, tile);
            }
        }
    }
}
