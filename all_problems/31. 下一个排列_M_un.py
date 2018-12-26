#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
31. 下一个排列
"""

"""
题目：
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

"""
思路1：
1. 从后往前扫描，找出后一位比前一位小的元素 i
2. 从上一个元素往后扫描，找出第一个比他小的元素 j
3. 交换这两个元素 i，j
4. 将 j 以后元素排序
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """执行用时: 56 ms, 在Next Permutation的Python3提交中击败了99.87% 的用户"""
        if not nums:
            return []

        l = len(nums)
        i = l - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        if i >= 0:
            j = l - 1
            while j >= i:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j -= 1

        nums[i+1:] = sorted(nums[i+1:])



if __name__ == '__main__':
    slt = Solution()
    print(slt.nextPermutation([1,3,2]))
