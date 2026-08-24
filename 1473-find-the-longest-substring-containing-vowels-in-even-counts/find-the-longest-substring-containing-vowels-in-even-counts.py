class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask=00000
        first=[-2]*32
        first[0]=-1
        ans=0
        vowel={
            'a':1,'e':2,'i':4,'o':8,'u':16 }

        for i,ch in enumerate(s):
            if ch in vowel:
                mask^=vowel[ch]

            if first[mask]!=-2:
                ans=max(ans,i-first[mask])

            else:
                first[mask]=i

        return ans       