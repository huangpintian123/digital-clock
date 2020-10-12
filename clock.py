import tkinter as tk
import time,random,threading,os
#_init_
clock=tk.Tk()
clock.title('Clock')
clock.configure(bg='#000000')
clock.resizable(0,0)
# clock.iconbitmap('clock.ico')
#clock.overrideredirect(1)
type='time'
org=''
flag=True
img=[]
for _ in range(13):
	img.append(tk.PhotoImage(file='{}.png'.format(str(_))))
labels=[]
for _ in range(8):  #设定一共有8个数码管显示，包括两个小数点
	labels.append(tk.Label(clock,bg='#000000',image=img[_]))
	labels[_].pack(side='left')
#_def_
def closecl():  #用于安全退出
	clock.destroy()
	os._exit(0)
def display(s: object, st: object) -> object:
	global flag,labels,org
	#'1.012345'
	if org!=s:
		for _ in range(8):
			if s[_]=='.':
				if flag:
					labels[_].configure(image=img[11])
				else:
					labels[_].configure(image=img[12])
			else:
				labels[_].configure(image=img[int(s[_])])
		flag=not flag
		org=s
		time.sleep(st)
def main():
	global type
	while True:
		if type=='time':
			#sleeptime=0.6
			t=time.localtime()
			t='{}.{}.{}'.format(str(t[3]).zfill(2),str(t[4]).zfill(2),str(t[5]).zfill(2))
			display(t,0.9)
			t=time.time()

#_start_
thread=threading.Thread(target=main)
thread.start()
clock.protocol("WM_DELETE_WINDOW", closecl)
clock.mainloop()