from tkinter import *
import time

root = Tk()
root.title("大苏")
root.geometry("200x30+1200+50")
root.wm_attributes('-topmost',1) # 置顶桌面

# def date_time():
#     top = Toplevel()
#     top.geometry("200x30+1200+110")
#     top.title('时间')
#     Button(top, text=time.strftime("%H:%M:%S")).pack(side=TOP, anchor=W, fill=X, expand=YES)
#
# Button(root,text='显示',command=date_time).pack(side=TOP, anchor=W, fill=X, expand=0)

Button(root,text= time.strftime("%H:%M:%S")).pack(side=TOP, anchor=W, fill=X, expand=0)
time.sleep(1)
Button(root,text= time.strftime("%H:%M:%S")).pack(side=TOP, anchor=W, fill=X, expand=0)



root.mainloop()

