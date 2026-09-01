class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        repeated=set()
        for i in range(len(s)-9):
            st=s[i:i+10]
            if st in seen:
                repeated.add(st)

            else:
                seen.add(st)

        return list(repeated)
        