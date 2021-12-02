'''除了字符串，Python还内置了多种类型的数据结构，如果要在程序中保存和操作数据，绝大多数时候可以利用现有的数据结构来实现，
最常用的包括列表、元组、集合和字典。
'''
'''刚才我们讲到的字符串类型（str）和之前我们讲到的数值类型（int和float）有一些区别。
数值类型是标量类型，也就是说这种类型的对象没有可以访问的内部结构；而字符串类型是一种结构化的、非标量类型，
所以才会有一系列的属性和方法。接下来我们要介绍的列表（list），也是一种结构化的、非标量类型，它是值的有序序列，
每个值都可以通过索引进行标识，定义列表可以将列表的元素放在[]中，多个元素用,进行分隔，
可以使用for循环对列表元素进行遍历，也可以使用[]或[:]运算符取出列表中的一个或多个元素。

下面的代码演示了如何定义列表、如何遍历列表以及列表的下标运算。'''
list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]

# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']

# 计算列表长度(元素个数)
print(len(list1)) # 5

# 下标(索引)运算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]

# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])

# 通过for循环遍历列表元素
for elem in list1:
    print(elem)

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)



'''下面的代码演示了如何向列表中添加元素以及如何从列表中移除元素。
'''
list1 = [1, 3, 5, 7, 100]

# 添加元素
list1.append(200) # [1, 3, 5, 7, 100, 200]
list1.insert(1, 400) # [1, 400, 3, 5, 7, 100, 200]

# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
	list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]

# 从指定的位置删除元素
list1.pop(0) # [400, 5, 7, 100, 200, 1000, 2000]
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]

# 清空列表元素
list1.clear()
print(list1) # []



'''和字符串一样，列表也可以做切片操作，
通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表，代码如下所示。'''
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango'] # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry

# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']

# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
print()



'''下面的代码实现了对列表的排序操作。
'''
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(list1)

# sorted函数返回列表排序后的拷贝不会修改传入的列表
list2 = sorted(list1)
print(list2) # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']

# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
print(list3) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']

# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list4) # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

list5 = sorted(list1, key=len, reverse=True)
print(list5) # ['internationalization', 'blueberry', 'orange', 'apple', 'zoo']

# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']

