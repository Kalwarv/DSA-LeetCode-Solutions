class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i=len(num)-1

        while i>=0 and k>0:
            total=num[i]+k

            num[i]=total%10
            k=total//10

            i-=1
        
        while k>0:
            num.insert(0,k%10)
            k//=10

        return num