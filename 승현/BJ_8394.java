import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_8394 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int[] shake = new int[N];
        if (N == 1) {
            System.out.println(1);
            return;
        } else if (N == 2) {
            System.out.println(2);
            return;
        }
        shake[0] = 1;
        shake[1] = 2;
        for (int i = 2; i < N; i++) {
            shake[i] = shake[i-1]%10 + shake[i-2]%10;
        }
        System.out.println(shake[N-1]%10);
    }
}
