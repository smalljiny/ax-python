'''
sum : 183 , avg : 61.00
'''

num1, num2, num3 = map(int, input().split())

sum = num1 + num2 + num3
avg = sum / 3

print("sum :", sum, ", avg : %.2f" % avg)