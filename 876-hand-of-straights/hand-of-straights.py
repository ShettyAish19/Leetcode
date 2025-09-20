class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        f=Counter(hand)
        for num in sorted(f.keys()):
            while f[num]:
                for i in range(groupSize):
                    if f[num+i] <=0:
                        return False

                    f[num+i]-=1

        return True
        