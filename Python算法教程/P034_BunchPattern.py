#encoding=utf-8

'''
@author:     zxwtry
@email:      zxwtry@qq.com
@date:       2017年3月25日
@details:    Bunch模式
@details:    例子中是以树结构来展现
@details:    属性可以从构造器中被动态设置时，可以利用该模式
'''

class Bunch(dict):
	def __init__(self, *args, **kwds):
		super(Bunch, self).__init__(*args, **kwds)
		self.__dict__ = self

if __name__=="__main__":
	x = Bunch(name="Steve Jobs", position="Apple CEO")
	print(x.name)
	#output: Steve Jobs
	
if __name__=="__main__":
	T = Bunch
	t = T(left=T(left="a", right="b"), right=T(left="c"))
	print(t.left)
	#output: {'left': 'a', 'right': 'b'}
	print("left" in t.right)
	#output: True
	print("right" in t.right)
	#output: False