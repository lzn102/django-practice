# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
# QtWidgets包含基本的组件.1:创建应用 2:自定义窗口 3:提示窗 4:显示按钮 5:退出消息提示 6:提供用户桌面信息(屏幕大小等)
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
# 1:自定义图标 2:自定义字体
from PyQt5.QtGui import QIcon, QFont
# QtCore是应用的核心. 1:包含事件的主循环,能添加或删除事件
from PyQt5.QtCore import QCoreApplication


# 创建基本窗口
def qt1():
    # 创建一个应用对象
    app = QApplication(sys.argv)

    # 用户界面基本控件,窗口的意思
    w = QWidget()
    # 定义窗口大小
    w.resize(200, 200)
    # 定义窗口的位置(在我们显示器上的位置)
    w.move(300, 300)
    # 定义窗口的标题
    w.setWindowTitle('hello world')
    # show()方法显示窗口到显示器
    w.show()

    # exec_()方法关闭应用
    sys.exit(app.exec_())


# 创建窗口图标
def qt2():
    # 创建类继承QWidget,以此引用它的方法
    class Example(QWidget):
        def __init__(self):
            # 初始化父类
            super().__init__()

            # 调用init_ui()方法
            self.init_ui()

        def init_ui(self):
            # 因为继承父类,直接调用setGeometry()方法,它可以同时设置窗口大小及位置
            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('hello world2')
            # 为窗口设置一个图标
            self.setWindowIcon(QIcon('web.png'))

            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 创建窗口标签
def qt3():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.init_ui()

        def init_ui(self):
            # 设置提示框的字体(提示框:鼠标放在指定位置显示一些提示信息),QFont指定字体和大小
            QToolTip.setFont(QFont('微软雅黑', 10))
            # 设置提示框的提示内容
            self.setToolTip('This is a <b>QWidget</b> widget')

            # 创建按钮
            btn = QPushButton('Button', self)
            # 设置按钮的提示框以及提示内容
            btn.setToolTip('This is a <b>QPushButton</b> widget')
            # 设置按钮大小,sizeHint()方法调取默认的按钮大小
            btn.resize(btn.sizeHint())
            # 设置按钮在窗口的位置
            btn.move(50,50)

            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('hello world3')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 为标签绑定事件(功能)
def qt4():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.init_ui()

        def init_ui(self):
            QToolTip.setFont(QFont('微软雅黑', 10))
            btn = QPushButton('Button', self)
            btn.setToolTip("Click it exit")
            # 将点击按钮事件绑定一个功能,这里绑定的是应用退出事件.(QCoreApplication创建一个实例并引用退出功能)
            btn.clicked.connect(QCoreApplication.instance().quit)
            btn.resize(btn.sizeHint())
            btn.move(50, 50)

            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('hello world4')
            self.show()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 退出时询问功能
def qt5():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.init_ui()

        def init_ui(self):
            self.setGeometry(300, 300, 300, 300)
            self.setWindowTitle('hello world5')
            self.show()

        # 当关闭窗口时,产生一个QCloseEvent事件.定义一个方法重定义该事件
        def closeEvent(self, event):
            # QMessage.question()方法创建一个消息盒子,询问用户是否退出,给出Yes和No选项,最后的参数表示默认选中的选项(这里是No)
            reply = QMessageBox.question(
                self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # 同意该事件
                event.accept()
            else:
                # 忽略该事件
                event.ignore()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 放置主窗口到屏幕中心
def qt6():
    class Example(QWidget):
        def __init__(self):
            super().__init__()

            self.init_ui()

        def init_ui(self):
            self.resize(300, 300)
            # 调用自己创建的屏幕居中方法
            self.center()
            self.setWindowTitle('hello world6')
            self.show()

        def center(self):
            # 获取主窗口的大小
            qr = self.frameGeometry()
            # QDesktopWidget()获取屏幕分辨率availableGeometry()根据分辨率找到屏幕中点
            cp = QDesktopWidget().availableGeometry().center()
            # 将主窗口的中心放到获取到的屏幕中心
            qr.moveCenter(cp)
            # 将创建的窗口左上角坐标移动到主窗口的左上角坐标
            self.move(qr.topLeft())

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


