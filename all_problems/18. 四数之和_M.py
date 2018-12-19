#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
18. 四数之和
"""

"""
题目：
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

"""
解题思路：
1. 对数组进行排序
2. 依次遍历每个小于0的元素 n_i，在剩余的元素中找到和为 -n_i 的两个元素
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 1644 ms, 在4Sum的Python3提交中击败了7.94% 的用户 """
        len_n = len(nums)
        nums.sort()
        res = []

        for i, n_i in enumerate(nums[:-3]):
            if n_i > 0 and n_i > target:
                break

            if i > 0 and n_i == nums[i - 1]:     # 若 n_i = n_i-1 则跳过
                continue

            for j, n_j in enumerate(nums[i + 1: -2], i + 1):    # 遍历第二个元素
                if n_j > 0 and n_i + n_j > target:
                    break

                if j > i + 1 and n_j == nums[j - 1]:  # 若 n_j = n_j-1 则跳过
                    continue

                l = j + 1
                r = len_n - 1       # 左右指针

                while l < r:
                    s = n_i + n_j + nums[l] + nums[r] - target
                    # print(n_i , n_j , nums[l] , nums[r] , n_i + n_j + nums[l] + nums[r] - target)

                    if s == 0:
                        res.append([n_i, n_j, nums[l], nums[r]])
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


"""
优化：
通过跳出减少判断次数
通过增加冗余变量减少计算次数
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """执行用时: 104 ms, 在4Sum的Python3提交中击败了98.98% 的用户"""
        len_n = len(nums)
        nums.sort()
        res = []

        sum_l2 = sum(nums[-2:])
        sum_l3 = sum(nums[-3:])
        # 遍历第一个元素
        for i, n_i in enumerate(nums[:-3]):
            target_i = target - n_i

            if sum(nums[i+1: i+4]) > target_i:      # 连续 4 个的和大于目标值，跳出
                break

            if sum_l3 < target_i:                   # n_i 与 三个最大的值的和小于 target，跳过
                continue

            if i > 0 and n_i == nums[i - 1]:        # 若 n_i = n_i-1 则跳过
                continue

            # 遍历第二个元素
            i1 = i + 1
            for j, n_j in enumerate(nums[i1: -2], i1):
                target_ij = target_i - n_j

                if nums[j + 1] + nums[j + 2] > target_ij:
                    break

                if sum_l2 < target_ij:
                    continue

                if j > i1 and n_j == nums[j - 1]:  # 若 n_i = n_i-1 则跳过
                    continue

                l = j + 1
                r = len_n - 1       # 左右指针

                while l < r:
                    s = nums[l] + nums[r] - target_ij
                    # print(n_i , n_j , nums[l] , nums[r] , n_i + n_j + nums[l] + nums[r] - target)

                    if s == 0:
                        res.append([n_i, n_j, nums[l], nums[r]])
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
    print(s.fourSum([1,-2,-5,-4,-3,3,3,5], -11))
