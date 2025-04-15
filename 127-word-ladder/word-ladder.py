class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordset=set(wordList)
        q=deque()
        q.append((beginWord,1))

        
        while q:
            word,l=q.popleft()
            if word==endWord:
                return l
            for i in range(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    new=word[:i]+j+word[i+1:]
                    if new in wordset:
                        q.append((new,l+1))
                        wordset.remove(new)

        return 0



        