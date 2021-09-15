# CRUD Application using with tkinter module
from tkinter import *
import pymysql
from tkinter import messagebox

def clear():
    sid.set('')
    sname.set('')
    saddress.set('')
    semail.set('')

def save():
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database="windowdb")
        cur=con.cursor()
        sql="insert into student values(%s,'%s','%s','%s')"\
             %(sid.get(),sname.get(),saddress.get(),semail.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("data saved successfully..")
    except:
        messagebox.showinfo("Error","Error In data.....")
    finally:
        clear()
def search():
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database="windowdb")
        cur=con.cursor()
        sql="select * from student where sid='%s'"%sid.get()
        cur.execute(sql)
        result=cur.fetchone()
        sname.set(result[1])
        saddress.set(result[2])
        semail.set(result[3])
        e1.configure(state='enable')
        messagebox.showinfo("Data Found............")
        con.close()
        
    except:
        messagebox.showinfo("No data Found....")
        
def update():
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database="windowdb")
        cur=con.cursor()
        sql="update student set sname='%s',saddress='%s',semail='%s' where sid=%s"%(sname.get(),saddress.get(),semail.get(),sid.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("data updated successfully..")
    except:
        messagebox.showinfo("Error","Error In data.....")
    finally:
        clear()
def delete():
    try:
        con=pymysql.connect(host='localhost',user='root',password='',database="windowdb")
        cur=con.cursor()
        sql="delete from student where sid='%s'"%(sid.get())
        cur.execute(sql)
        
        con.commit()
        con.close()
        messagebox.showinfo("data deleted successfully..")
    except:
        messagebox.showinfo("Error","Error In data.....")
    finally:
        clear() 


w1=Tk()
w1.title('My App')
w1.geometry('500x500')

sid=StringVar()
sname=StringVar()
saddress=StringVar()
semail=StringVar()
lb=Label(w1,text='REGISTRATION FORM')
l1=Label(w1, text='Student Id')
e1=Entry(w1, textvariable=sid)
l2=Label(w1, text='Student Name')
e2=Entry(w1, textvariable=sname)
l3=Label(w1, text='Student Address')
e3=Entry(w1, textvariable=saddress)
l4=Label(w1, text='Student Email')
e4=Entry(w1, textvariable=semail)
b1=Button(w1, text='Save', command=save)
b2=Button(w1, text='Display', command=search)
b4=Button(w1, text='Update', command=update)

b5=Button(w1,text='delete',command=delete)
b3=Button(w1, text='Clear', command=clear)
lb.place(x=50,y=50)
l1.place(x=50,y=100)
e1.place(x=200,y=100)

l2.place(x=50,y=150)
e2.place(x=200,y=150)

l3.place(x=50,y=200)
e3.place(x=200,y=200)

l4.place(x=50,y=250)
e4.place(x=200,y=250)

b1.place(x=50,y=300)
b3.place(x=100,y=300)
b2.place(x=150,y=300)

b4.place(x=200,y=300)
b5.place(x=250,y=300)

w1.mainloop()
