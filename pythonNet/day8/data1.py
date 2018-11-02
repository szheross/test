from tkinter import *
from time import *
import threading

root = Tk()
root.title("大苏")
root.wm_attributes('-topmost',1) # 置顶桌面

text = Text(root, width=15, height=1, fg='red',font=("黑体",20,"bold"))
# insert的第一个参数为索引;第二个为添加的内容
text.tag_config("a",justify="center")
# text.insert(1.0, strftime("%H:%M:%S"),'a')


def fun_timer():
    text.insert(1.0, strftime("%H:%M:%S"), 'a')
    text.insert(1.8,'\n')
    global timer
    timer = threading.Timer(1, fun_timer)
    timer.start()
    timer.join()

timer = threading.Timer(1, fun_timer)
timer.start()



text.pack()
root.mainloop()
