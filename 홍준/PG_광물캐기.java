import java.util.*;
class Solution {
    int MAX=Integer.MAX_VALUE;
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        int weapon_size=Arrays.stream(picks).sum();
        int tired[][]={{1,1,1},{5,1,1},{25,5,1}};
        int[] mineral_value=new int[minerals.length];
        for(int i=0;i<minerals.length;i++){
            switch(minerals[i]){
                case "diamond":
                    mineral_value[i]=0;
                    break;
                case "iron":
                    mineral_value[i]=1;
                    break;
                case "stone":
                    mineral_value[i]=2;     
            }
        }
        for(int i=0;i<3;i++){
            if(picks[i]==0)
                continue;
            picks[i]-=1;
            mine(i,picks,mineral_value,tired,0,0);
            picks[i]+=1;
        }
        answer=MAX;
        return answer;
    }
    
    public void mine(int a,int[] picks,int minerals[],int[][] tired,int current,int sum){
        if(current+5>=minerals.length||Arrays.stream(picks).sum()==0){
            for(int i=current;i<current+5;i++){
                if(i==minerals.length)
                    break;
                sum+=tired[a][minerals[i]];
            }
            MAX=Math.min(MAX,sum);
            return;
        }
        for(int i=current;i<current+5;i++)
            sum+=tired[a][minerals[i]];
        for(int i=0;i<3;i++){
            if(picks[i]==0)
                continue;
            picks[i]-=1;
            mine(i,picks,minerals,tired,current+5,sum);
            picks[i]+=1;
        }
           
    }
}
