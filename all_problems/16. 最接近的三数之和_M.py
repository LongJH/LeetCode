#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
16. 最接近的三数之和
"""

"""
题目：
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""

"""
解题思路：
参考 三数之和 ，定义 dif 保存最小差值以及 res 保存最终结果。
当 dif = 0 时返回 res
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """执行用时: 132 ms, 在3Sum Closest的Python3提交中击败了83.28% 的用户"""
        len_n = len(nums)
        nums.sort()

        dif = 999999
        res = 0

        for i, n_i in enumerate(nums[:-2]):

            l = i + 1
            r = len_n - 1       # 左右指针

            while l < r:
                s = n_i + nums[l] + nums[r]

                curDiff = abs(target - s)

                if curDiff == 0:
                    return s

                if curDiff < dif:
                    dif = curDiff
                    res = s

                if s < target:
                    l += 1
                else:
                    r -= 1

        return res

"""
优化：
提前结束遍历：
当 n_i, n_j, n_j+1 的和大于 target，则以后均会大于 target，可提前结束；
同理，当 n_i, n_r, n_r-1 的和小于 target，也可提前结束 
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """执行用时: 88 ms, 在3Sum Closest的Python3提交中击败了94.53% 的用户"""
        len_n = len(nums)
        nums.sort()

        dif = 999999
        res = 0

        for i, n_i in enumerate(nums[:-2]):         # 只需要遍历到倒数第三个元素

            l = i + 1
            r = len_n - 1       # 左右指针

            if n_i + nums[l] + nums[l + 1] > target:    # n_i 只会越来越大，可直接返回
                s = n_i + nums[l] + nums[l + 1]
                return s if abs(target - s) < dif else res

            if n_i + nums[r] + nums[r - 1] < target:
                s = n_i + nums[r] + nums[r - 1]
                curDiff = abs(target - s)
                if curDiff == 0:
                    return s
                if curDiff < dif:
                    dif = curDiff
                    res = s
                continue

            while l < r:
                s = n_i + nums[l] + nums[r]
                print(n_i, nums[l], nums[r], s)
                curDiff = abs(target - s)

                if curDiff == 0:
                    return s

                if curDiff < dif:
                    dif = curDiff
                    res = s

                if s < target:
                    l += 1
                else:
                    r -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))
