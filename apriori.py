import sys

#计数函数
def JiShu(K, keys):
	X = []
	for k1 in keys:
		c = 0
		for T in K:
			you = True
			for k in k1:
				if k not in T:
					you = False
			if you:
				c += 1
		X.append(c)
	return X


#剪枝函数
def JianZhi(keys, C, minSup, length,num):
	retKeys=[]
	for i, key in enumerate(keys):
		if len(key)==num:
			print(key,'---> Sup =',float(C[i]) / length, end ="")
			if float(C[i]) / length >= minSup:
				print(' --->',key,'是频繁项集')
			else:
				print()
		if float(C[i]) / length < minSup:
			pass
		else:
			retKeys.append(key)

	return retKeys


#连接函数
def Lianjie(keys):
	jieguo = []
	for k1 in keys:
		for k2 in keys:
			if k1 != k2:
				key = []
				for k in k1:
					if k not in key:
						key.append(k)
				for k in k2:
					if k not in key:
						key.append(k)
				key.sort()
				if key not in jieguo:
					jieguo.append(key)
	return jieguo


#Apriori算法
def Apri(D, minSup):
	C1 = {}
	for T in D:
		for I in T:
			if I in C1:
				C1[I] += 1
			else:
				C1[I] = 1
	keys1 = []
	for i in C1.keys():
		keys1.append([i])
	print('第',1,'次：')
	n = len(D)
	cutKeys1 = []
	for k in keys1[:]:
		if C1[k[0]]*1.0/n >= minSup:
			cutKeys1.append(k)
	cutKeys1.sort()
	keys = cutKeys1
	pfxj = []
	num=0
	while keys != []:
		num+=1
		C = JiShu(D, keys)
		if num!=1:
			print('第',num,'次：')
		cutKeys = JianZhi(keys, C, minSup, len(D),num)
		print('频繁',num,'项集：',cutKeys,'\n')
		for key in cutKeys:
			pfxj.append(key)
		keys = Lianjie(cutKeys)
	print("频繁项集为：",pfxj)
	return 0


Apri([['M','O','N','K','E','Y'],['D','O','N','K','E','Y'],['M','A','K','E'],['M','U','C','K','Y'],['C','O','O','K','I','E']], 0.6)

