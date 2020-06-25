import concurrent.futures
import time

number_list = [i for i in range(1,11)]

def add_item(x):
    result = count(x)
    return result

def count(number):
    for i in range(0,30000000):
        i += 1
    return i*number

if __name__ == '__main__':
    #单线程
    s = time.time()
    for item in number_list:
        print(add_item(item))
    print(time.time()-s)
    #多线程
    s2 = time.time()
    #创建5个线程
    with concurrent.futures.ThreadPoolExecutor(max_workers = 5 )as e:
        #调用这个函数，用一个列表的形式把这个函数给保存下来
        futuers = [e.submit(add_item,item) for item in number_list]
        #用叠带把这个函数的内容一个个打印出来
        for futuer in concurrent.futures.as_completed(futuers):
            print(futuer.result())
    print(time.time()-s2)
    #多进程
    s3 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5)as e:
        futuers = [e.submit(add_item, item) for item in number_list]
        for futuer in concurrent.futures.as_completed(futuers):
            print(futuer.result())
    print(time.time() - s3)