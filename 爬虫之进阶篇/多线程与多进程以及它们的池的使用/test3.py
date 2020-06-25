from multiprocessing import Process,Queue

#写入进程
def write(q):
    print('Process to write：%s' %Process.pid)
    for i in range(10):
        print('Put %d to queue...' %i)
        q.put(i)
#读取进程
def read(q):
    print('Process to read:%s' % Process.pid)
    while True:
        value = q.get()
        print("read %d to queue..."%value)

if __name__ == '__main__':
    #创建一个队列
    q = Queue()
    #开始写入进程
    pw = Process(target=write,args=(q,))
    #开始读取进程
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
