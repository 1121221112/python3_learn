# -*- coding:utf-8 -*-
import time
import queue
import threading

q = queue.Queue(10)  # 生成一个队列，用来保存“包子”，最大数量为10


def productor(i):
    # 每2秒生产1份
    while True:
        q.put("厨师 %s 做的包子! " % i)
        time.sleep(2)


def consumer(j):
    # 每秒消费1次
    while True:
        print("顾客 %s 吃了一个 %s" % (j, q.get()))
        time.sleep(1)


for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()

for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()
