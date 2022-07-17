import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[] L_Key = {3,0};
        int[] R_Key = {3,2};
        int[] N_Key = {0,0};
        for(int i=0; i<numbers.length; i++){
            if(numbers[i] == 0) {
                numbers[i] = 11;
            }
             if(numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) {
                 answer += "L";
                 L_Key[0] = numbers[i]/3;
                 L_Key[1] = 0;
                 continue;
             } else if(numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) {
                 answer += "R";
                 R_Key[0] = numbers[i]/3-1;
                 R_Key[1] = 2;
                 continue;
             } else if(numbers[i] == 2 || numbers[i] == 5 || numbers[i] == 8 || numbers[i] == 11) {
                 N_Key[0] = numbers[i]/3;
                 N_Key[1] = 1;
             }
            int L_Dist = Math.abs(L_Key[0]-N_Key[0]) + Math.abs(L_Key[1]-N_Key[1]);
            int R_Dist = Math.abs(R_Key[0]-N_Key[0]) + Math.abs(R_Key[1]-N_Key[1]);
            if(L_Dist < R_Dist){
                answer += "L";
                L_Key[0] = N_Key[0];
                L_Key[1] = N_Key[1];
            } else if (L_Dist > R_Dist) {
                answer += "R";
                R_Key[0] = N_Key[0];
                R_Key[1] = N_Key[1];
            } else if (L_Dist == R_Dist) {
                if(hand.equals("right")){
                    answer += "R";
                    R_Key[0] = N_Key[0];
                    R_Key[1] = N_Key[1];
                } else {
                    answer += "L";
                    L_Key[0] = N_Key[0];
                    L_Key[1] = N_Key[1];
                }
            }
        }
        return answer;
    }
}
