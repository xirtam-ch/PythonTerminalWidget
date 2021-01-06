import sys

# print(sys.argv[0])
if(len(sys.argv) != 4):
	print("用法：zhai 正股价 转股价 债面值")
else:
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
	x = c/(c/b*a)-1
	print("转股溢价率"+str(x * 100)+"%")