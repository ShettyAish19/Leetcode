class MinStack:

    def __init__(self):
        self.st=[]
        self.min_st=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_st or val<=self.min_st[-1]:
            self.min_st.append(val)


    def pop(self) -> None:
        if self.st:
            val=self.st.pop()

        if self.min_st and val==self.min_st[-1]:
            self.min_st.pop()
        

    def top(self) -> int:
        if self.st:
            return self.st[-1]
        else:
            return None
        

    def getMin(self) -> int:
        if self.min_st:
            return self.min_st[-1]

        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()