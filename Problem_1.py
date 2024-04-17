'''
Time Complexity - O(n^3). outermost for burstable array size, middle loop start point, innermost loop iterates through the burstable array
Space Complexity - O(n^2)
Works on leetcode
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
        for l in range(1, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                for k in range(i, j+1):
                    #before+left*nums[k]*after
                    #before indicate balloons on left of balloon at k when burst before it
                    #after indicates balloons on right of balloon at k when burst before it
                    before, after = 0, 0
                    if k!=i:
                        before = dp[i][k-1]
                    if k!=j:
                        after = dp[k+1][j]

                    #if the first balloon in the burstable array is also the first balloon in the main array we set left to 1
                    left, right = 1, 1
                    if i!=0:
                        left = nums[i-1]
                    #if the last balloon in the burstable array is also the last balloon in the main array we set right to 1
                    if j!=n-1:
                        right = nums[j+1]

                    curr = before+left*nums[k]*right+after
                    dp[i][j] = max(dp[i][j], curr)
        return dp[0][n-1]