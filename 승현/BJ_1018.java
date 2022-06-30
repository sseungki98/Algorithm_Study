import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_1018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());
        String[][] chess = new String[X][Y];
        for (int i = 0; i < X; i++) {
            String line = br.readLine();
            for (int j = 0; j < Y; j++) {
                chess[i][j] = Character.toString(line.charAt(j));
            }
        }
        int count = 0;
        int count_2 = 1;
        int min = 9999;
        for (int i = 0; i < X - 7; i++) {
            for (int j = 0; j < Y - 7; j++) {
                if (chess[i][j].equals("B")) {
                    int k = 0;
                    int l = 0;
                    while (true) {
                        if (k == 8) {
                            k = 0;
                            l = l + 1;
                            if (l == 8) {
                                break;
                            }
                        }
                        if (l % 2 == 0) {
                            if ((k % 2 == 0)) {
                                if (chess[i + k][j + l].equals("B")) {
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            } else {
                                if (chess[i + k][j + l].equals("W")) {
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            }
                        } else {
                            if ((k % 2 == 0)) {
                                if (chess[i + k][j + l].equals("W")) { // i = 2, k = 8
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            } else {
                                if (chess[i + k][j + l].equals("B")) {
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            }
                        }
                    }
                    chess[i][j] = "W";
                    if (chess[i][j].equals("W")) {
                        int k_2 = 0;
                        int l_2 = 0;
                        while (true) {
                            if (k_2 == 8) {
                                k_2 = 0;
                                l_2 = l_2 + 1;
                                if (l_2 == 8) {
                                    break;
                                }
                            }
                            if (l_2 % 2 == 0) {
                                if ((k_2 % 2 == 0)) { //홀수번째 칸
                                    if (chess[i + k_2][j + l_2].equals("W")) {
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                } else { //짝수번째 칸
                                    if (chess[i + k_2][j + l_2].equals("B")) {
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                }
                            } else {
                                if ((k_2 % 2 == 0)) { //홀수번째 칸
                                    if (chess[i + k_2][j + l_2].equals("B")) {
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                } else { //짝수번째 칸
                                    if (chess[i + k_2][j + l_2].equals("W")) {
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                }
                            }
                        }
                    }
                    if (count_2 < count) {
                        count = count_2;
                    }
                    chess[i][j] = "B";
                }




                if (chess[i][j].equals("W")) {
                    int k = 0;
                    int l = 0;
                    while (true) {
                        if (k == 8) {
                            k = 0;
                            l = l + 1;
                            if (l == 8) {
                                break;
                            }
                        }
                        if (l % 2 == 0) {
                            if ((k % 2 == 0)) { //홀수번째 칸
                                if (chess[i + k][j + l].equals("W")) {
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            } else { //짝수번째 칸
                                if (chess[i + k][j + l].equals("B")) {
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            }
                        } else {
                            if ((k % 2 == 0)) { //홀수번째 칸
                                if (chess[i + k][j + l].equals("B")) {
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            } else { //짝수번째 칸
                                if (chess[i + k][j + l].equals("W")) {
                                    k++;
                                    continue;
                                } else {
                                    count++;
                                    k++;
                                }
                            }
                        }
                    }
                    chess[i][j] = "B";
                    if (chess[i][j].equals("B")) {
                        int k_2 = 0;
                        int l_2 = 0;
                        while (true) {
                            if (k_2 == 8) {
                                k_2 = 0;
                                l_2 = l_2 + 1;
                                if (l_2 == 8) {
                                    break;
                                }
                            }
                            if (l_2 % 2 == 0) {
                                if ((k_2 % 2 == 0)) {
                                    if (chess[i + k_2][j + l_2].equals("B")) {
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                } else {
                                    if (chess[i + k_2][j + l_2].equals("W")) {
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                }
                            } else {
                                if ((k_2 % 2 == 0)) {
                                    if (chess[i + k_2][j + l_2].equals("W")) { // i = 2, k = 8
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                } else {
                                    if (chess[i + k_2][j + l_2].equals("B")) {
                                        k_2++;
                                        continue;
                                    } else {
                                        count_2++;
                                        k_2++;
                                    }
                                }
                            }
                        }
                    }
                    if (count_2 < count) {
                        count = count_2;
                    }
                    chess[i][j] = "W";
                }
                if (min > count) {
                    min = count;
                }
                    count = 0;
                    count_2 = 1;
                }

            }
        System.out.println(min);
        }

    }

