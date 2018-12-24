#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/14

"""
49. 字母异位词分组
"""

"""
题目：
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],

输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""

"""
思路1：
每个字符串转换成 wc 字典，并使用 tuple类型 表示作为key
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """执行用时: 144 ms, 在Group Anagrams的Python3提交中击败了99.52% 的用户"""
        hash_wc = {}        # 将 word count 转换成 tuple 作为 key
        letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                   'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                   'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                   'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                   'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

        for s in strs:
            wc = [0] * 26
            for l in s:
                wc[letters[l]] += 1

            t_wc = tuple(wc)
            if t_wc not in hash_wc:
                hash_wc[t_wc] = []
            hash_wc[t_wc].append(s)

        return list(hash_wc.values())



if __name__ == '__main__':
    slt = Solution()
    print(slt.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
