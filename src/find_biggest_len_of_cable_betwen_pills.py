#9
import math
def max_cable_length(w, heights):
    n = len(heights)
    dp = [[-1 for _ in range(2)] for _ in range(n)]

    def calculate(i, prev_height):
        if i == n:  
            return 0
        if dp[i][prev_height] != -1:
            return dp[i][prev_height]

        prev_h = heights[i - 1] if prev_height == 0 else 1
        h_max = heights[i]
        dist_max = math.sqrt(w ** 2 + (prev_h - h_max) ** 2) + calculate(i + 1, 0)

        h_min = 1
        dist_min = math.sqrt(w ** 2 + (prev_h - h_min) ** 2) + calculate(i + 1, 1)

        dp[i][prev_height] = max(dist_max, dist_min)
        return dp[i][prev_height]

    result = max(calculate(1, 0), calculate(1, 1))

    return result


