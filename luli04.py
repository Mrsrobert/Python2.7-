# -*- coding:utf-8 -*-
__metaclass__=type





count=0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j) and (j!=k) and (i!=k):
				count+=1
				print i,j,k


print 'count=',count
