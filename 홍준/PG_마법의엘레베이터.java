import java.util.*;
class Solution {
    static int answer=Integer.MAX_VALUE;
    public static int solution(int storey) {
        int tmp=storey;
        int limit=1;
        while(tmp/10!=0){
            tmp=tmp/10;
            limit++;
        }
        for(int i=0;i<2;i++){
            caculate(storey,0,i,0,limit+1);
        }
        return answer;
    }
    //dfs로 올라가는경우 내려가는경우
    public static void caculate(int num,int digit,int plus,int cnt,int limit){
        if(limit==0||num==0){
          //최대로 올렷을때 현재층보다 한자리수 위이기때문에 해당칸까지만 허용
            answer=Math.min(answer,cnt);
            return;
        }
        if(plus==0){
            cnt+=(num%(int)Math.pow(10,digit+1)/(int)Math.pow(10,digit));
            num-=(num%(int)Math.pow(10,digit+1)/(int)Math.pow(10,digit));
            for(int i=0;i<2;i++)
                caculate(num,digit+1,i,cnt,limit-1);
        }
        else if(plus==1){
            cnt+=(10-(num%(int)Math.pow(10,digit+1)/(int)Math.pow(10,digit)));
            num-=(num%(int)Math.pow(10,digit+1)/(int)Math.pow(10,digit));
            num+=(int)Math.pow(10,digit+1);
            for(int i=0;i<2;i++)
                caculate(num,digit+1,i,cnt,limit-1);
        }
    }
}
