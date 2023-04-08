import java.io.*;
import java.util.ArrayList;

public class BJ_1660 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> dp=new ArrayList<>();
        ArrayList<Integer> sum=new ArrayList<>();
        ArrayList<Integer> res=new ArrayList<>();
        int n=Integer.parseInt(br.readLine());
        for(int i=0;i<=n;i++)
            res.add(i);
        sum.add(0);
        sum.add(1);
        sum.add(4);
        dp.add(0);
        dp.add(1);
        dp.add(3);
        int idx=2;
        if(n>3){
            while(sum.get(idx)<=n){
                dp.add(dp.get(idx)+dp.get(idx)-dp.get(idx-1)+1);
                sum.add(sum.get(idx)+dp.get(idx+1));
                idx++;
            }
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<sum.size();j++){
                if(sum.get(j)>i)
                    break;
                res.set(i,Math.min(res.get(i),res.get(i-sum.get(j))+1));
            }
        }
        System.out.println(res.get(n));


    }

}
