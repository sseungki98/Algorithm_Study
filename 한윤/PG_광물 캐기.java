class Solution {
    
    static int answer; // 정답을 저장하는 변수
    
    // 곡괭이가 남아있는 지 체크하는 메서드 (남아있다면 true, 남아있지 않다면 false)
    public boolean isPossible(int[] picks) {
        
        for (int i = 0; i < picks.length; i++) {
            if (picks[i] != 0) return true;
        }
        
        return false;
    }
    
    // 선택된 곡괭이와 광물을 통해 피로도를 계산해주는 메서드
    public int calc(int num, String mineral) {
        
        if (num == 0) {
            return 1;
        }
        else if (num == 1) {
            if (mineral.equals("diamond")) {
                return 5;
            }
            else {
                return 1;
            }
        }
        else {
            if (mineral.equals("diamond")) {
                return 25;
            }
            else if (mineral.equals("iron")) {
                return 5;
            }
            else {
                return 1;
            }
        }
    }
    
    // 선택 가능한 곡괭이의 가짓수로 모든 경우의 수를 계산하는 메서드
    // num: 선택된 곡괭이의 인덱스
    // cnt: 선택된 곡괭이를 사용한 횟수
    // idx: minerals 배열의 인덱스를 가리키는 변수
    // val: 피로도를 저장하는 변수
    public void subset(int[] picks, int num, int cnt, String[] minerals, int idx, int val) {
        
        // System.out.println(cnt + " " + idx + " " + val);
        
        // 모든 광물을 캔 경우 (첫 번째 종료 조건)
        if (minerals.length == idx) {
            answer = Math.min(answer, val); // 최솟값으로 갱신
            return;
        }
        
        // 곡괭이를 5회 사용한 경우 -> 새로운 곡괭이를 선택
        if (cnt % 5 == 0) {
            
            // 더 사용할 곡괭이가 없는 경우 (두 번째 종료 조건)
            if (!isPossible(picks)) {
                System.out.println(val);
                answer = Math.min(answer, val); // 최솟값으로 갱신
                return;
            }
            
            // (1) 다이아몬드 곡괭이를 사용하는 경우
            if (picks[0] > 0) {
                picks[0]--;
                int plus = calc(0, minerals[idx]);
                subset(picks, 0, cnt + 1, minerals, idx + 1, val + plus);
                picks[0]++;
            }

            // (2) 철 곡괭이를 사용하는 경우
            if (picks[1] > 0) {
                picks[1]--;
                int plus = calc(1, minerals[idx]);
                subset(picks, 1, cnt + 1, minerals, idx + 1, val + plus);
                picks[1]++;
            }

            // (3) 돌 곡괭이를 사용하는 경우
            if (picks[2] > 0) {
                picks[2]--;
                int plus = calc(2, minerals[idx]);
                subset(picks, 2, cnt + 1, minerals, idx + 1, val + plus);
                picks[2]++;
            }
        }
        // 현재 선택된 곡괭이로 광물 채취
        else {
            int plus = calc(num, minerals[idx]);
            subset(picks, num, cnt + 1, minerals, idx + 1, val + plus);
        }
        
    }
    
    // picks: 마인이 갖고 있는 곡괭이의 개수를 나타내는 정수 배열
    // minerals: 광물들의 순서를 나타내는 문자열 배열
    public int solution(int[] picks, String[] minerals) {
        answer = Integer.MAX_VALUE; // 최솟값으로 갱신하기 위해 최댓값을 저장
        
        subset(picks, 0, 0, minerals, 0, 0); // 피로도의 최솟값을 계산하는 메서드 호출
        
        return answer;
    }
}
