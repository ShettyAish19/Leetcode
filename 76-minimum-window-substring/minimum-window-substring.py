class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        d1 = {}
        for char in t:
            d1[char] = d1.get(char, 0) + 1

        left = 0
        cnt = 0
        min_len = float('inf')
        start = 0
        window_count = {}

        for right in range(len(s)):
            char = s[right]
            
            if char in d1:
                window_count[char] = window_count.get(char, 0) + 1
                if window_count[char] <= d1[char]:
                    cnt += 1  # Only count characters that contribute to fulfilling `t`
            
            while cnt == len(t):  # Valid window found
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # Shrink the window
                left_char = s[left]
                if left_char in d1:
                    if window_count[left_char] == d1[left_char]:
                        cnt -= 1  # A required character is being removed
                    window_count[left_char] -= 1
                left += 1

        return s[start:start + min_len] if min_len != float('inf') else ""
