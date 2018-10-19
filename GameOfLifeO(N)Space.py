class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def interactCell(x, y, board):
            M = len(board)
            N = len(board[0])
            n_live, n_dead = 0, 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and i < M and j >= 0 and j < N:
                        if x == i and y == j:
                            continue
                        if board[i][j] == 0:
                            n_dead += 1
                        else:
                            n_live += 1
            
            if board[x][y] == 0:
                if n_live == 3:
                    return 1
            else:
                if n_live == 2 or n_live == 3:
                    return 1
            return 0
        M = len(board)
        if M == 0:
            return board
        N = len(board[0])
        tmp = []
        for i in range(M):
            tmp.append([])
            for j in range(N):
                tmp[i].append(board[i][j])
        for i in range(M):
            for j in range(N):
                tmp[i][j] = interactCell(i,j,board)
        
        for i in range(M):
            for j in range(N):
                board[i][j] = tmp[i][j]

        
