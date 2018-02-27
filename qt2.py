# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# 1:设置标签 2:水平布局盒子 3:垂直布局盒子 4:表格布局盒子 5:行编辑器 6:文本编辑器
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


# 坐标布局(限制多)
def qt1():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.initui()

        def initui(self):

            # 设置标签,输入标签说明和放置标签的窗口
            lb1 = QLabel('坐标位置1', self)
            # 将标签放置在窗口的坐标位置处(左上角为0,0.向下向右为正)
            lb1.move(15, 10)

            lb2 = QLabel('坐标位置2', self)
            lb2.move(35, 40)

            lb3 = QLabel('坐标位置3', self)
            lb3.move(55, 70)

            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('hello world')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 盒子布局(一般用)
def qt2():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.initui()

        def initui(self):
            button1 = QPushButton('YES')
            button2 = QPushButton('NO')

            # 创建一个水平布局
            hbox = QHBoxLayout()
            # 布局内每个元素的间隔设置为1
            hbox.addStretch(1)
            # 布局内添加组件,这里是创建的按钮
            hbox.addWidget(button1)
            hbox.addWidget(button2)

            # 创建一个垂直布局
            vbox = QVBoxLayout()
            # 弹性元素把所有的元素放在窗口右下角
            vbox.addStretch(1)
            # 布局内添加布局,这里是创建的水平布局
            vbox.addLayout(hbox)

            # 为窗口创建布局
            self.setLayout(vbox)
            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('hello world2')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 栅格布局(常用)
def qt3():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.initui()

        def initui(self):
            # 创建一个栅格布局
            grid = QGridLayout()
            # 将布局放置在窗口上
            self.setLayout(grid)

            # 设定所有按钮的名称
            names = ['cls', 'bck', '', 'close',
                    '7', '8', '9', '/',
                    '4', '5', '6', '*',
                    '1', '2', '3', '-',
                    '0', '.', '=', '+' ]

            # 设置按钮的位置坐标,[(0,0),(0,1),(0,2),(0,3),(1,0)......(4,3)],共16个
            positions = [(i,j) for i in range(5) for j in range(4)]
            # 遍历两个列表,zip函数包含两个可迭代的参数,这里是坐标和名字
            for position, name in zip(positions, names):
                # 如果名字是空的就跳过创建按钮,窗口上显示的是空白而不是空的按钮
                if name == '':
                    continue
                # 分别创建16个按钮并且赋予名称
                button = QPushButton(name)
                # 将按钮和对应的位置添加到创建的栅格布局, *position表示传入的参数是一个元组
                grid.addWidget(button, *position)

            self.move(300, 150)
            self.setWindowTitle('hello world3')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 布局实例(文本编辑)
def qt4():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.initui()

        def initui(self):
            title = QLabel('Title')
            author = QLabel('Author')
            review = QLabel('Review')

            # 创建行编辑器
            t_edit = QLineEdit()
            a_edit = QLineEdit()
            # 创建文本编辑器
            r_edit = QTextEdit()

            # 设置栅格布局
            grid = QGridLayout()
            # 设置标签之间的空间距离
            grid.setSpacing(10)

            # 添加标签和编辑器,分别设置坐标
            grid.addWidget(title, 1, 0)
            grid.addWidget(t_edit, 1, 1)

            grid.addWidget(author, 2, 0)
            grid.addWidget(a_edit, 2, 1)

            grid.addWidget(review, 3, 0)
            grid.addWidget(r_edit, 3, 1, 5, 1)

            # 将栅格布局设为窗口布局
            self.setLayout(grid)
            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('hello world4')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

qt4()