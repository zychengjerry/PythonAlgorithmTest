'''
整型：Python中可以处理任意大小的整数（Python 2.x中有int和long两种类型的整数，但这种区分对Python来说意义不大，因此在Python 3.x中整数只有int这一种了），而且支持二进制（如0b100，换算成十进制是4）、八进制（如0o100，换算成十进制是64）、十进制（100）和十六进制（0x100，换算成十进制是256）的表示法。
浮点型：浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，浮点数除了数学写法（如123.456）之外还支持科学计数法（如1.23456e2）。
字符串型：字符串是以单引号或双引号括起来的任意文本，比如'hello'和"hello",字符串还有原始字符串表示法、字节字符串表示法、Unicode字符串表示法，而且可以书写成多行的形式（用三个单引号或三个双引号开头，三个单引号或三个双引号结尾）。
布尔型：布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来（例如3 < 5会产生布尔值True，而2 == 1会产生布尔值False）。
复数型：形如3+5j，跟数学上的复数表示一样，唯一不同的是虚部的i换成了j
'''
a = 321
b = 12
print(a + b)    # 333
print(a - b)    # 309
print(a * b)    # 3852
print(a / b)    # 26.75



'''在Python中可以使用type函数对变量的类型进行检查'''
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>



'''
上面的print函数中输出的字符串使用了占位符语法，
其中%d是整数的占位符，%f是小数的占位符，%%表示百分号
（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%），
字符串之后的%后面跟的变量值会替换掉占位符然后输出到终端中
'''
#a = int(input('a = '))
#b = int(input('b = '))
a, b = 5, 3
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))



'''
运算符          	描述

[] [:]          	下标，切片
**	                指数
~ + -	            按位取反, 正负号
* / % //	        乘，除，模，整除
+ -	                加，减
>> <<	            右移，左移
&	                按位与
^ |	                按位异或，按位或
<= < > >=	        小于等于，小于，大于，大于等于
== !=	            等于，不等于
is is not	        身份运算符
in not in	        成员运算符
not or and	        逻辑运算符
'''
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 算一下这里会输出什么



'''比较运算符和逻辑运算符'''
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False



'''练习1：华氏温度转换为摄氏温度。
'''
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# 在使用print函数输出时，也可以对字符串内容进行格式化处理，
# 上面print函数中的字符串%.1f是一个占位符，稍后会由一个float类型的变量值替换掉它。
# 同理，如果字符串中有%d，后面可以用一个int类型的变量值替换掉它，而%s会被字符串的值替换掉。
# 除了这种格式化字符串的方式外，还可以用下面的方式来格式化字符串，其中{f:.1f}和{c:.1f}可以先看成是{f}和{c}，
# 表示输出时会用变量f和变量c的值替换掉这两个占位符，后面的:.1f表示这是一个浮点数，小数点后保留1位有效数字
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')



'''练习2：输入圆的半径计算计算周长和面积。
'''
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)



'''练习3：输入年份判断是不是闰年。
'''
year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(is_leap)