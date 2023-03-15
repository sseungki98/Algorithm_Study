import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	static int N; // 집의 수
	
	static PriorityQueue<Integer> pq; // 가장 눈이 많은 집을 고르기 위해 우선순위 큐 사용
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		
		// 높은 숫자가 우선 순위인 int 형 우선순위 큐 선언
		pq = new PriorityQueue<>(Collections.reverseOrder());
		
		for (int i = 0; i < N; i++) {
			pq.add(sc.nextInt());
		} // end input
		
		int endTime = 0; // 집 앞의 눈을 치우는데 걸리는 시간
		
		// pq가 비지 않으면서, 1441분까지 눈 치우기 (둘 중, 하나라도 맞지 않으면 종료)
		while (!pq.isEmpty() && endTime < 1441) {			

			// 두 집에 대해서 수행
			int[] homes = new int[2];
			
			// 먼저, pq가 존재하는 선에서 집 추출
			for (int i = 0; i < 2; i++) {
				if (!pq.isEmpty()) homes[i] = pq.poll();
			}
			
			// pq에서 값이 추출되었다면, 1을 빼고 다시 삽입
			for (int i = 0; i < 2; i++) {
				// 현재 homes의 값이 없거나, 치우면 0인 경우 무시
				if (homes[i] == 0 || homes[i] - 1 == 0) continue;
				
				pq.add(homes[i] - 1);
			}
						
			endTime++; // 시간 증가
		}
		
		if (endTime > 1440) System.out.println(-1);
		else System.out.println(endTime); // 최종 시간 출력
	}
}
