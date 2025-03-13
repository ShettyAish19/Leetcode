class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        if not s:
            return 0

    # Step 2: Check for sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

    # Step 3: Extract digits
        num_str = ""
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break

    # Step 4: Convert string to integer
        if not num_str:
            return 0

        result = sign * int(num_str)

    # Step 5: Handle 32-bit integer limits
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max

        return result
        