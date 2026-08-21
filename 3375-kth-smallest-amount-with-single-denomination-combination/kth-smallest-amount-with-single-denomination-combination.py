from math import gcd

class Solution:

    def findKthSmallest(self, coins, k):

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # How many valid amounts are <= x?
        def count(x):

            ans = 0

            # Try every subset of coins
            for mask in range(1, 1 << n):

                common = 1
                bits = 0

                for i in range(n):

                    # Is coin i included in this subset?
                    if mask & (1 << i):

                        bits += 1

                        # LCM of selected coins
                        common = lcm(common, coins[i])

                        if common > x:
                            break

                if common > x:
                    continue

                # Odd subset size -> ADD
                if bits % 2 == 1:
                    ans += x // common

                # Even subset size -> SUBTRACT
                else:
                    ans -= x // common

            return ans

        # Binary search for smallest x
        # such that there are at least k valid numbers <= x

        left = 1
        right = min(coins) * k

        while left < right:

            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid

            else:
                left = mid + 1

        return left