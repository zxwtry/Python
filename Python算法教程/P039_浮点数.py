#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    浮点数不精确
'''

if __name__ == "__main__":
    print(sum(0.1 for i in range(10)) == 1)
    #output: False
    print(sum(0.125 for i in range(8)) == 1)
    #output: True
    
#使用unittest模块中的assertAlmostEqual实现
def almost_equal(x, y, places=7):
    return round(abs(x-y), places) == 0

if __name__ == "__main__":
    print(almost_equal(sum(0.1 for i in range(10)), 1))
    #output: True
    
#如果需要某种精确的十进制浮点数表示法，可以使用decimal模块
from decimal import Decimal

if __name__ == "__main__":
    print(sum(Decimal("0.1") for i in range(10)) == Decimal("1"))
    #output: True
    
#如果需要对一定数位范围内的十进制进行精确计算的话，如财务数据。如Sage模块，需要单独下载
if __name__ == "__main__":
    #sage: 3/5 * 11 / 7 + sqrt(5239)
    print()
    
#值相近减法运算会丢失精度
from math import sqrt
if __name__ == "__main__":
    x = 987737323.23
    print(sqrt(x + 1) - sqrt(x))            #减法会丢失精度
    print(1.0 / (sqrt(x + 1) + sqrt(x)))    #这里更好一点