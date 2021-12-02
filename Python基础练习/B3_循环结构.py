'''如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），
那么我们推荐使用for-in循环，例如下面代码中计算1~100求和的结果'''

sum = 0
for x in range(101):    # 0-100, 101个数字
    sum += x
print(sum)



'''
range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。'''

'''用for循环实现1~100之间的偶数求和
'''
sum = 0
for x in range(2, 101, 2):  #偶数
    sum += x
print(sum)

'''sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)'''

sum = 0
for x in range(1, 11, 2):   #奇数
    print(x)

for x in range(1,2,2):
    print(x)

'''
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。
while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True则继续循环；表达式的值为False则结束循环。'''
import random

answer = random.randint(1,100)
count = 0

while True:
    count += 1
    num = int(input('请输入：'))
    if num < answer:
        print('小了')
    elif num > answer:
        print('大了')
    else:
        print('恭喜你猜对了！')
        break
print('你总共猜了%d次' % count)
if count > 7:
    print('你是sb')



'''上面的代码中使用了break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，
这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。
除了break之外，还有另一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。

和分支结构一样，循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。
下面的例子演示了如何通过嵌套的循环来输出一个九九乘法表。'''

'''输出乘法口诀表(九九表)'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' % (i,j,i*j), end = '\t')
    print()



'''练习1：输入一个正整数判断是不是素数。'''
'''素数指的是只能被1和自身整除的大于1的整数。'''
import math

num = int(input('请输入一个正整数：'))
end = int(math.sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)



'''练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。'''
'''
两个数的最大公约数是两个数的公共因子中最大的那个数；
两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。'''
x = int(input('x = '))
y = int(input('y = '))

if x > y:
    x, y = y, x

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break



'''练习3：打印如下所示的三角形图案。'''
'''
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'''
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()