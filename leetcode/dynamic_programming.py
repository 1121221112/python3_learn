# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # 最高有效位， 动态规划
        # bits = [0]
        # hight_bit = 0
        # for i in range(1, n + 1):
        #     if i & (i - 1) == 0:
        #         hight_bit = i
        #     bits.append(bits[i - hight_bit] + 1)
        # return bits
        # 最低有效位
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits

    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        # LCP 07. 传递信息, 动态规划，计数relation
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for _ in range(k):
            ne = [0 for _ in range(n + 1)]
            for edge in relation:
                src = edge[0]
                dst = edge[1]
                ne[dst] += dp[src]
            dp = ne
        return dp[n - 1]

    def generate(self, numRows: int) -> List[List[int]]:
        # 118. 杨辉三角 二维列表 dp
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret


if __name__ == '__main__':
    s = Solution()
    c = s.countBits(5)
    print(c)
