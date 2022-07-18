import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_1058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[][] friend = new char[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                friend[i][j] = line.charAt(j);
            }
        }
        int min = 0;
        for (int i = 0; i < N; i++) {
            int[] check = new int[N];
            check[i] = 1;
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (friend[i][j] == 'Y') {
                    if (check[j] == 1) {
                        count--;
                    }
                    check[j] = 1;
                    count++;
                    for (int k = 0; k < N; k++) {
                        if (friend[j][k] == 'Y' && check[k] != 1) {
                            count++;
                            check[k] = 1;
                        }
                    }
                }
            }
            if (count > min) {
                min = count;
            }
        }
        System.out.println(min);
    }
}
