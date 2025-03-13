class Solution:
    def myAtoi(self, s: str) -> int:
        
        def convert_recursive(s, index=0, result=0):
            if index == len(s) or not s[index].isdigit():
                return result
        
        # Append current digit to the result
            result = result * 10 + (ord(s[index]) - ord('0'))
            return convert_recursive(s, index + 1, result)

    # Step 1: Trim leading whitespace
        s = s.lstrip()
    
        # Step 2: Handle sign
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
    
    # Step 3: Extract digits (handles leading zeros naturally)
        digits = ''
        for char in s:
            if char.isdigit():
                digits += char
            else:
                break

    # Step 4: Handle empty digit string
        if not digits:
            return 0

    # Step 5: Recursive conversion
        result = convert_recursive(digits)

    # Step 6: Apply sign and clamp result to 32-bit integer limits
        result *= sign
        return max(-2**31, min(result, 2**31 - 1))
        