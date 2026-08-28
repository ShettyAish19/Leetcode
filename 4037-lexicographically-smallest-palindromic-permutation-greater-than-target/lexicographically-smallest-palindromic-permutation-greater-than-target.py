from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        
        count = Counter(s)
        n = len(s)

        # 1. Check whether a palindrome is possible
        odd = []

        for ch in count:
            if count[ch] % 2 == 1:
                odd.append(ch)

        if len(odd) > 1:
            return ""

        # 2. Find middle character
        middle = odd[0] if odd else ""

        # 3. Build the multiset for the left half
        half = []

        for ch in "abcdefghijklmnopqrstuvwxyz":
            half.extend([ch] * (count[ch] // 2))

        half = "".join(half)
        m = len(half)

        # Only first half of target is relevant initially
        target_half = target[:m]

        # ------------------------------------------------
        # Case 1: Can we exactly make target_half?
        # ------------------------------------------------
        half_count = Counter(half)

        possible_equal = True

        for ch in target_half:
            if half_count[ch] == 0:
                possible_equal = False
                break
            half_count[ch] -= 1

        if possible_equal:
            candidate = (
                target_half +
                middle +
                target_half[::-1]
            )

            # If this palindrome itself is greater
            if candidate > target:
                return candidate

            # Otherwise need the NEXT permutation
            next_half = list(target_half)

            if self.nextPermutation(next_half):
                left = "".join(next_half)

                return (
                    left +
                    middle +
                    left[::-1]
                )

            return ""

        # ------------------------------------------------
        # Case 2: Cannot exactly match target_half
        # Find smallest permutation strictly greater
        # ------------------------------------------------
        left = self.smallestGreater(half, target_half)

        if left == "":
            return ""

        return left + middle + left[::-1]


    # Same idea as the previous question
    # Find smallest permutation of s strictly > target
    def smallestGreater(self, s, target):

        count = Counter(s)
        prefix = []
        n = len(s)

        i = 0

        # Match target as much as possible
        while i < n and count[target[i]] > 0:
            prefix.append(target[i])
            count[target[i]] -= 1
            i += 1

        # First try the position where matching failed
        if i < n:
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c > target[i] and count[c] > 0:

                    count[c] -= 1

                    suffix = []
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        suffix.extend([ch] * count[ch])

                    return "".join(prefix) + c + "".join(suffix)

        # Otherwise backtrack
        for pos in range(i - 1, -1, -1):

            ch = prefix.pop()
            count[ch] += 1

            for c in "abcdefghijklmnopqrstuvwxyz":

                if c > target[pos] and count[c] > 0:

                    count[c] -= 1

                    suffix = []

                    for x in "abcdefghijklmnopqrstuvwxyz":
                        suffix.extend([x] * count[x])

                    return "".join(prefix) + c + "".join(suffix)

        return ""


    def nextPermutation(self, nums):

        n = len(nums)

    # No next permutation possible
        if n <= 1:
            return False

        i = n - 2

    # Find first position from right where nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

    # Entire array is descending
        if i < 0:
            return False

        j = n - 1

    # Find rightmost element greater than nums[i]
        while j > i and nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    # Reverse suffix
        nums[i + 1:] = reversed(nums[i + 1:])

        return True