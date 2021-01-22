# -*- coding:utf-8-*-
# 将 10不断除以2，直至商为0，输出这个过程中每次得到的商的值。
def recursion(n):
    v = n//2 # 地板除，保留整数
    print(v) # 每次求商，输出商的值
    if v==0:
        ''' 当商为0时，停止，返回Done'''
        return 'Done'
    v = recursion(v) # 递归调用，函数内自己调用自己
recursion(10) # 函数调用