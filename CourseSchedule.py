class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # we just need to contruct an DAG graph and check if there is cycle
        def helper(visited, recStack, prereq,cId):
            visited[cId] = True
            recStack[cId] = True
            if cId in prereq:
                for sId in prereq[cId]:
                    if visited[sId] == False:
                        if helper(visited, recStack, prereq, sId) == True:
                            return True
                    elif recStack[sId] == True:
                        return True
            
            recStack[cId] = False
            return False
        
        visited = [False] * numCourses
        recStack = [False] * numCourses
        prereq = {}
        
        for x, y in prerequisites:
            if y not in prereq:
                prereq[y] = [x]
            else:
                prereq[y].append(x)
        
        for i in range(len(visited)):
            if not visited[i]:
                if helper(visited, recStack, prereq, i):
                    return False
        
        return True
