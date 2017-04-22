#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年4月22日
@details:    拓扑排序
'''

def naive_topsort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i,u in enumerate(seq):
        if v in G[u]: min_i = i+1
    seq.insert(min_i, v)
    return seq

