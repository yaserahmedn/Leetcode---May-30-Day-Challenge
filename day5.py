class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=dict()

        for alp in s:
            if alp in d:
                d[alp]=d[alp]+1
            else:
                d[alp]=1

        result=-1

        for alp in s:
            if d[alp]==1:
                result=s.index(alp)
                break


        return result
