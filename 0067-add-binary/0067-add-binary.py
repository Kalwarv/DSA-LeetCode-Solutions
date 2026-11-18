class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        result=[]

        while i>=0 or j>=0 or carry:

            total=carry

            if i>=0:
                total+=int(a[i])

            if j>=0:
                total+=int(b[j])

            result.append(str(total%2))

            carry=total//2

            i-=1
            j-=1

        return ''.join(result[::-1])

