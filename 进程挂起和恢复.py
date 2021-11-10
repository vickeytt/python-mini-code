from multiprocessing import  Process
import keyboard,time,psutil

def fun1(name):
    i = 0
    while 1:
        print('测试%s多进程' %str(i))
        time.sleep(2)
        i +=1
def Suspended_thread(pid):
    pi = psutil.Process(pid)
    pi.suspend()  # 挂起进程
    print('挂起进程')

def Resume_thread(pid):
    pi = psutil.Process(pid)
    pi.resume()  # 恢复进程
    print('恢复进程')

if __name__ == '__main__':
    p = Process(target=fun1,args=('0',)) #实例化进程对象
    p.start()
    p.join()#利用多线程时，一般都先让子线程调用start() ，然后再去调用join()，让主进程等待子进程结束才继续走后续的逻辑
    print(p.pid)
    while 1:
        keyboard.wait('enter')#等待键盘回车输入
        Suspended_thread(p.pid)
        print(p.pid)

        keyboard.wait('space')
        Resume_thread(p.pid)
        print(p.pid)

