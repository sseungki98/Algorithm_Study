import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BJ_2644 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        HashMap <Integer,Integer> tree=new HashMap<>();
        int n=Integer.parseInt(br.readLine());
        int[] visit=new int[n+1];
        Arrays.fill(visit,n+1);
        StringTokenizer st=new StringTokenizer(br.readLine());
        int x=Integer.parseInt(st.nextToken());
        int y=Integer.parseInt(st.nextToken());
        visit[x]=0;
        visit[y]=0;
        int relation=Integer.parseInt(br.readLine());
        int tmp1;
        int tmp2;
        int cnt1=0;
        int cnt2=0;
        for(int i=0;i<relation;i++){
            st=new StringTokenizer(br.readLine());
            tmp1=Integer.parseInt(st.nextToken());
            tmp2=Integer.parseInt(st.nextToken());
            tree.put(tmp2,tmp1);
        }
        tmp1=x;
        tmp2=y;
        while(x!=y){
            if(tree.containsKey(x)) {
                x = tree.get(x);
                cnt1++;
                if(visit[x]==n+1){
                    visit[x]=cnt1;
                }
                else{
                    visit[x]+=cnt1;
                    System.out.println(visit[x]);
                    break;
                }

            }
            if(tree.containsKey(y)) {
                y = tree.get(y);
                cnt2++;
                if(visit[y]==n+1){
                   visit[y]=cnt2;
                }
                else{
                    visit[y]+=cnt2;
                    System.out.println(visit[y]);
                    break;
                }
            }
            if(!tree.containsKey(x)&&!tree.containsKey(y)) {
                System.out.println(-1);
                break;
            }
        }


    }
}
