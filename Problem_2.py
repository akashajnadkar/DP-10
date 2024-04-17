class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        '''
        Time Complexity - O(n^2 * k)....Time Limit Exceeded on LC
        Space Complexity - O(nk)
        Does not Work on Leetcode
        '''
        # dp = [[0 for j in range(n+1)] for k in range(k+1)]
        # for j in range(1, n+1):
        #     dp[1][j] = j
        
        # for i in range(2, k+1):
        #     for j in range(1, n+1):
        #         dp[i][j] = 1e9
        #         for f in range(1, j+1):
        #             dp[i][j] = min(dp[i][j], 1+max(dp[i-1][f-1], dp[i][j-f]))
        # return dp[k][n]

        '''
        Time Complexity - O(n*k)
        Space Complexity - O(nk)
        Works on Leetcode
        '''
        #Actual solution, requires thoda reverse engineering.
        #given number of attempts and number eggs we can get a ball park range of number of floors we can find

        ''' So we consider eggs and attempts and calculate 1+number of floors that can be covered if I have 1 less attempt and 1 less egg(if egg breaks on throwing from this floor) + 
                                                            +number of floors that can be covered if I have 1 less attempt and same number of eggs(if egg does not break on throwing from this floor) '''
        
        dp = [[0 for j in range(k+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, k+1):
                #find number of floors for number of attempts and number of eggs
                #when the number of floors is greater or equal to the input, we return the number of attempts
                dp[i][j] = 1+ dp[i-1][j-1] + dp[i-1][j]
                if dp[i][j] >= n:
                    return i
        