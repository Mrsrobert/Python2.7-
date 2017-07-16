# -*- coding: UTF-8 -*-
__metaclass__=type
import random


#将偶数放在前面，将奇数放在后面
l1=[random.randint(1,11) for x in range(1,11)]
print u'l1的原值为：',l1

def foo(a):
	l2=[]
	oushu=[]
	jishu=[]
	for i in a:
		if i%2==0:
			oushu.append(i)
		else:
			jishu.append(i)
	l2.extend(oushu)
	l2.extend(jishu)
	return l2
			
			
		
	
	
if __name__=='__main__':
	print foo(l1)
