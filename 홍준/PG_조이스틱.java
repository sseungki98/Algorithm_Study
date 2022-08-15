import java.util.*;
class Solution {
    public int solution(String name) {
        ArrayList<Integer> move=new ArrayList<Integer>();
        int answer = 0;
        int cnt=0;
        int size=name.length();
        int min=size;
        int oneside=size;
        int a=0;
        int b=0;
        if('A'!=name.charAt(0)){
            cnt=Math.abs('A'-name.charAt(0));
            if(cnt>13)
                cnt=26-cnt;
            answer=answer+cnt;
        }
        for(int i=1;i<size;i++){
            if('A'==name.charAt(i))
                continue;
            cnt=Math.abs('A'-name.charAt(i));
            move.add(i);
            if(cnt>13)
                cnt=26-cnt;
            answer=answer+cnt;
        }
        if(move.size()!=0){
            oneside=Math.min(move.get(move.size()-1),size-move.get(0));
            if(move.size()>=2){
                for(int i=0;i<move.size()-1;i++){
                    a=Math.min(move.get(i),size-move.get(i+1));
                    b=Math.max(move.get(i),size-move.get(i+1));
                    min=Math.min(min,(2*a+b));
                }
            }
            answer=answer+Math.min(min,oneside);
        }
        return answer;
    }
}
