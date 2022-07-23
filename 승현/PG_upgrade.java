import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer_array = new ArrayList<Integer>();
        int number = speeds.length;
        int[] need_day = new int[number];
        for(int i=0; i<number; i++) {
            for(int j=0;;j++){
                if(progresses[i] + speeds[i]*j >= 100) {
                    need_day[i] = j;
                    break;
                }
            }
        }
        
        for(int i=0; i<number; i++) {
            if(need_day[i] <= 0) {
                continue;
            }
            int temp = need_day[i];
            for(int j=0; j<number; j++){
                need_day[j] -= temp;
            }
            int count = 0;
            for(int k=i; k<number; k++){
                if(need_day[k] <= 0) {
                    count++;
                    continue;
                } else {
                    break;
                }
            }
            answer_array.add(count);
        }
        int[] answer = new int[answer_array.size()];
        for(int i=0; i<answer_array.size(); i++) {
            answer[i] = answer_array.get(i);
        }
        return answer;
    }
}
