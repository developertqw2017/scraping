from random import randint
class Solution(object):
    n = 0
    rain = 0
    flag = True
    height = 0
    def trap(self):
        for x in range(1,len(self.height)-1):
            l1 = self.height[:x]
            l2 = self.height[x+1:]
            L1 = list(filter(self.more_than(self.height[x]),l1))
            print(L1)
            L2 = list(filter(self.more_than(self.height[x]),l2))
            print(L2)
            if L1 != [] and L2 != []:
                flag = False
            if L1 ==[] or L2 == []:
                continue
            self.rain = self.rain + min(L1[-1],L2[0])
            self.height[x] = self.height[x] + min(L1[-1],L2[0])
            if x == len(self.height)-1 and flag == False:
                for x2 in range(1,len(self.height)-1):
                    self.flag = True
                    self.trap(self.height)
            print(self.rain)
            print(self.height)
            return 0



    def __init__(self,n):
        self.n = n
        self.height = [0 for x in range(n)]
        for x in range(len(self.height)):
            self.height[x] = randint(0,5)


    def less_than(self,v1):
        return lambda x : x < v1

    def more_than(self,v2):
        return lambda x : x > v2

s = Solution(12)
s.trap()
