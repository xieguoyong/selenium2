import multiprocessing
import os
import time


def queue_input(queue):
    info = str(os.getpid()) + "(put)的信息, " + "在时间 " + str(time.time())
    queue.put(info)


def queue_output(queue, lock):
    info = queue.get()
    lock.acquire()
    print(str(os.getpid()) + "(get) —> " + info)
    lock.release()


if __name__ == '__main__':
    record1 = []
    record2 = []
    lock = multiprocessing.Lock()  # 加锁，防止散乱的打印
    queue = multiprocessing.Queue(3)

    for i in range(10):
        process = multiprocessing.Process(target=queue_input, args=(queue,))
        process.start()
        record1.append(process)

    for i in range(10):
        process = multiprocessing.Process(target=queue_output, args=(queue, lock))
        process.start()
        record2.append(process)

    for i in record1:
        i.join()
    queue.close()   # 没有更多的对象进来，关闭通道
    for i in record2:
        i.join()
