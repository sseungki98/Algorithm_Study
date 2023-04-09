import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
	
	static int N;
	static int ans;
	static int cnt;
	
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, -1, 0, 1 };
	
	static int[][] map;
	
	public static int dfs(int x, int y) {
		map[x][y] = 0; // 방문 처리
		cnt++;
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if (nx < 0 || ny < 0 || nx >= N || ny >= N || map[nx][ny] == 0) continue;
			
			dfs(nx, ny);
		}
		
		return 1;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<Integer> homes = new ArrayList<Integer>();
		
		N = Integer.parseInt(br.readLine());
		
		map = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < N; j++) {
				map[i][j] = tmp.charAt(j) - '0';
			}
		} // 입력 종료
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cnt = 0;
				if (map[i][j] == 1) {
					ans += dfs(i, j);
					homes.add(cnt);
				}
			}
		}
		
		Collections.sort(homes);
		
		System.out.println(ans);
		for (int i = 0; i < homes.size(); i++) {
			System.out.println(homes.get(i));
		}
	}
}
