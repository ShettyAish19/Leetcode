class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d={}
        d[5]=d[10]=d[20]=0

        for i in bills:
            d[i]+=1

            if i==10:
                if d[5]>0:
                    d[5]-=1
                else:
                    return False

            elif i==20:
                if d[10]>0 and d[5]>0:
                    d[10]-=1
                    d[5]-=1

                elif d[5]>=3:
                    d[5]-=3

                else:
                    return False

        return True

            

        