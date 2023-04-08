import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class BJ_2667 {
    public static void main(String[] args)throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        ArrayList<Integer> crowd;
        String line;
        ArrayList<ArrayList<Integer>> apart=new ArrayList<>();
        ArrayList<Integer> amount=new ArrayList<>();
        int cnt=0;
        for(int i=0;i<n;i++){
            crowd=new ArrayList<>();
            line= br.readLine();
            for(int j=0;j<n;j++){
                crowd.add(Character.getNumericValue(line.charAt(j)));
            }
            apart.add(crowd);
        }
        for(int i=0;i<n;i++) {
            cnt = 0;
            for (int j = 0; j < n; j++) {
                if (apart.get(i).get(j) == 1)
                    cnt = search(apart, i, j,n);
                if(apart.get(i).get(j) == 0){
                    if(cnt!=0) {
                        amount.add(cnt);
                        cnt=0;
                    }
                }
            }
        }
        System.out.println(amount.size());
        Collections.sort(amount);
        for(int i=0;i< amount.size();i++){
            System.out.println(amount.get(i));
        }
    }

    public static int search(ArrayList<ArrayList<Integer>> apart,int i,int j,int n){
        int cnt=1;
        apart.get(i).set(j,0);
        if(i!=n-1){
            if(apart.get(i+1).get(j)==1){
                cnt+=search(apart,i+1,j,n);
            }
        }
        if(i!=0){
            if(apart.get(i-1).get(j)==1){
                cnt+=search(apart,i-1,j,n);
            }
        }
        if(j!=n-1){
           if(apart.get(i).get(j+1)==1){
               cnt+=search(apart,i,j+1,n);
           }
        }
        if(j!=0){
            if(apart.get(i).get(j-1)==1)
                cnt+=search(apart,i,j-1,n);
        }
        return cnt;
    }
}
