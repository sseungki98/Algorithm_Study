public class Baek4673 {
    public static void main(String[] args) {
        int[] numbers = new int[10000];
        for (int i = 0; i <10; i++) {
            numbers[2*i] = 2*i;
        }
        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                numbers[(11*i+2*j)] = (11*i + 2*j);
            }
        }
        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 10; k++) {
                    numbers[(101*i + 11*j + 2*k)] = (101*i + 11*j + 2*k);
                }
            }
        }
        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 10; k++) {
                    for (int l = 0; l < 10; l++) {
                        if((1001*i + 101*j + 11*k + 2*l)>10000) {
                            continue;
                        }
                        numbers[(1001*i + 101*j + 11*k + 2*l)] = (1001*i + 101*j + 11*k + 2*l);
                    }
                }
            }
        }
        for (int i = 1; i < 10000; i++) {
            if (numbers[i] == 0) {
                System.out.println(i);
            }
        }
    }
}
