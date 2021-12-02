'''我们还可以使用列表的生成式语法来创建列表，代码如下所示。
'''
import sys

f = [x for x in range(1, 10)]
print(f) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = [x + y for x in 'ABC' for y in '12345']
print(f) # ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5']

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 10)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数 184
print(f) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 10))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间 112
print(f)
for val in f:
    print(val)
'''
<generator object <genexpr> at 0x000002280C9A2BA0>
1
4
9
16
25
36
49
64
81
'''
print()



'''除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数。
下面的代码演示了如何实现一个生成斐波拉切数列的生成器。所谓斐波拉切数列可以通过下面递归的方法来进行定义'''
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()

