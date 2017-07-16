# -*- coding: UTF-8 -*-
__metaclass__=type
import random


#求平均数，中位数，众数
l1=[random.randint(1,11) for x in range(1,11)]
print u'l1的原值为：',l1

#平均数
def average(a):
	sum1=sum(a)
	return (sum1*1.0)/len(a)
	
#中位数：排序后，当样本数为奇数时，中位数是n/2.当样本数为偶数时，中位数是n/2与n/2+1的平均数!(其中n为列表的个数)
def among(a):#只处理n为偶数的情况
	b=sorted(a)
	print b
	b1=b[len(b)/2]
	b2=b[(len(b)/2)+1]
	av1=(b1+b2)/2
	return av1
	
#在一个列表中出现次数最多的为众数	
def zhong_shu(a):
	dict1={}
	zhongshu=[]
	for i in a:
		dict1[i]=a.count(i)
	max1=max(dict1.values())
	for k,v in dict1.items():
		if v==max1:
			zhongshu.append(k)
			continue
	return zhongshu
	
			
			
		
	
	
if __name__=='__main__':
	print u'l1的平均数为：'+str(average(l1))
	print u'l1的中位数为：'+str(among(l1))
	print u'l1的众数为：',zhong_shu(l1)





