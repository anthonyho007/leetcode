class Solution:
    def __init__(self):
        self.hasCycle = False
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        def topologySortHelper(visited, recStack, prereq, cId, pId, result):
            visited[cId] = True
            recStack[cId] = True
            if cId in prereq:
                for sId in prereq[cId]:
                    if not visited[sId]:
                        if topologySortHelper(visited, recStack, prereq, sId, cId, result):
                            return True
                    elif recStack[sId] == True:
                        return True
            
            result.insert(0, cId)
            recStack[cId] = False
            return False
            
        
        visited = [False] * numCourses
        recStack = [False] * numCourses
        
        result = []
        
        prereq = {}
        
        for i in range(len(prerequisites)):
            if prerequisites[i][1] not in prereq:
                prereq[prerequisites[i][1]] = [prerequisites[i][0]]
            else:
                prereq[prerequisites[i][1]].append(prerequisites[i][0])
        for i in range(numCourses):
            if not visited[i]:
                 if topologySortHelper(visited, recStack, prereq, i, -1, result) == True:
                        return []

        return result
