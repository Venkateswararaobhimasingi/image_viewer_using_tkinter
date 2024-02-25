from tkinter import *
from PIL import ImageTk,Image
s=Tk()
s.title('image viewer')
c='red'
img1=ImageTk.PhotoImage(Image.open('img4.png'))
img2=ImageTk.PhotoImage(Image.open('imagetk.png'))
img3=ImageTk.PhotoImage(Image.open('welcomefriend.png'))
img4=ImageTk.PhotoImage(Image.open('img5.png'))
img5=ImageTk.PhotoImage(Image.open('img2.png'))
img6=ImageTk.PhotoImage(Image.open('img3.png'))
img7=ImageTk.PhotoImage(Image.open('img6.png'))

imglist=[img1,img2,img3,img4,img5,img6,img7]
label=Label(image=img1)
label.grid(row=0,column=0,columnspan=2)
status=Label(s,text='image 1 of '+str(len(imglist)),bd=1,relief=SUNKEN,anchor=E)


def forward(imgnum):
    global label,bf,bb
    label.grid_forget()
    label=Label(image=imglist[imgnum-1])
    bf=Button(s,text='>>',command=lambda:forward(imgnum+1))
    bb=Button(s,text='<<',command=lambda:backward(imgnum-1))
    status=Label(s,text='image'+str(imgnum)+' of '+str(len(imglist)),bd=1,relief=SUNKEN,anchor=E)
    if imgnum==7:
        bf=Button(s,text='>>',state=DISABLED)
    label.grid(row=0,column=0,columnspan=3)
    bb.grid(row=1,column=0)
    bf.grid(row=1,column=2)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
def backward(imgnum):
    global label,bf,bb
    label.grid_forget()
    label=Label(image=imglist[imgnum-1])
    bf=Button(s,text='>>',command=lambda:forward(imgnum+1))
    bb=Button(s,text='<<',command=lambda:backward(imgnum-1))
    status=Label(s,text='image'+str(imgnum)+' of '+str(len(imglist)),bd=1,relief=SUNKEN,anchor=E)
    if imgnum==1:
        bb=Button(s,text='>>',state=DISABLED)
    label.grid(row=0,column=0,columnspan=3)
    bb.grid(row=1,column=0)
    bf.grid(row=1,column=2)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    
bb=Button(s,text='<<',fg=c,command=backward,state=DISABLED)
bf=Button(s,text='>>',fg=c,command=lambda:forward(2))
be=Button(s,text='Exit',fg=c,command=s.destroy)
bb.grid(row=1,column=0)
bf.grid(row=1,column=2)
be.grid(row=1,column=1)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

s.mainloop()

