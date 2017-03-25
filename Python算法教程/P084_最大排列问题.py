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

if __name__ == "__main__":
    M = [9, 0, 8, 1, 7, 2, 6, 3, 5, 4]
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    A = native_max_perm(M, None)
    print(A)