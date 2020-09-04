#Given a string s. In one step you can insert any character at any index of the string.

#Return the minimum number of steps to make s palindrome.

#A Palindrome String is one that reads the same backward as well as forward.

#Example 1:
#Input: s = "zzazz"
#Output: 0
#Explanation: The string "zzazz" is already palindrome we don't need any insertions.

#Example 2:
#Input: s = "mbadm"
#Output: 2
#Explanation: String can be "mbdadbm" or "mdbabdm".

##################################################

class Solution:
    def minInsertions(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] =  1 + dp[i-1][j-1] 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n - dp[-1][-1]           