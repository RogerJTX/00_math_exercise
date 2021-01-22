class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 非优化动态规划，时间复杂度O(m*n)，空间复杂度O(n*m)
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for j in range(1, m):
            grid[j][0] += grid[j - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

        # 优化算法,即求每次到达位置的最优解
        # 定义状态：即定义数组元素的含义,dp[i]表示当前位置的最小数值综合
        # 建立状态转移方程:dp[i] = min(dp[i-1],dp[i])+grid[i,j]
        # 设定初始值:这一步是关键
        # 选择结果，即dp[-1]
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for k in range(1, n):
            dp[k] = dp[k - 1] + grid[0][k]
        for i in range(1, m):
            for j in range(0, n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]

if __name__ == '__main__':
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

    s = Solution()
    result = s.minPathSum(grid)
    print(result)