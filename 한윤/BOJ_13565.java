package algo;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_13565 {
	
	static int M, N; // 격자의 크기를 나타내는 변수
	
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, -1, 0, 1 };
	
	static int[][] map; // 2차원 M x N 격자
	
	// 현재 열에 대해 전류가 안쪽으로 침투 가능한 지 체크하는 메서드
	public static boolean isPossible(int row) {
		
		boolean[][] visited = new boolean[M][N]; // 방문 처리 배열
		
		Queue<Point> q = new LinkedList<Point>();
		q.add(new Point(0, row)); // 시작점을 queue에 삽입
		visited[0][row] = true; // 시작점을 방문 처리
		
		// queue에 원소가 존재하는 경우 계속 수행
		while (!q.isEmpty()) {
			Point p = q.poll();
			
			// 전류가 가장 아래쪽에 공급이 된 경우, true를 반환하며 함수 종료
			if (p.x == M - 1) return true;
			
			for (int i = 0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				
				// 범위를 벗어나거나 방문처리 된 경우 무시
				if (nx < 0 || ny < 0 || nx >= M || ny >= N || visited[nx][ny]) continue;
				
				// 다음 칸이 전류가 통하는 칸인 경우, queue에 삽입
				if (map[nx][ny] == 0) {
					q.add(new Point(nx, ny));
					visited[nx][ny] = true;
				}
			}
		}
		
		return false;
	}
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		
		map = new int[M][N];
		
		for (int i = 0; i < M; i++) {
			String str = br.readLine();
			
			for (int j = 0; j < N; j++) {
				map[i][j] = str.charAt(j) - '0';
			}
		} // end input
		
		// 모든 맨 위의 칸에 대해 BFS 수행
		for (int i = 0; i < N; i++) {
			// 전류가 침투할 수 있는 경우, YES를 출력 후 main 함수 강제종료
			if (isPossible(i)) {
				System.out.println("YES");
				return;
			}
		}
		// 위의 for문에서 main 함수가 종료되지 않은 경우, NO를 출력
		System.out.println("NO");
	}
}
