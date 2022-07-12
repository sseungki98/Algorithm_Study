import java.util.Scanner;

public class BJ_1904 {
    public static void fibb(int[] arr, int num) {
        for (int i = 2; i < num; i++) {
            arr[i] = (arr[i-1] + arr[i-2])%15746;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        if (N == 1) {
            System.out.printf("1");
            return;
        } else if (N == 2) {
            System.out.printf("2");
            return;
        }
        int[] arr = new int[N];
        arr[0] = 1;
        arr[1] = 2;
        fibb(arr,N);
        System.out.println(arr[N-1]);
    }
}
