# -*- coding:utf-8 -*-
import collections
from typing import List


class Solution:


    def countPairs(self, nums: List[int], k: int) -> int:
        # 2176. 统计数组中相等且可以被整除的数对, 遍历
        tmp_nums = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    tmp_nums += 1
        return tmp_nums

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # 1662. 检查两个字符串数组是否相等, 直接拼接
        return "".join(word1) == "".join(word2)

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # 2089. 找出数组排序后的目标下标, 统计数量, 匹配target 后未升序nums, 获取数量即可
        cnt1 = 0  # 小于 target 的元素数量
        cnt2 = 0  # 等于 target 的元素数量
        for num in nums:
            if num < target:
                cnt1 += 1
            elif num == target:
                cnt2 += 1
        res = list(range(cnt1, cnt1 + cnt2))  # 下标数组
        return res

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 2037. 使每位学生都有座位的最少移动次数, 排序求和
        seats.sort()
        students.sort()
        return sum(abs(students[i] - seats[i]) for i in range(len(seats)))

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # 804. 唯一摩尔斯密码词
        mosi_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len(set({''.join(mosi_list[ord(i) - ord('a')] for i in w) for w in words}))


if __name__ == '__main__':
    s = Solution()
    a = s.searchRange([5, 7, 7, 8, 8, 10], 6)
    print(a)
