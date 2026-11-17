class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        m=len(num1)
        n=len(num2)

        result = [0] * (m+n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):

                digit1=int(num1[i]) #convert individual character into digit
                digit2=int(num2[j])

                pos=i+j+1  #For result position

                total = digit1 * digit2 + result[pos]  #multipying and add the existing value 

                result[pos] = total%10   # only adding the reminder 

                result[pos-1]+=total//10  #here we are getting carry to previous index

        return ''.join(map(str, result)).lstrip('0')  #to convert the array result in to string again and to remove trailing 0

            







