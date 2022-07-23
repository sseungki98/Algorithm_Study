import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        int cnt=0;
        ArrayList<Integer> answer=new ArrayList<Integer>();
        int n=progresses.length;
        int[] day=new int[n];
        int[] out=new int[n];
        int j=0;
        for(int i=0;i<n;i++){
            while(progresses[i]<100){
                progresses[i]=speeds[i]+progresses[i];
                j++;
            }
            day[i]=j;
            j=0;
        }
        for(int i=0;i<n;i++){
            if(out[i]==0){
                for(j=i+1;j<n;j++){
                    if(day[i]>=day[j]&&out[j]==0){
                        cnt++;
                        out[j]=1;
                    }
                    if(day[j]>day[i])
                        break;
                }
                out[i]=1;
                cnt++;
            }
            if(cnt!=0)
                answer.add(cnt);
            cnt=0;
        }
        
        
        return answer;
    }
}
