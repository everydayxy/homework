#*******************************************
#     My blog http://www.my-blog.top       #
#*******************************************
#     Python                               #
#     Version 3.6.3                        #
#*******************************************
#打印出100以内的斐波那契数列
a=int(0)
b=int(1)
n=int(0)
while n<=100: #限制条件
	n=a+b	#将上一次循环后a与b的和赋值给n
	a=b	#将b在本次循环中的值传给a
	b=n	#将本次循环中n的值传给b，这样就使a,b,n的值循环向前挤，使n的值为前两次的累加
	if n<100:
		print(n)
