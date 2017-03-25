#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    用L形砖去拼接一个缺角的8*8棋盘
'''

def cover(board, lab=1, top=0, left=0, side=None):
    if side is None: side = len(board)
    s = side // 2
    offsets = (0, -1), (side - 1, 0)
    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top + dy_outer][left + dx_outer]:
                board[top + s + dy_inner][left + s + dx_inner] = lab
    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                lab = cover(board, lab, top + dy, left + dx, s)
    return lab

if __name__ == "__main__":
    for i in range(0,2,6):
        print(i)
    l = 4**1
    board = [[0] * l for i in range(l)]
    board[l - 1][l - 1] = -1
    #print(cover(board))
    #output: 22
    #for row in board:
    #    print((" %2i" * l) % tuple(row))