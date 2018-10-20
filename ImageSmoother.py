class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(board, x, y):
            M = len(board)
            N = len(board[0])
            size = 0
            tot = 0
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and i < M and j >= 0 and j < N:
                        tot += board[i][j]
                        size += 1
            return tot / size
        
        m = len(M)
        if m == 0:
            return M
        n = len(M[0])
        
        tmp = []
        for i in range(m):
            tmp.append([])
            for j in range(n):
                tmp[i].append(0)
        
        for i in range(m):
            for j in range(n):
                tmp[i][j] = helper(M, i, j)
        
        return tmp
