# TODO 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。两个相邻元素间的距离为 1 。

import numpy as np
import random
# numpy.random.randint(low[,high,size]) 值范围位于半区间[low,high)中

# print("matrix 1: \n", np.random.randint(1,9,3))
# print("matrix 2: \n", np.random.randint(1,9,(3,1)))
# print("matrix 3: \n", np.random.randint(0,9,(3,3)))

a = random.randint(0,99)
b = random.randint(0,99)

A = np.random.randint(0,2,(a,b))
B = np.random.randint(0,1,(a,b))
print("a", a)
print("b", b)
print("matrix A:", A)

n = 1
m = 1

# TODO 方法1
# def judge_around_0(n, m):
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             if A[i][j] == 0:
#                 B[i][j] = 0
#             else:
#                 if (A[i][j-1] != 0) and (A[i][j+1] != 0) and (A[i+1][j] != 0) and (A[i-1][j] != 0):
#
#
#                     n += 1
#                     m += 1
#
#
#
#
#                 elif (A[i][j-1] != 0) or (A[i][j+1] != 0) or (A[i+1][j] != 0) or (A[i-1][j] != 0):
#                     B[i][j] = 1

# TODO 方法2
# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 l, t = 10001, 10001
#                 if matrix[i][j] != 0:
#                     if i > 0:
#                         t = matrix[i - 1][j]
#
#                     if j > 0:
#                         l = matrix[i][j - 1]
#
#                     matrix[i][j] = min(l, t) + 1
#
#         for i in range(len(matrix) - 1, -1, -1):
#             for j in range(len(matrix[0]) - 1, -1, -1):
#                 r, b = 10001, 10001
#                 if matrix[i][j] != 0:
#                     if i < len(matrix) - 1:
#                         b = matrix[i + 1][j]
#
#                     if j < len(matrix[0]) - 1:
#                         r = matrix[i][j + 1]
#
#                     matrix[i][j] = min(matrix[i][j], min(r, b) + 1)
#         return matrix

# TODO 方法3
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS宽度优先搜索
        # 先找到所有的0点
        # 从0层开始搜索，与0相连的非0值全部为1
        # 继续搜索1层，与1相连的、未被遍历过的点且非0的点的值置为当前层1+1

        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0] * n for i in range(m)]
        Q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited[i][j] = 1
                    Q.append([i, j])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        cur_num = 0
        while Q:
            size = len(Q)
            for _ in range(size):
                x, y = Q.pop(0)
                for i in range(4):
                    newx, newy = x + dx[i], y + dy[i]
                    if newx < 0 or newy < 0 or newx >= m or newy >= n:
                        continue
                    if visited[newx][newy]:
                        continue
                    visited[newx][newy] = 1
                    if matrix[newx][newy] != 0:
                        matrix[newx][newy] = cur_num + 1
                        Q.append([newx, newy])
            cur_num += 1
        return matrix


