class Solution(object):
    def uniquePathsWithObstacles(self, ob):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if ob[0][0] == 1:
            return 0
        ob[0][0] = 1
        n,m = len(ob[0]), len(ob)
        for i in range(1,m):
            ob[i][0] = int(ob[i][0]==0 and ob[i-1][0]==1)
        for j in range(1,n):
            ob[0][j] = int(ob[0][j]==0 and ob[0][j-1])
        for i in range(1,m):
            for j in range(1,n):
                if ob[i][j]:
                    ob[i][j]=0
                    continue
                ob[i][j] = ob[i-1][j] + ob[i][j-1]
        return ob[-1][-1]