class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        mini=float('inf')
        ans=-1
        for i in range(len(drones)):
            dist=abs(drones[i][0]-target[0])+abs(drones[i][1]-target[1])
            if dist>drones[i][2]:
                continue
            if dist<mini:
                mini=dist
                ans=i

        return ans





        