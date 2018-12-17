#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
15. 三数之和
"""

"""
题目：
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
解题思路：
1. 对数组进行排序
2. 以每个
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 1100 ms, 在3Sum的Python3提交中击败了75.49% 的用户"""
        len_n = len(nums)
        nums.sort()
        res = []

        for i, n_i in enumerate(nums):
            if n_i > 0:
                break

            if i == 0 or n_i > nums[i - 1]:     # 判断与前一个元素不同, 以第 i 个数作为
                l = i + 1
                r = len_n - 1       # 左右指针

                while l < r:
                    s = n_i + nums[l] + nums[r]

                    if s == 0:
                        res.append([n_i, nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        while nums[r] == nums[r+1] and l < r:
                            r -= 1

                    elif s < 0:
                        l += 1
                    else:
                        r -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0, 0, 0]))
