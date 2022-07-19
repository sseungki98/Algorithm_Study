import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_16953 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int count = 1;
        for (int i = 0; ; i++) {
            String S_B = Integer.toString(B);
            if (B < A) {
                System.out.println(-1);
                return;
            }
            if (S_B.charAt(S_B.length() - 1) ==  '1') {
                String new_S_B = S_B.substring(0,S_B.length()-1);
                B = Integer.parseInt(new_S_B);
                count++;
                if (B == A) {
                    System.out.println(count);
                    return;
                }
                continue;
            } else if (B % 2 == 0) {
                B = B / 2;
                count++;
                if (B == A) {
                    System.out.println(count);
                    return;
                }
                continue;
            } else{
                System.out.println(-1);
                return;
            }

        }
    }
}
