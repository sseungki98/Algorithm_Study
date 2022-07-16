import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_20365 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[] blog = new char[N];
        String input = br.readLine();
        for (int i = 0; i < N; i++) {
            blog[i] = input.charAt(i);
        }
        int B_count = 0;
        int R_count = 0;
        for (int i = 0; i < N; i++) {
            if (blog[i] == 'B') {
                if (i + 1 == N) {
                    B_count++;
                    break;
                }
                if (blog[i] != blog[i + 1]) {
                    B_count++;
                }
            } else if (blog[i] == 'R') {
                if (i + 1 == N) {
                    R_count++;
                    break;
                }
                if (blog[i] != blog[i + 1]) {
                    R_count++;
                }
            }
        }
        if (B_count > R_count) {
            System.out.println(1 + R_count);
        } else {
            System.out.println(1 + B_count);
        }
    }
}
