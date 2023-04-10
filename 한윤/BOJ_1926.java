import java.awt.Point;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	
	static int N, M; // 세로 크기, 가로 크기
	static int picCnt; // 그림의 개수
	static int maxValue; // 가장 넓은 그림의 넓이
	
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, -1, 0, 1 };
	
	static boolean[][] visited;
	static int[][] map;
	
	public static void bfs(int x, int y) {
		
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(x, y));
		visited[x][y] = true;
		
		int size = 1;
		
		while (!q.isEmpty()) {
			Point p = q.poll();
			
			for (int i = 0; i < 4; i++) {
				int nx = p.x + dx[i];
				int ny = p.y + dy[i];
				
				if (nx < 0 || ny < 0 || nx >= N || ny >= M || visited[nx][ny]) continue;
				
				if (map[nx][ny] == 1) {
					size++;
					visited[nx][ny] = true;
					q.add(new Point(nx, ny));
				}
			}
		}
		
		maxValue = Math.max(maxValue, size);
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		
		visited = new boolean[N][M];
		map = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				map[i][j] = sc.nextInt();
			}
		} // end input
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (!visited[i][j] && map[i][j] == 1) {
					picCnt++;
					bfs(i, j);
				}
			}
		}
		
		System.out.println(picCnt);
		System.out.println(maxValue);
	}
}
