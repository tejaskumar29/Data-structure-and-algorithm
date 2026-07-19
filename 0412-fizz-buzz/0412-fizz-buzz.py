class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        mp={3:"Fizz",5:"Buzz"}
        divisor=[3,5]
        for i in range(1,n+1):
            s=""
            for d in divisor:
                if i%d==0:
                    s+=mp[d]
            if not s:
                s+=str(i)
            res.append(s)
        return res