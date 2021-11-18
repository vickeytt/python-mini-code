from multiprocessing import Process
from watchdog.observers import Observer
from watchdog.events import *
import time

class thread(object):
    def __init__(self):
        self.ta = 0

    class FileEventHandler(FileSystemEventHandler):
        def __init__(self):
            FileSystemEventHandler.__init__(self)

        def on_moved(self, event):
            if event.is_directory:
                print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
            else:
                print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

        def on_created(self, event):
            if event.is_directory:
                print("directory created:{0}".format(event.src_path))
            else:
                print("file created:{0}".format(event.src_path))

        def on_deleted(self, event):
            if event.is_directory:
                print("directory deleted:{0}".format(event.src_path))
            else:
                print("file deleted:{0}".format(event.src_path))

        def on_modified(self, event):
            if event.is_directory:
                print("directory modified:{0}".format(event.src_path))
            else:
                print("file modified:{0}".format(event.src_path))
                print('到点睡觉啦')
                if ''.join(event.src_path.split('data_file_save\\')[1:]):
                    f = open(r"data_file_save\Countdown_program_can_be_started.txt", 'r')
                    line = f.read()
                    if line == '1':  # 如果Countdown_program_can_be_started.txt文件如果值为1，则测试界面已经走完设置IP + ping 通的第一轮测试，告诉该程可以执行计时重启
                        global t
                        t = 1
                        print(t)
                    f.close()


class thread2(object):
    def __init__(self):
        self.a = 'qwe'
    def put(self):
        print(self.a)

def run():
    observer = Observer()
    r = thread()
    event_handler = r.FileEventHandler()
    observer.schedule(event_handler, r"data_file_save", True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def run2(q):
        q.put()

if __name__ == "__main__":
    a = thread2()
    pw = Process(target=run, args=())  # 实例化进程对象
    pe = Process(target=run2, args=(a,))  # 实例化进程对象
    pw.start()
    pe.start()
    
    # pe进程里是死循环，无法等待其结束，只能强行终止:
    pw.join()
    # 等待pe结束:
    pe.join()

    print('kl')
