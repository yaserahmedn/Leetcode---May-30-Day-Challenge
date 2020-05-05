class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones=set(S)
        count=0
        for stone in stones:
            if stone in J:
                count+=S.count(stone)
        return count
