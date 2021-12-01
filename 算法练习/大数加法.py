from _typeshed import Self


class Solution:
    def add(self, num1, num2):
        return int(num1) + int(num2)

    a = int(input('a = '))
    b = int(input('b = '))
    print(add(Self,a,b))