#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    Bunch模式
'''

from random import randrange

def nn_sol(seq):
    dd = float("inf")
    for x in seq:
        for y in seq:
            if x == y: continue
            d = abs(x - y)
            if d < dd:
                xx, yy, dd = x, y, d
    #print("%d %d" % (1, 2))
    print("%d %d" % (xx, yy))

def nlgn_sol(seq):
    seq.sort(key=None, reverse=False)
    dd = float("inf")
    for i in range(len(seq) - 1):
        x,y = seq[i], seq[i + 1]
        if (x == y): continue
        d = abs(x - y)
        if d < dd:
            xx, yy, dd = x, y, d
    print("%d %d" % (xx, yy))

if __name__ == "__main__":
    seq = [randrange(10**10) for i in range(100)]
    nn_sol(seq)
    nlgn_sol(seq)