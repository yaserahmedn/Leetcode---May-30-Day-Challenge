'''
Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
'''

class Solution:
    def dfs(self, start):
        if self.found_loop == 1: return        #early stop if we found odd cycle
    
        for neib in self.adj_list[start]:
            if self.dist[neib] > 0 and (self.dist[neib] - self.dist[start]) %2 == 0:
                self.found_loop = 1
            elif self.dist[neib] < 0:  #not visited yet
                self.dist[neib] = self.dist[start] + 1
                self.dfs(neib)
            
    def possibleBipartition(self, N, dislikes):
        self.adj_list = defaultdict(list)
        self.found_loop, self.dist = 0, [-1] *(N+1)
        
        for i,j in dislikes:
            self.adj_list[i].append(j)
            self.adj_list[j].append(i)
        
        for i in range(N):
            if self.found_loop: return False    #early stop if we found odd cycle
            
            if self.dist[i] == -1:    #not visited yet
                self.dist[i] = 0
                self.dfs(i)
        
        return True
