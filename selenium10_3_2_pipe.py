import multiprocessing


def pipe_a(pipe):
    pipe.send('hello b')
    print("pipe a rev: ", pipe.recv())


def pipe_b(pipe):
    pipe.send('hello too a')
    print("pipe b rev: ", pipe.recv())


if __name__ == '__main__':
    multiprocessing.freeze_support()
    pipe = multiprocessing.Pipe()
    a = multiprocessing.Process(target=pipe_a, args=(pipe[0],))
    b = multiprocessing.Process(target=pipe_b, args=(pipe[1],))
    a.start()
    b.start()
    a.join()
    b.join()
