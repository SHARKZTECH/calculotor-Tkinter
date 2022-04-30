from tkinter import *
window=Tk()
window.title("calculator")


e=Entry(window,width=50,borderwidth=5)
e.grid(column=0,row=0,columnspan=4,padx=10,pady=10)

def btnclick(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def btnClear():
    e.delete(0,END)
def add():
    firstnumber=e.get()
    global f_num
    global yafe
    yafe="addition"
    f_num=int(firstnumber)
    e.delete(0,END)
def sub():
    firstnumber=e.get()
    global f_num
    global yafe
    yafe="subtraction"
    f_num=int(firstnumber)
    e.delete(0,END)
    
def mult():
    firstnumber=e.get()
    global f_num
    global yafe
    yafe="multplication"
    f_num=int(firstnumber)
    e.delete(0,END)
    
def div():
    firstnumber=e.get()
    global f_num
    global yafe
    yafe="divition"
    f_num=int(firstnumber)
    e.delete(0,END)
    

def equall():
    secondnumber=e.get()
    secondnumber=int(secondnumber)
    e.delete(0,END)
    if yafe=="addition":
        e.insert(0,f_num+secondnumber)
    elif yafe=="subtraction":
        e.insert(0,f_num-secondnumber)
    elif yafe=="multplication":
        e.insert(0,f_num*secondnumber)
    elif yafe=="divition":
        e.insert(0,f_num/secondnumber)
    
btn1=Button(window,text="1",width=10,height=3,command=lambda : btnclick(1))
btn2=Button(window,text="2",width=10,height=3,command=lambda : btnclick(2))
btn3=Button(window,text="3",width=10,height=3,command=lambda : btnclick(3))
btn4=Button(window,text="4",width=10,height=3,command=lambda : btnclick(4))
btn5=Button(window,text="5",width=10,height=3,command=lambda : btnclick(5))
btn6=Button(window,text="6",width=10,height=3,command=lambda : btnclick(6))
btn7=Button(window,text="7",width=10,height=3,command=lambda : btnclick(7))
btn8=Button(window,text="8",width=10,height=3,command=lambda : btnclick(8))
btn9=Button(window,text="9",width=10,height=3,command=lambda : btnclick(9))
btn0=Button(window,text="0",width=10,height=3,command=lambda : btnclick(0))
btnclear=Button(window,text="clear",width=10,height=3,command=btnClear)
btnequall=Button(window,text="=",width=10,height=3,command=equall)
btnadd=Button(window,text="+",width=10,height=3,bg="gray",command=add)

btnsub=Button(window,text="-",width=10,height=3,bg="gray",command=sub)
btnmult=Button(window,text="x",width=10,height=3,bg="gray",command=mult)
btndiv=Button(window,text="/",width=10,height=3,bg="gray",command=div)

btn1.grid(column=0,row=3,padx=5,pady=3)
btn2.grid(column=1,row=3,padx=5,pady=3)
btn3.grid(column=2,row=3,padx=5,pady=3)
btnmult.grid(column=3,row=3,padx=5,pady=3)

btn4.grid(column=0,row=2,padx=5,pady=3)
btn5.grid(column=1,row=2,padx=5,pady=3)
btn6.grid(column=2,row=2,padx=5,pady=3)
btnsub.grid(column=3,row=2,padx=5,pady=3)

btn7.grid(column=0,row=1,padx=5,pady=3)
btn8.grid(column=1,row=1,padx=5,pady=3)
btn9.grid(column=2,row=1,padx=5,pady=3)
btnadd.grid(column=3,row=1,padx=5,pady=3)

btn0.grid(column=0,row=4,padx=5,pady=3)
btnclear.grid(column=1,row=4,padx=5,pady=3)
btndiv.grid(column=2,row=4,padx=5,pady=3)
btnequall.grid(column=3,row=4,padx=5,pady=3)

window.maxsize()
window.mainloop()

