class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        mid=n//2
        leftq=0
        rightq=0
        lefts=0
        rights=0


        for i in range(len(num)):
            if num[i]=='?':
                if i<mid:
                    leftq+=1
                else:
                    rightq+=1

            else:
                if i<mid:
                    lefts+=int(num[i])

                else:
                    rights+=int(num[i])

        if (leftq+rightq)%2==1:
            return True

        return 9*(rightq-leftq)!=2*(lefts-rights)
    


        