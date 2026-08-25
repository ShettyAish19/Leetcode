class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        prev=0
        t=0
        for i in requests:
            t+=abs(prev-i)
            prev=i

        return t
        