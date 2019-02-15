'''
Created on 2019年2月15日

@author: luowg
'''

print('hello')

num1 = input('请输入第一个数字:')
num2 = input('请输入第二个数字:')

sum1 = float(num1) + float(num2)

print('数字 {0} 和 {1} 相加结果为: {2}'.format(num1, num2, sum1))

num3 = float(input('请输入一个数字:'))

print('数字{0}平方结果:{1}'.format(num3,num3**2))
print('数字{0}平方根结果:{1:0.3f}'.format(num3,num3**0.5))