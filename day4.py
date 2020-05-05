class Solution:
    def findComplement(self, n: int) -> int:
        binaryNum= bin(n).replace("0b","")


        binaryNum=list(binaryNum)
        s=''

        for i in range(0,len(binaryNum)):
            if binaryNum[i]=='0':
                binaryNum[i]=1
            else:
                binaryNum[i]=0
            s=s+str(binaryNum[i])

        result=int(s,2)
        return result
