#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    二叉树和多路搜索树
'''

class BinaryTree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class MultiwayTree:
    def __init__(self, kids, nextOne=None):
        self.kids = self.val = kids
        self.nextOne = nextOne;

if __name__=="__main__":
    t = BinaryTree(BinaryTree("a", "b"), BinaryTree("c", "d"))
    print(t.right.left)
    #output: c
    
if __name__=="__main__":
    t = MultiwayTree(MultiwayTree("a", MultiwayTree("b", MultiwayTree("c", MultiwayTree("d")))));
    print(t.kids.nextOne.nextOne.val)
    #output: c