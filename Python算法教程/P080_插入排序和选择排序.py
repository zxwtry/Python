#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    插入排序和选择排序，分别用递归和迭代实现
'''

#递归版的插入排序   [i, j)序
def insert_sort_recursion(seq, i, j):
    if j <= i + 1: return
    insert_sort_recursion(seq, i, j - 1)
    k = j - 1
    while k > 0 and seq[k - 1] > seq[k]:
        seq[k - 1], seq[k] = seq[k], seq[k - 1]
        k -= 1

#迭代版本的插入排序   [i, j)
def insert_sort_iteration(seq, i, j):
    if j <= i + 1: return
    for r in range(i, j):
        l = r
        while l > 0 and seq[l - 1] > seq[l]:
            seq[l - 1], seq[l] = seq[l], seq[l - 1]
            l -= 1

#递归版本的插入排序   [i, j)
def select_sort_recursion(seq, i, j):
    if j <= i + 1: return
    max_i = i;
    for v in range(i + 1, j):
        if (seq[max_i] < seq[v]):
            max_i = v
    seq[j - 1], seq[max_i] = seq[max_i], seq[j - 1]
    select_sort_recursion(seq, i, j - 1)
    
#迭代版本的插入排序   [i, j)
def select_sort_iteration(seq, i, j):
    if j <= i + 1: return
    for k in range(j - 1, i, -1):
        max_i = k
        for v in range(i, k, 1):
            if (seq[max_i] < seq[v]):
                max_i = v
        seq[max_i], seq[k] = seq[k], seq[max_i]

if __name__ == "__main__":
    seq = [4, 3, 2, 1]
    insert_sort_recursion(seq, 0, len(seq))
    print(" %d" * len(seq) % tuple(seq))
    seq = [4, 3, 2, 1]
    insert_sort_iteration(seq, 0, len(seq))
    print(" %d" * len(seq) % tuple(seq))
    seq = [4, 3, 2, 1]
    select_sort_recursion(seq, 0, len(seq))
    print(" %d" * len(seq) % tuple(seq))
    seq = [4, 3, 2, 1]
    select_sort_iteration(seq, 0, len(seq))
    print(" %d" * len(seq) % tuple(seq))
