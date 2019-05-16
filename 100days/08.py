#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_tv(self):
        if self.age < 18:
            print('%s is watching xiongchumo' % self.name)
        else:
            print('%s is watching movie' % self.name)

def main():
    stu1 = Student('yangguo', 19)
    stu1.study('python lesson')
    stu1.watch_tv()

if __name__ == '__main__':
    main() 
