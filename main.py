from math import *
import numpy as np
def integral(xi,xf,n,func):
	times=1/n#(xf-xi)
	nums=np.arange(xi,xf,times)
	applay=np.vectorize(func)
	dots=applay(nums)
	return dots
def main():
	print("integral from")
	try:
		xi=int(input("from ...[default: 1]\n"))
	except:
		xi=1
	try:
		xf=int(input("end ... [default: 10]\n"))
	except:
		xf=10
	try:
		n=int(input("how many steps?...[default: 10]"))
	except:
		n=10
	try:
		funcs=input("please input your function on x:[default: x**2+sqrt(x)]\n")
		func=lambda x:eval(funcs)	
	except:
		func=lambda x:eval("x**2+sqrt(x)")
	#interpretate functios string to code  
	dots=integral(xi,xf,n,func)
	print(np.sum(dots)/n)
main()