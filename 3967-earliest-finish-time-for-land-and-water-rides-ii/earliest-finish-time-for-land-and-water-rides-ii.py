from bisect import bisect_right

class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        def solve(firstStart, firstDur,
                  secondStart, secondDur):

            rides = sorted(
                zip(secondStart, secondDur)
            )

            starts = [s for s, d in rides]
            durs = [d for s, d in rides]

            n = len(rides)

            # prefix minimum duration
            prefix = [0] * n
            prefix[0] = durs[0]

            for i in range(1, n):
                prefix[i] = min(
                    prefix[i - 1],
                    durs[i]
                )

            # suffix minimum of (start + duration)
            suffix = [0] * n
            suffix[-1] = (
                starts[-1] + durs[-1]
            )

            for i in range(n - 2, -1, -1):
                suffix[i] = min(
                    suffix[i + 1],
                    starts[i] + durs[i]
                )

            ans = float('inf')

            for s, d in zip(firstStart, firstDur):

                finish = s + d

                # split point
                idx = bisect_right(starts, finish)

                # CASE 1:
                # rides already open
                if idx > 0:
                    ans = min(
                        ans,
                        finish + prefix[idx - 1]
                    )

                # CASE 2:
                # rides not open yet
                if idx < n:
                    ans = min(
                        ans,
                        suffix[idx]
                    )

            return ans

        # LAND -> WATER
        ans1 = solve(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        # WATER -> LAND
        ans2 = solve(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(ans1, ans2)