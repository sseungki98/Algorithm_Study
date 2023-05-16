import java.io.*;
import java.util.ArrayList;

public class BJ_2302 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        int vip=Integer.parseInt(br.readLine());
        ArrayList<Integer> unable=new ArrayList<>();
        for(int i=0;i<vip;i++)
            unable.add(Integer.parseInt(br.readLine()));
        int cnt=1;
        for(int i=1;i<N;i++){
            cnt+=check(i,unable,N);
        }
        System.out.println(cnt);


    }
    public static int check(int a,ArrayList<Integer> unable,int N){
        if(unable.contains(a+1)||unable.contains(a))
            return 0;
        int cnt=1;
        for(int i=a+2;i<N;i++){
           cnt+=check(i,unable,N);
        }

        return cnt;
    }
}
