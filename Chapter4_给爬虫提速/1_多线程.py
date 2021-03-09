# 进程：资源单位，一个进程里至少要有一个线程
# 线程：执行单位

# def func():
#     for i in range(1000):
#         print("func", i)
#
#
# if __name__ == "__main__":
#     func()
#     for i in range(1000):
#         print("main", i)

# 多线程
from threading import Thread  # 线程类


# 多线程第一种写法
# def func():
#     for i in range(1000):
#         print("func", i)
#
#
# if __name__ == "__main__":
#     t = Thread(target=func)  # 创建线程并给线程安排任务
#     t.start()  # 多线程状态为可以开始工作状态，具体的执行时间由cpu决定
#     for i in range(1000):
#         print("main", i)


# 多线程第二种写法
class MyThread(Thread):
    def run(self):  # 固定写法 -> 当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print("子线程", i)


if __name__ == "__main__":
    t = MyThread()
    t.start()  # 开启线程

    for i in range(1000):
        print("主线程", i)
