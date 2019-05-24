#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Person(object):
    
    def __init__(self, name, age):
        self._name = name
        self._age  = age

    # property装饰器的作用是把一个方法变成属性调用
    # 还可以定义只读属性，只定义getter方法不定义setter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <=16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('翠花', 12)
    person.play()
    age = person.age
    print(age)
       
if __name__ == '__main__':
    main() 
