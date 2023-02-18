package day0218;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_15683 {

	static int N; // 사무실의 세로 크기
	static int M; // 사무실의 가로 크기
	static int minValue = Integer.MAX_VALUE; // 사각지대의 최소 크기

	static int[] dx = { 0, -1, 0, 1 }; // 위쪽, 아래쪽 이동
	static int[] dy = { 1, 0, -1, 0 }; // 오른쪽, 왼쪽 이동
	static char[][] graph;
	static List<Point> cctv = new ArrayList<>(); // cctv의 좌표를 담는 리스트
	
	public static void movecctv(char[][] graph, boolean[][] visited, Point p, int idx) {
		Queue<Point> queue = new LinkedList<>();
		queue.add(p);
		
		while(!queue.isEmpty()) {
			Point c = queue.poll();
			int nx = c.x + dx[idx];
			int ny = c.y + dy[idx];
			
			// 범위를 벗어나거나 방문 처리 됐거나 벽을 만난 경우 무시
			if (nx < 0 || ny < 0 || nx >= N || ny >= M || visited[nx][ny] || graph[nx][ny] == '6') continue;
			
			// 0인 경우 #으로 변경하고 방문처리 후 queue에 삽입
			if (graph[nx][ny] == '0') {
				graph[nx][ny] = '#';
				visited[nx][ny] = true;
				queue.add(new Point(nx, ny));
			}
			// 다른 cctv이거나 #인 경우 문자로 변경하지 않고 방문처리 후 queue에 삽입
			else {
				visited[nx][ny] = true;
				queue.add(new Point(nx, ny));
			}
		}
	}

	public static void comb(char[][] graph, int cnt) {
		// 모든 cctv의 경우의 수를 수행한 후 사각지대의 크기를 계산하고 종료
		if (cnt == cctv.size()) {
			int cctv_count = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (graph[i][j] == '0') cctv_count++;
				}
			}
			minValue = Math.min(minValue, cctv_count); // 최솟값 갱신
			return;
		}
		
		Point p = cctv.get(cnt);
		
		char[][] subGraph = new char[N][M]; // graph의 깊은 복사
		
		// cctv 1번부터 5번까지 모든 경우의 수를 수행
		switch (graph[p.x][p.y] - '0') {
		case 1:
			for (int idx = 0; idx < 4; idx++) {
				boolean[][] visited = new boolean[N][M]; // 방문 처리를 위한 배열
				for (int r = 0; r < N; r++) {
					for (int c = 0; c < M; c++) {
						subGraph[r][c] = graph[r][c];
					}
				}
				movecctv(subGraph, visited, p, idx);
				comb(subGraph, cnt + 1); // 재귀				
			}
			break;
		case 2:
			for (int idx = 0; idx < 2; idx++) {
				boolean[][] visited = new boolean[N][M]; // 방문 처리를 위한 배열
				for (int r = 0; r < N; r++) {
					for (int c = 0; c < M; c++) {
						subGraph[r][c] = graph[r][c];
					}
				}
				for (int k = 0; k < 4; k+=2) {
					movecctv(subGraph, visited, p, idx + k);
				}
				comb(subGraph, cnt + 1); // 재귀
			}
			break;
		case 3:
			for (int idx = 0; idx < 4; idx++) {
				boolean[][] visited = new boolean[N][M]; // 방문 처리를 위한 배열
				for (int r = 0; r < N; r++) {
					for (int c = 0; c < M; c++) {
						subGraph[r][c] = graph[r][c];
					}
				}
				for (int k = 0; k < 2; k++) {
					movecctv(subGraph, visited, p, (idx + k) % 4);
				}
				comb(subGraph, cnt + 1); // 재귀
			}
			break;
		case 4:
			for (int idx = 0; idx < 4; idx++) {
				boolean[][] visited = new boolean[N][M]; // 방문 처리를 위한 배열
				for (int r = 0; r < N; r++) {
					for (int c = 0; c < M; c++) {
						subGraph[r][c] = graph[r][c];
					}
				}
				for (int k = 0; k < 3; k++) {
					movecctv(subGraph, visited, p, (idx + k) % 4);
				}
				comb(subGraph, cnt + 1); // 재귀
			}
			break;
		case 5:
			boolean[][] visited = new boolean[N][M]; // 방문 처리를 위한 배열
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					subGraph[r][c] = graph[r][c];
				}
			}
			for (int k = 0; k < 4; k++) movecctv(subGraph, visited, p, k);
			comb(subGraph, cnt + 1); // 재귀
			break;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		graph = new char[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				graph[i][j] = st.nextToken().charAt(0);
				if ('1' <= graph[i][j] && graph[i][j] <= '5') cctv.add(new Point(i, j)); // cctv의 좌표를 저장
			}
		}
		comb(graph, 0);
		System.out.println(minValue);
	}
}
