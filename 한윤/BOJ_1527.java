package algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1527 {
	
	static Long A, B; // 숫자의 범위
	static int ans; // 정답의 수
	
	static String[] plus = { "4", "7" }; // 이어붙힐 문자열
	
	public static void bfs() {
		
		Queue<String> q = new LinkedList<>();
		q.add("");
		
		while (!q.isEmpty()) {
			String s = q.poll();
			
			for (int i = 0; i < 2; i++) {
				String next = s + plus[i]; // 문자열 이어붙히기
				
				// 문자열의 크기가 더 작은 경우, 이어붙힌 문자열을 queue에 다시 삽입
				if (Long.parseLong(next) < A)
					q.add(next);
				// 문자열의 크기가 더 큰 경우, 무시
				else if (Long.parseLong(next) > B)
					continue;
				// 문자열의 크기가 A와 B의 사이에 있는 경우, count 증가 후, queue에 삽입
				else {
					ans++;
					q.add(next);
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		A = Long.parseLong(st.nextToken());
		B = Long.parseLong(st.nextToken());
		
		// end input
		
		bfs();
		
		System.out.println(ans);
	}
}
