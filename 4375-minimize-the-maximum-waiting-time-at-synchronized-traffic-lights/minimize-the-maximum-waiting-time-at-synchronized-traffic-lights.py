class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxi=0
        for i in range(len(arrivalTime)):
            arrivalTime[i]=arrivalTime[i]%period

        arrivalTime.sort()

        lights.sort()
        ans=0
        i=0
        j=0
        while i<len(arrivalTime) and j<len(lights):
            if arrivalTime[i]<lights[j]:
                i+=1
                
            else:
                j+=1

        while i<len(arrivalTime):
            maxi=max(maxi,period-arrivalTime[i])
            i+=1
            

        return maxi


            
        