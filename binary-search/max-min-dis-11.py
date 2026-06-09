class Solution:

    def canPlace(self, positions, k, dist):

        routers = 1
        last = positions[0]

        for i in range(1, len(positions)):

            if positions[i] - last >= dist:
                routers += 1
                last = positions[i]

            if routers == k:
                return True

        return False


    def maxMinDistance(self, positions, k):

        positions.sort()

        low = 1
        high = positions[-1] - positions[0]

        ans = 0

        while low <= high:

            mid = (low + high) // 2

            if self.canPlace(positions, k, mid):

                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans




    print(maxMinDistance([1,2,8,12,1], 3))
    #  [1,2,8,12,1]