

class Solution:
    def getHouses(self, t, xa):
        result = 2
        houses = []
        for i in range(len(xa)//2):
            houses.append([xa[2*i]-xa[2*i+1]//2, xa[2*i]+xa[2*i+1]//2])
        houses.sort(key=lambda x: x[0])
        leftskip = houses[0][0]-1
        rightskip = houses[0][0]
        houseindex = 0
        while True:
            nextskip = houses[houseindex][1]
            while(houseindex+1 < len(houses) and houses[houseindex+1][0] <= nextskip):
                houseindex += 1
                nextskip = houses[houseindex][1]
            leftskip = nextskip
            if houseindex == len(houses)-1:
                break
            houseindex += 1
            rightskip = houses[houseindex][0]
            if rightskip-leftskip > t:
                result += 2
            elif rightskip-leftskip == t:
                result += 1
            else:
                pass

        return(result)
        pass

        # write code here


# solu = Solution()
# solu.getHouses(2, [-1, 4, 5, 2, 7, 2, 100, 3])
