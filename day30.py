'''
K Closest Points to Origin
Solution
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import math

        distances=[]

        for point in points:
            x=(point[0]-0)**2
            y=(point[1]-0)**2
            distances.append((math.sqrt(x+y),point))

        distances.sort(key=lambda x: x[0])

        result=[]
        for i in range(K):
            result.append(distances[i][1])

        return result
