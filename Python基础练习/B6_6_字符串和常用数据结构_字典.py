'''字典是另一种可变容器模型，Python中的字典跟我们生活中使用的字典是一样一样的，它可以存储任意类型对象，
与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。
下面的代码演示了如何定义和使用字典。'''
# 创建字典的字面量语法
scores = {'Jerry': 95, 'Alex': 78, 'Mike': 82}
print(scores)               # {'Jerry': 95, 'Alex': 78, 'Mike': 82}

# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)            # {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))              # {'a': '1', 'b': '2', 'c': '3'}

# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}        # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(items1, items2, items3)

# 通过键可以获取字典中对应的值
print(scores['Jerry'])                  # 95
print(scores['Alex'])                   # 78

# 对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')      # Jerry: 95
                                        # Alex: 78
                                        # Mike: 82

# 更新字典中的元素
scores['Bob'] = 65
scores['Candi'] = 71
scores.update(Harry=67, Potter=85)
print(scores)                           # {'Jerry': 95, 'Alex': 78, 'Mike': 82, 'Bob': 65, 'Candi': 71, 'Harry': 67, 'Potter': 85}

if 'Lucy' in scores:
    print(scores['Lucy'])
print(scores.get('Lucy'))               # None

# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('Lucy', 60))           # 60

# 删除字典中的元素
print(scores.popitem())                 # ('Potter', 85) 取出最后一个
print(scores.popitem())                 # ('Harry', 67)
print(scores.pop('Jerry', 100))         # 95

# 清空字典
scores.clear()
print(scores)                           # {}
