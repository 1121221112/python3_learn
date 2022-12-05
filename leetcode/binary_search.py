# -*- coding:utf-8 -*-


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
from typing import List


def guess(mid):
    # 374 内置函数
    pass


class Solution:

    def guessNumber(self, n: int) -> int:
        # 374. 猜数字大小
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:  # 答案在区间 [left, mid] 中
                right = mid
            else:
                left = mid + 1  # 答案在区间 [mid+1, right] 中

        # 此时有 left == right，区间缩为一个点，即为答案
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 34. 在排序数组中查找元素的第一个和最后一个位置
        left, right, ans = 0, len(nums) - 1, [-1, -1]
        if not nums:
            return ans
        # 左边界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            ans[0] = left

        left, right = 0, len(nums) - 1
        # 右边界
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        if nums[left] == target:
            ans[1] = left

        return ans

    def search(self, nums: List[int], target: int) -> int:
        # 704. 二分查找
        l, r, ans = 0, len(nums) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
                ans = mid if nums[mid] == target else -1
            else:
                r = mid - 1
        return ans

    def mySqrt(self, x: int) -> int:
        # 69. x 的平方根
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                # 加1 避免死循环
                l = mid + 1
            else:
                # 减1 避免死循环
                r = mid - 1
        return ans

    def searchInsert(self, nums: List[int], target: int) -> int:
        # 35. 搜索插入位置, 二分查找
        len_nums = len(nums)
        left, right = 0, len_nums
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 406. 根据身高重建队列， 身高倒叙， 个数正序
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = list()
        for p in people:
            if len(ans) <= p[1]:
                ans.append(p)
            elif len(ans) > p[1]:
                ans.insert(p[1], p)
        return ans
