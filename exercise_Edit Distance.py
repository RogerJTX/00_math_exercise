import sys


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        # print(dp)
        return dp[-1][-1]

if __name__ == '__main__':
    b = Solution()
    result_word = b.minDistance('Fuzzy matching', 'spontaneous')
    print(result_word)
    result_sentence = b.minDistance('Trust in your ideas', 'Just do it')
    print(result_sentence)
    result_sentence_long = b.minDistance('Btw, SpaceX is no longer planning to upgrade Falcon 9 second stage for reusability. Accelerating BFR instead. New design is very exciting! Delightfully counter-intuitive.', 'Sure hope this isn’t true. It is the non-linearities, such as Siberian permafrost melting or ocean currents changing, that are most difficult to predict.')
    print(result_sentence_long)