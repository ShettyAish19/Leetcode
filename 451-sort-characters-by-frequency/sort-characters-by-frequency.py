class Solution:
    def frequencySort(self, s: str) -> str:

        d = {}

        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        max_d = max(d.values())

        # bucket[f] = characters having frequency f
        bucket = [[] for _ in range(max_d + 1)]

        for ch, freq in d.items():
            bucket[freq].append(ch)

        ans = ""

        # highest frequency first
        for freq in range(max_d, 0, -1):

            for ch in bucket[freq]:
                ans += ch * freq

        return ans