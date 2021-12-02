'''输入M和N计算C(M,N)
'''
'''方程 x1 + x2 + x3 + x4 = 8 有多少组正整数解。上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案'''
m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
print(fm // fn // fm_n)



'''在Python中可以使用def关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的。
在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，
程序中函数的参数就相当于是数学上说的函数的自变量，而函数执行完成后我们可以通过return关键字来返回一个值，这相当于数学上说的函数的因变量。

在了解了如何定义函数后，我们可以对上面的代码进行重构，所谓重构就是在不影响代码执行结果的前提下对代码的结构进行调整，重构之后的代码如下所示。'''
def fac(num):
    # 求阶乘
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

#m = int(input('m = '))
#n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(fac(m) // fac(n) // fac(m - n))



'''Python的math模块中其实已经有一个名为factorial函数实现了阶乘运算，事实上求阶乘并不用自己定义函数。
下面的例子中，我们讲的函数在Python标准库已经实现过了，我们这里是为了讲解函数的定义和使用才把它们又实现了一遍，实际开发中并不建议做这种低级的重复劳动。'''
from math import factorial as fact
print(fact(m) // fact(n) // fact(m - n))
print()



'''函数是绝大多数编程语言中都支持的一个代码的"构建块"，但是Python中的函数与其他语言中的函数还是有很多不太相同的地方，
其中一个显著的区别就是Python对函数参数的处理。在Python中，函数的参数可以有默认值，也支持使用可变参数，
所以Python并不需要像其他语言一样支持函数的重载，因为我们在定义一个函数的时候可以让它有多种不同的使用方式，下面是两个小例子。'''
from random import randint

def roll_dice(n=2):
    # 摇色子
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

def add(a=0, b=0, c=0):
    # 三个数相加
    return a + b + c

# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))



'''其实上面的add函数还有更好的实现方案，因为我们可能会对0个或多个参数进行加法运算，而具体有多少个参数是由调用者来决定，
我们作为函数的设计者对这一点是一无所知的，因此在不确定参数个数的时候，我们可以使用可变参数，代码如下所示。'''
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))



'''用模块管理函数
'''
'''
也可以按照如下所示的方式来区分到底要使用哪一个foo函数。

test.py

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
但是如果将代码写成了下面的样子，那么程序中调用的是最后导入的那个foo，因为后导入的foo覆盖了之前导入的foo。

test.py

from module1 import foo
from module2 import foo

# 输出goodbye, world!
foo()
'''



'''需要说明的是，如果我们导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，
这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"。'''
#module3.py
def foo():
    pass

def bar():
    pass

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()

#test.py
#import module3
# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__



'''练习1：实现计算求最大公约数和最小公倍数的函数。
'''
def gcd(x, y):
    # 求最大公约数
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    # 求最小公倍数 
    return x * y // gcd(x, y)



'''练习2：实现判断一个数是不是回文数的函数。
'''
def is_palindrome(num):
    # 判断一个数是不是回文数
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num



'''练习3：实现判断一个数是不是素数的函数。
'''
def is_prime(num):
    # 判断一个数是不是素数
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False



'''练习4：写一个程序判断输入的正整数是不是回文素数。
'''
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)

# 通过上面的程序可以看出，当我们将代码中重复出现的和相对独立的功能抽取成函数后，
# 我们可以组合使用这些函数来解决更为复杂的问题，这也是我们为什么要定义和使用函数的一个非常重要的原因。



'''最后，我们来讨论一下Python中有关变量作用域的问题。
'''
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined

if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()


'''上面的代码能够顺利的执行并且打印出100、hello和True，但我们注意到了，在bar函数的内部并没有定义a和b两个变量，那么a和b是从哪里来的。
我们在上面代码的if分支中定义了一个变量a，这是一个全局变量（global variable），属于全局作用域，因为它没有定义在任何一个函数中。
在上面的foo函数中我们定义了变量b，这是一个定义在函数中的局部变量（local variable），属于局部作用域，在foo函数的外部并不能访问到它；
但对于foo函数内部的bar函数来说，变量b属于嵌套作用域，在bar函数中我们是可以访问到它的。bar函数中的变量c属于局部作用域，在bar函数之外是无法访问的。
事实上，Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，前三者我们在上面的代码中已经看到了，
所谓的“内置作用域”就是Python内置的那些标识符，我们之前用过的input、print、int等都属于内置作用域。'''


'''我们可以使用global关键字来指示foo函数中的变量a来自于全局作用域，如果全局作用域中没有a，那么下面一行的代码就会定义变量a并将其置于全局作用域。
同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，可以使用nonlocal关键字来指示变量来自于嵌套作用域，请大家自行试验。'''
def foo():
    global a    # 使用global关键字来指示foo函数中的变量a来自于全局作用域
    a = 200
    print(a)  # 200

if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200



'''在实际开发中，我们应该尽量减少对全局变量的使用，因为全局变量的作用域和影响过于广泛，可能会发生意料之外的修改和使用，
除此之外全局变量比局部变量拥有更长的生命周期，可能导致对象占用的内存长时间无法被垃圾回收。
事实上，减少对全局变量的使用，也是降低代码之间耦合度的一个重要举措，同时也是对迪米特法则的践行。
减少全局变量的使用就意味着我们应该尽量让变量的作用域在函数的内部，但是如果我们希望将一个局部变量的生命周期延长，
使其在定义它的函数调用结束后依然可以使用它的值，这时候就需要使用闭包，这个我们在后续的内容中进行讲解。

说明： 很多人经常会将“闭包”和“匿名函数”混为一谈，但实际上它们并不是一回事，
如果想了解这个概念，可以看看维基百科的解释或者知乎上对这个概念的讨论。

说了那么多，其实结论很简单，从现在开始我们可以将Python代码按照下面的格式进行书写，
这一点点的改进其实就是在我们理解了函数和作用域的基础上跨出的巨大的一步。
'''
def main():
    # Todo: Add your code here
    pass

if __name__ == '__main__':
    main()
