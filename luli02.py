# -*- coding: UTF-8 -*-
__metaclass__=type


by_string=['a','e','i','o','u']
words=['suzhou','shanghai','hangzhou','nanjing','beijng']

result={}
for word in words:
	n=[]
	for char in word:
		if char in by_string:
			n.append(by_string.index(char))
		else:
			n.append(9)
	result[word]=n
print result
			
vs=result.values()	
print vs
vs.sort()
print vs	

sorted_words=[]

for i in vs:
	for k,v in result.items():
		if v==i:
			sorted_words.append(k)
print sorted_words
	







