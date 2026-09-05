class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:

        n = len(stations)

        power = [0] * n
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]

        power = [0] * n

        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)

            power[i] = prefix[right + 1] - prefix[left]

        def is_possible(target):

            diff = [0] * (n + 1)
            extra = 0
            used = 0

            for i in range(n):

                extra += diff[i]

                current = power[i] + extra

                if current < target:

                    need = target - current

                    used += need

                    if used > k:
                        return False

                    extra += need

                    end = i + 2*r + 1

                    if end < n:
                        diff[end] -= need

            return True


        low = min(power)
        high = max(power) + k
        ans = -1

        while low <= high:

            mid = (low + high) // 2

            if is_possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans