def decode_message( s: str, p: str) -> bool:

# write your code here
        m = len(s)
        p = len(pattern)
    
    # Create a DP table initialized with False values
        dp = [[False] * (m + 1) for _ in range(p + 1)]
        dp[0][0] = True  # Empty pattern matches empty message

        # Handle patterns that start with '*'
        for i in range(1, p + 1):
                if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        
        # Fill the DP table
        for i in range(1, p + 1):
                for j in range(1, m + 1):
                if pattern[i - 1] == message[j - 1] or pattern[i - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == '*':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[p][m]