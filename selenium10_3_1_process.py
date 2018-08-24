import multiprocessing
from time import ctime, sleep

"""多进程跟多线程的使用累相似，只需要用multiprocessing.Process替换threading.Thread就可以"""


# 创建进程类）
class MyProcess(multiprocessing.Process):
    def __init__(self, func, args):
        multiprocessing.Process.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


# 播放方法(播放文件， 播放时长， 播放次数)
def play(file, time):
    for i in range(2):
        print("开始播放：%s %s" % (file, ctime()))
        sleep(time)


if __name__ == '__main__':
    dicts = {'爱情买卖.mp3': 3, '阿凡达.mp4': 4, '我和你.mp3': 5}
    processes = []
    files = range(len(dicts))
    for file, time in dicts.items():
        t = MyProcess(play, (file, time))
        processes.append(t)

    for j in files:
        processes[j].start()
    for j in files:
        processes[j].join()
    print("结束播放 %s" % ctime())