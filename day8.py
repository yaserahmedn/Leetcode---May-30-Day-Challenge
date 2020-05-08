class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length=len(coordinates)
        if length==2:
            return True
        else:
            point1=coordinates[0]
            point2=coordinates[1]
            if (point2[0]-point1[0]==0):
                return False
            slope=(point2[1]-point1[1])/(point2[0]-point1[0])
            i=1
            j=2
            while((i<length-1) and (j<length)):
                pointi=coordinates[i]
                pointj=coordinates[j]
                if (pointj[0]-pointi[0])==0:
                    return False
                curr_slope=(pointj[1]-pointi[1])/(pointj[0]-pointi[0])
                if curr_slope!=slope:
                    return False
                i=i+1
                j=j+1
            return True
