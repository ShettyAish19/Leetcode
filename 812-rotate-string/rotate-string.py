class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        n = len(s)

        for start in range(n):

            j = 0

            while j < n and s[(start + j) % n] == goal[j]:
                j += 1

            if j == n:
                return True

        return False