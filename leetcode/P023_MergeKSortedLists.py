#coding=utf-8

'''
    url: leetcode.com/problems/merge-k-sorted-lists/
    @author:     zxwtry
    @email:      zxwtry@qq.com
    @date:       2017年3月29日
    @details:    Solution: 56ms 52.31%
'''

from tools.Utils import *

class Solution(object):
    def cmp(self, a, b):
        if a == None:
            return 1
        elif b == None:
            return -1
        return a.val - b.val
    
    def mergeKLists(self, ls):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lsn = 0 if ls == None else len(ls)
        if (lsn == 0): return []
        heap, a, t = [], None, None
        for i in range(lsn):
            heap.append(i)
        
        
        
        
        
        