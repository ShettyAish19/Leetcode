class Solution:
    def canCross(self, stones: List[int]) -> bool:

        stoneset = set(stones)
        memo = {}

        def dfs(curpos, last):

            if curpos == stones[-1]:
                return True

            if (curpos, last) in memo:
                return memo[(curpos, last)]

            for jump in (last - 1, last, last + 1):

                if jump > 0:

                    if curpos + jump in stoneset:

                        if dfs(curpos + jump, jump):
                            memo[(curpos, last)] = True
                            return True

            memo[(curpos, last)] = False
            return False

        if 1 not in stoneset:
            return False

        return dfs(1, 1)