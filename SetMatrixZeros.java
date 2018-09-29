class Solution {
    public void setZeroes(int[][] matrix) {
        int M = matrix.length;
        if (M == 0) {
            return;
        }
        int N = matrix[0].length;
        boolean hasZero1row = false;
        for (int i = 0; i < M; i++) {
            if (matrix[i][0] == 0) {
                hasZero1row = true;
                break;
            }
        }
        
        for (int j = 1; j < N; j++) {
            boolean hasZero = false;
            for (int i = 0; i < M; i++) {
                if(matrix[i][j] == 0) {
                    hasZero = true;
                    matrix[i][0] = 0;
                }
            }
            if (hasZero) {
                for (int i = 0; i < M; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        for (int i = 0; i < M; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 1; j < N; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        if (hasZero1row) {
            for (int i = 0; i < M; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
