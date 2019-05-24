#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import tkMessageBox as mb

def main():
    global flag 
    flag = True

    def change_label_text():
        #nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
        #nonlocal在python3.x引入
        #nonlocal flag
        #在python中not是逻辑判断词，用于布尔型True和False，not True为False，not False为True        
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if mb.askokcancel('温馨提示','确定要退出吗'):
            top.quit()

    top = Tkinter.Tk()
    top.geometry('240x160')
    top.title('小游戏')
    label = Tkinter.Label(top, text='Hello,world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    panel = Tkinter.Frame(top)
    button1 = Tkinter.Button(panel, text='修改',command=change_label_text)
    button1.pack(side='left')
    button2 = Tkinter.Button(panel,text='退出',command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    Tkinter.mainloop()

if __name__ == '__main__':
    main()
