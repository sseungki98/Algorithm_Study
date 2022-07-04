import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_14467 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] cow = new int[11][1];
        for (int i = 0; i < 11; i++) {
            cow[i][0] = 10;
        }
        int count = 0;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int cow_num = Integer.parseInt(st.nextToken());
            int cow_loc = Integer.parseInt(st.nextToken());
            if (cow[cow_num][0] == 10) {
                cow[cow_num][0] = cow_loc;
                continue;
            }
            if (cow[cow_num][0] != 10 && cow[cow_num][0] != cow_loc) {
                cow[cow_num][0] = cow_loc;
                count++;
            }
        }
        System.out.println(count);
    }
}
