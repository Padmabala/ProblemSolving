class Solution:
    def kClosest(self, points,K):
        points.sort(key=lambda K:K[0]**2+K[1]**2)
        return points[:K]