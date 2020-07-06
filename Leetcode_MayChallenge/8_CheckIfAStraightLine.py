class Solution:
    def slope(self, point1, point2):
        if ((point1[0] - point2[0]) == 0):
            return 0
        print(abs(point2[1] - point1[1]))
        print(abs(point2[0] - point1[0]))
        return (float)(abs(point2[1] - point1[1]) / abs(point2[0] - point1[0]))

    def checkStraightLine(self, coordinates) -> bool:
        point1 = coordinates[1]
        point2 = coordinates[0]
        gSlope = self.slope(point1, point2)
        for i in range(1,len(coordinates)):
            point1 = coordinates[i]
            point2 = coordinates[0]
            if (gSlope != self.slope(point1, point2)):
                return False
        return True


# class Solution:
#     def checkStraightLine(self, coordinates) -> bool:
#         hash={}
#         diff = -1
#         tempDiff = -1
#         p = -1
#         q = -1
#         for i in range(len(coordinates)):
#             if(len(coordinates[i])>2 or (len(hash)>0 and (abs(coordinates[i][1]+coordinates[i][0]) in hash) and (coordinates[i] in hash[abs(coordinates[i][1]+coordinates[i][0])]))):
#                 return False
#             if (diff > -1):
#                 tempDiff = abs(coordinates[i][1] - coordinates[i][0])
#                 if (tempDiff != diff):
#                     if (p != coordinates[i][0] and q != coordinates[i][1]):
#                         return False
#             else:
#                 diff = abs(coordinates[i][1] - coordinates[i][0])
#                 p = coordinates[i][0]
#                 q = coordinates[i][1]
#             hash[abs(coordinates[i][1] + coordinates[i][0])]=[]
#             hash[abs(coordinates[i][1]+coordinates[i][0])].append(coordinates[i])
#         return True


s=Solution()
print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))


