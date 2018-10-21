class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(hmap, visited, x, y):
            if x not in hmap:
                return None
            if x in visited:
                return None
            visited.add(x)
            if x == y:
                return 1.0
            if y in hmap[x]:
                return hmap[x][y]
            for k,v in hmap[x].items():
                r = dfs(hmap, visited, k, y)
                if r != None:
                    return v * r
            return None
        
        hmap = {}
        
        for i in range(len(equations)):
            x = equations[i][0]
            y = equations[i][1]
            val = values[i]
            
            if x not in hmap:
                hmap[x] = {}
            hmap[x][y] = val
            
            if y not in hmap:
                hmap[y] = {}
            hmap[y][x] = 1/val
        
        result = []
        for i in range(len(queries)):
            visited = set()
            res = dfs(hmap, visited, queries[i][0], queries[i][1])
            res = res if res != None else -1.0
            result.append(res)
        return result
            
