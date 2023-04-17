import java.io.*;
import java.util.*;
public class BJ_1926 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        PriorityQueue <Integer>count=new PriorityQueue<>(Collections.reverseOrder());
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        int draw[][]=new int[n][m];
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<m;j++){
                draw[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(draw[i][j]==0)
                    continue;
                else
                    count.add(width(draw,i,j,n,m));
            }
        }
        System.out.println(count.size());
        if(count.size()==0)
            System.out.println(0);
        else
            System.out.println(count.poll());

    }
    public static int width(int draw[][],int i,int j, int n, int m){
        int cnt=1;
        draw[i][j]=0;
        if(i!=n-1){
            if(draw[i+1][j]==1)
                cnt+=width(draw,i+1,j,n,m);
        }
        if(i!=0){
            if(draw[i-1][j]==1)
                cnt+=width(draw,i-1,j,n,m);
        }
        if(j!=m-1){
            if(draw[i][j+1]==1)
                cnt+=width(draw,i,j+1,n,m);

        }
        if(j!=0){
            if(draw[i][j-1]==1)
                cnt+=width(draw,i,j-1,n,m);
        }
        return cnt;
    }
}
