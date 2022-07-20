import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ_15787 {
    static int count = 0; // 통과 가능한 열차의 수
    static int number = 0; // 저장된 train 수
    public static void check(int[] train, int[][] checker) {
        int check_count = 0;
        for (int j = 0; j < number; j++) {
            if (Arrays.equals(train, checker[j]) == true) {
                return;
            }
        }
        checker[number] = Arrays.copyOf(train, train.length);
        number++;
        count++;
        return;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] train = new int[N][20]; // 0 => 탑승 X, 1 => 탑승 O
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            if (command == 1) {
                int train_num = Integer.parseInt(st.nextToken());
                int people = Integer.parseInt(st.nextToken());
                train[train_num - 1][people - 1] = 1;
            }
            if (command == 2) {
                int train_num = Integer.parseInt(st.nextToken());
                int people = Integer.parseInt(st.nextToken());
                train[train_num - 1][people - 1] = 0;
            }
            if (command == 3) {
                int train_num = Integer.parseInt(st.nextToken());
                if (train[train_num - 1][19] == 1) {
                    train[train_num - 1][19] = 0;
                }
                for (int j = 19; j > 0; j--) {
                    if (train[train_num - 1][j-1] == 1) {
                        train[train_num - 1][j] = 1;
                        train[train_num - 1][j-1] = 0;
                    }
                }
            }
            if (command == 4) {
                int train_num = Integer.parseInt(st.nextToken());
                if (train[train_num - 1][0] == 1) {
                    train[train_num - 1][0] = 0;
                }
                for (int j = 0; j < 19; j++) {
                    if (train[train_num - 1][j+1] == 1) {
                        train[train_num - 1][j] = 1;
                        train[train_num - 1][j + 1] = 0;
                    }
                }
            }
        } // M번의 명령 끝
        int[][] checker = new int[N][20];
        for (int i = 0; i < N; i++) {
            Arrays.fill(checker[i],9999);
        }
        for (int i = 0; i < N; i++) {
            check(train[i],checker);
        }
        System.out.println(count);
    }
}
