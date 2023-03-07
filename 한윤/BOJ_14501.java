package baekjoon.algorithm.study;

import java.util.Scanner;

public class BOJ_14501 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt(); // 상담 일 수
		
		int[] T = new int[N]; // 상담을 완료하는데 걸리는 기간
		int[] P = new int[N]; // 상담을 했을 때 받을 수 있는 금액
		
		for (int i = 0; i < N; i++) {
			T[i] = sc.nextInt();
			P[i] = sc.nextInt();
		} // end input
		
		int[] dp = new int[N + 1]; // dp 테이블 생성 (N일에서 상담을 완료하는데 걸리는 기간이 1인 경우의 수도 가능하기 때문에 N + 1크기로 생성)
		
		for (int i = 0; i < N; i++) {
			// 상담을 완료하는 시간이 퇴사 이후 시점인 경우 무시
			if (i + T[i] > N) continue;
			
			// 해당 값이 빈 값일 경우를 대비해서, 이전 값과의 최댓값을 저장
			if (i > 0) dp[i] = Math.max(dp[i], dp[i - 1]);
			
			// K일째에서의 최대 수익은 해당 날짜의 수익과, 현재 날짜에서 받을 수 있는 금액을 추가한 금액 중 최대 금액
			dp[i + T[i]] = Math.max(dp[i + T[i]], dp[i] + P[i]);
		}
		
		int ans = 0; // 최대 수익을 저장
		for (int i = 0; i < N + 1; i++) {
			ans = Math.max(ans, dp[i]);
		}
		
		System.out.println(ans);
	}
}
