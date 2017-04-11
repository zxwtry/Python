#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    最大排列问题
'''

def native_max_perm(M, A=None):
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return native_max_perm(M, A)
    return A

def loop_max_perm(M):
    n = 0 if M == None else len(M)
    A, count = set(range(n)), [0]*n
    for i in M: count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A
    
from _collections import defaultdict

def counting_sort(A, key=lambda x:x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C)+1):
        B.extend(C[k])
    return B

if __name__ == "__main__":
    M = [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    A = native_max_perm(M, None)
    B = counting_sort(M, None)
    print(B)
    print(A)