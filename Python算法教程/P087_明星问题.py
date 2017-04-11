#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年4月8日
@details:    明星问题：明星不认识其他人，其他人都认识明星
'''

def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else: return u
    return None
#即在for 循环中，如果没有从任何一个break中退出，则会执行和for对应的else
#只要从break中退出了，则else部分不执行。

def celeb(G):
    n, u, v = len(G), 0, 1
    for c in range(2, n+1):
        if G[u][v]: u = c
        else: v = c
    c = v if u == n else u
    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
    else: return c
    return None

if __name__ == "__main__":
    G = []
    G.append([True, True, True])
    G.append([False, True, True])
    G.append([False, False, True])
    print(naive_celeb(G))
    print(celeb(G))

