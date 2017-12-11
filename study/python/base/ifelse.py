import math
height = input('请输入身高:')
weight = input('请输入体重:')
bmi = float(weight)/math.pow(float(height),2)
if bmi>32:
	print('严重肥胖')
elif bmi>28:
	print('肥胖')
elif bmi>25:
	print('过重')
elif bmi>18.5:
	print('正常')
else :
	print('过轻')