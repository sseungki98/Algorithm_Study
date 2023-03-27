import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BJ_1124 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        ArrayList<Integer> primenumber=new ArrayList<>();
        int a=Integer.parseInt(st.nextToken());
        int b=Integer.parseInt(st.nextToken());
        int cnt=0;
        int tmp=0;
        for(int i=2;i<=b;i++)
            prime(i,primenumber);
        for(int i=a;i<=b;i++){
            tmp=divide(i,primenumber);
            if(primenumber.contains(tmp))
                cnt++;
        }
        System.out.println(cnt);

    }
    public static int divide(int n, ArrayList<Integer> primenumber){
        int i=0;
        int cnt=0;
        int size=primenumber.size();
        while(i<size&&primenumber.get(i)<=n){
            while(n% primenumber.get(i)==0) {
                n = n /primenumber.get(i) ;
                cnt++;
            }
            i++;
        }
        return cnt;
    }
    public static void prime(int n,ArrayList<Integer> primenumber){
        if(n==1)
            return;
        for(int i=2;i<n;i++){
            if(n%i==0)
                return;
        }
        primenumber.add(n);
    }
}
