#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    Bunch模式
'''

from random import randrange
from jinja2._compat import unichr

if __name__ == "__main__":
    L = [randrange(10000) for i in range(1000)]
    print(42 in L)
    #output False 线性查找
    S = set(L)
    print(42 in S)
    #output False 常数查找
    print(str(len(L)) + "..." + str(len(S)))
    #output 1000...953

def string_producer():
    l = randrange(20);
    a = ""
    for i in range(l):
        #a += unichr(('a' + randrange(26)))
        a += unichr(ord('a') + randrange(26))
    return a

if __name__ == "__main__":
    a = ""
    b = []
    for i in range(1000):
        t = string_producer()
        a += t          #平方级
        b.append(t)     #效率一直很高
    print(a == ''.join(b))
    #output: True
    
if __name__ == "__main__":
    lists = [[1,2], [3,4,5], [6]]
    print(sum(lists, []))   #sum函数对需要叠加的东西一无所知，平方
    #output: [1, 2, 3, 4, 5, 6]
    res = []
    for lst in lists:
        res.extend(lst)     #和.append类似
    print(res)
    #output: [1, 2, 3, 4, 5, 6]
    
    