#Valid Perfect Square

#Given a positive integer num, write a function which returns True if num is a perfect square else False.

#Note: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        while(i*i)<num:
            i=i+1
        if(i*i)==num:
            return True
        return False
