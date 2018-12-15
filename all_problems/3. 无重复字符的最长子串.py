#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
3. 无重复字符的最长子串
"""

"""
题目：
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

"""
解题思路：
使用滑动窗口法寻找子串
1. i, j 分别表示当前的窗口右左指针，i 依次向右滑动
2. t 依次指向窗口内元素，若发现 t 与 i 相等，则 i - j 为当前窗口的无重复字串长度
3. 使 j = t + 1，让 i 继续往后遍历
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """执行用时: 120 ms, 在Longest Substring Without Repeating Characters的Python3提交中击败了74.02% 的用户"""

        s_len = len(s)
        max_len = 0  # 记录最大子串的长度

        # 左窗口指针
        j = 0

        for i in range(s_len):  # 右窗口指针
            for t in range(j, i):  # 窗口内指针
                if s[t] == s[i]:
                    # 子串中发现重复字符，记录长度并更新 j 位置
                    t_len = i - j  # 记录窗口中的子串长度
                    max_len = t_len if t_len > max_len else max_len
                    j = t + 1
                    break

        t_len = s_len - j  # 记录窗口中的子串长度
        max_len = t_len if t_len > max_len else max_len

        return max_len


"""
思路2：
使用元素替代指针
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """执行用时: 132 ms"""

        sub = ''  # 记录字串
        sub_len = 0
        max_len = 0  # 记录最大子串的长度
        max_sub = ''

        for l in s:  # 右窗口指针
            if l in sub:
                if sub_len > max_len:
                    max_len = sub_len
                    max_sub = sub

                i = sub.index(l)
                sub = sub[i + 1:] + l
                sub_len = sub_len - i

            else:
                sub = sub + l
                sub_len += 1

        if sub_len > max_len:
            max_len = sub_len

        return max_len


"""
思路3：
使用字典存储每个字符对应的最大子串长度
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """执行用时: 124 ms"""

        j = 0       # 滑动窗口的左指针
        max_len = 0
        hash_str = {}   # 记录每个元素上一次出现的位置
        for i, char in enumerate(s):
            if char in hash_str and j <= hash_str[char]:  # 若出现重复字符，则更新 j
                j = hash_str[char] + 1
            else:       # 否则，更新 max_len
                if max_len < (i - j + 1):
                    max_len = i - j + 1
            hash_str[char] = i

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('pwwkew'))
