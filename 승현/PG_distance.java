import java.io.IOException;

public class PG_distance {
    public static int search(char[][] places, int i, int j) {
        if(i-1 >= 0) {
            if (places[i - 1][j] == 'P') {
                return 0;
            }
            if (places[i - 1][j] == 'O') {
                if (((i-2)>=0 && places[i - 2][j] == 'P')|| (j-1>=0 && places[i - 1][j - 1] == 'P') || (j+1<=4 && places[i - 1][j + 1] == 'P')) {
                    return 0;
                }
            }
        }
        if(i+1 <=4) {
            if (places[i + 1][j] == 'P') {
                return 0;
            }
            if (places[i + 1][j] == 'O') {
                if ((i+2<=4 && places[i + 2][j] == 'P') || (j-1>=0 && places[i + 1][j - 1] == 'P') || (j+1<=4 && places[i + 1][j + 1] == 'P')) {
                    return 0;
                }
            }
        }
        if(j+1<=4) {
            if (places[i][j + 1] == 'P') {
                return 0;
            }
            if (places[i][j + 1] == 'O') {
                if ((j+2<=4 && places[i][j + 2] == 'P') || (i+1<=4 && places[i + 1][j + 1] == 'P') || (i-1>=0 && places[i - 1][j + 1] == 'P')) {
                    return 0;
                }
            }
        }
        if(j-1>=4) {
            if (places[i][j - 1] == 'P') {
                return 0;
            }
            if (places[i][j - 1] == 'O') {
                if ((j-2>=0 && places[i][j - 2] == 'P') || (i+1<=4 && places[i + 1][j - 1] == 'P') || (i-1 >=0 && places[i - 1][j - 1] == 'P')) {
                    return 0;
                }
            }
        }
        return 1;
    }

    public static void main(String[] args) throws IOException {
        String[][] places = {
                {"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
                {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
                {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
                {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
                {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"}
        };
        char[][] wait_places = new char[5][5];
        for(int k=0; k<5; k++) {
            int count = 0;
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    wait_places[i][j] = places[k][i].charAt(j);
                }
            }
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (wait_places[i][j] == 'P') {
                        if (search(wait_places, i, j) == 0) {
                            count++;
                        }
                    }
                }
            }
            if (count == 0) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }

        }
    }

