import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Baek2491 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        if (N == 1) {
            System.out.println("1");
            return;
        }
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }
        ArrayList<Integer> length = new ArrayList<>();
        int count_large = 1;
        int count_small = 1;

        for (int i = 0; i < N-1; i++) {
            if (numbers[i] <= numbers[i + 1]) {
                count_large++;
                if ((i + 1) == N - 1) {
                    length.add(count_large);
                }
            } else {
                length.add(count_large);
                count_large = 1;
            }
        }
        for (int i = 0; i < N-1; i++) {
            if (numbers[i] >= numbers[i + 1]) {
                count_small++;
                if ((i + 1) == N - 1) {
                    length.add(count_small);
                }
            } else {
                length.add(count_small);
                count_small = 1;
            }
        }
        int max_length = 0;
        for (int i : length) {
            if (i > max_length) {
                max_length = i;
            }
        }
        System.out.println(max_length);
    }
}
