import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class BJ_1026 {
    public static int get_min(ArrayList<Integer> arr) {
        int index = 0;
        int min = 101;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < min) {
                index = i;
                min = arr.get(i);
            }
        }
        return arr.remove(index);
    }
    public static int get_max(ArrayList<Integer> arr) {
        int index = 0;
        int max = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > max) {
                index = i;
                max = arr.get(i);
            }
        }
        return arr.remove(index);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> A = new ArrayList<>();
        ArrayList<Integer> B = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            B.add(Integer.parseInt(st.nextToken()));
        }
        int sum = 0;
        for (int i = 0; i < N; i++) {
            int a_obj = get_min(A);
            int b_obj = get_max(B);
            sum += a_obj * b_obj;
        }
        System.out.println(sum);
    }
}
