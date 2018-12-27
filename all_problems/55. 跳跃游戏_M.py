#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
55. 跳跃游戏
"""

"""
题目：
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""

"""
解题思路：
判断0元素位置，若0元素之前的所有元素均小于等于其与0之间的距离，则肯定不可能到达最后
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """"""

        has0 = False
        for i, n in enumerate(nums[:-1]):
            if n == 0:
                has0 = True
                for j in range(i):
                    if nums[j] > i - j:     # 这个0可以跳过
                        has0 = False

                if has0:
                    return False

        return not has0


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
