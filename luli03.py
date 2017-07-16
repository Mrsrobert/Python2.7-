# -*- coding: UTF-8 -*-
__metaclass__=type



def fib(a):
	b=[0,1]
	for i in range(a-2):
		b.append(b[-2]+b[-1])
		
	return b
	
print fib(10)
	
	






