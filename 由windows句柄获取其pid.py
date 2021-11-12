import win32gui,win32process
def get_window_pid(title):
    hwnd = win32gui.FindWindow(None, title)
    threadid,pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid

if __name__ == "__main__":
    print(get_window_pid("CPE老化测试"))
