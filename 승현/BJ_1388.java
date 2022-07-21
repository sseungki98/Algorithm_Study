import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_1388 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        char[][] tile = new char[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                tile[i][j] = line.charAt(j);
            }
        }
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (tile[i][j] == '-') {
                    if (j == M - 1) {
                        count++;
                        continue;
                    }
                    if (tile[i][j + 1] == '-') {
                        if (j + 1 == M - 1) {
                            count++;
                            break;
                        }
                        continue;
                    } else {
                        count ++;
                    }
                }
            }
        }
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (tile[j][i] == '|') {
                    if (j == N - 1) {
                        count++;
                        continue;
                    }
                    if (tile[j + 1][i] == '|') {
                        if (j + 1 == N - 1) {
                            count++;
                            break;
                        }
                        continue;
                    } else {
                        count++;
                    }
                }
            }
        }
        System.out.println(count);
    }
}
