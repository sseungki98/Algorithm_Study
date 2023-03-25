import java.io.*;
import java.util.StringTokenizer;

public class BJ_2961 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int taste[][]=new int[n][2];
        StringTokenizer st;
        int sour=1;
        int bitter=0;
        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            taste[i][0]=Integer.parseInt(st.nextToken());
            taste[i][1]=Integer.parseInt(st.nextToken());
        }
        int min=999999999;
        for(int i=0;i<n;i++){
            min=Math.min(min,cook(i,taste,sour,bitter,n));
        }
        System.out.println(min);

    }

    public static int cook(int i,int [][]taste,int sour,int bitter,int n){
        sour=sour*taste[i][0];
        bitter=bitter+taste[i][1];
        int min=Math.abs(sour-bitter);
        for(int j=i+1;j<n;j++){
            min=Math.min(min,cook(j,taste,sour,bitter,n));
        }
        return min;
    }
}
