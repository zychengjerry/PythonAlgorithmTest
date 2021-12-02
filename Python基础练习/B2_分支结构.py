'''
在Python中，要构造分支结构可以使用if、elif和else关键字。
所谓关键字就是有特殊含义的单词，像if和else就是专门用于构造分支结构的关键字，很显然你不能够使用它作为变量名
（事实上，用作其他的标识符也是不可以）。下面的例子中演示了如何构造一个分支结构。'''
username = input('请输入用户名: ')
password = input('请输入口令: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')



'''缩进可以使用任意数量的空格，但通常使用4个空格，
建议大家不要使用制表键或者设置你的代码编辑工具自动将制表键变成4个空格。'''
'''
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)'''
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))



'''练习1：英制单位英寸与公制单位厘米互换。
'''
value = float(input('请输入长度: '))
unit = input('请输入单位: ')
if unit == 'in' or unit == '英寸':
    print('%.2f英寸 = %.2f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')



'''练习2：百分制成绩转换为等级制成绩。
如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；
60分以下输出E。'''
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是: ', grade)



'''练习3：输入三条边长，如果能构成三角形就计算周长和面积。
'''
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5     # 上面使用的通过边长计算三角形面积的公式叫做'海伦公式'
    print('面积: %f' % (area))
else:
    print('不能构成三角形')
