import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

import pymysql

def fun1():
    global frame1
    frame1.destroy()
    import admin_login
def fun2():
    global frame1
    global var1#userid
    global var2#msg
    global var3#name
    global var4#email
    global var5#phone
    global n1
    s1=var3.get()
    s2=var4.get()
    s3=var5.get()
    try:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='sohham')
        cur=conn.cursor()
        s4="select * from `friends` where `email`='"+s2+"' or `phone`='"+s3+"'"
        res1=cur.execute(s4)
        count=0
        for r1 in cur:
            count=count+1
        if(count>0):
            var2.set("Email or phone already exist")
        else:
            str1="INSERT INTO `friends` (`name`, `email`, `phone`) VALUES ('"+s1+"', '"+s2+"', '"+s3+"')"
            res=cur.execute(str1)
            conn.commit()#save change
            if(res):
                var2.set("inserted")
            else:
                var2.set("failed")
    except:
        var2.set("please check localhost/database")
def fun3():
    global frame1
    global n1
    frame1.destroy()
    import admin_profile
    admin_profile.display(n1)
def fun4():
    global frame1
    global n1
    global n2
    frame1.destroy()
    import edit_student
    edit_student.display(n1,n2)
def fun5():
    global frame1
    global n1
    global n2
    frame1.destroy()
    import delete_student
    delete_student.display(n1,n2)
def fun6():
    global frame1
    global n1
    global n2
    frame1.destroy()
    import display_student
    display_student.display(n1,n2)
def OnDoubleClick(iidd):
    global frame1
    global tv
    global n1
    global n2
    print(tv.item(tv.selection())['text'])
    n2=tv.item(tv.selection())['text']
    global root2
    root2 = Toplevel(frame1)
    root2.title("EDIT Delete Display Record")
    root2.geometry("250x100")
    root2.config(bg="white")
    B5=Button(root2, text="EDIT",command=fun4, bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),width=29 ,height=1)
    B5.place(relx=0, rely=0, relwidth=1, relheight=0.30)
    B6=Button(root2, text="DELETE",command=fun5, bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),width=29 ,height=1)
    B6.place(relx=0, rely=0.31, relwidth=1, relheight=0.30)
    B7=Button(root2, text="DISPLAY",command=fun6, bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),width=29 ,height=1)
    B7.place(relx=0, rely=0.62, relwidth=1, relheight=0.30)
    
    
def display(n):
    global frame1
    frame1=tk.Tk()
    frame1.geometry("600x400")
    frame1.title("All Student")
    #frame.resizable(False,False)#Width,Height
    frame1.configure(background='#f00fff')

    global var1
    global var2
    global var3
    global var4
    global var5
    global n1
    
    var1=tk.StringVar()
    var2=tk.StringVar()
    var3=tk.StringVar()
    var4=tk.StringVar()
    var5=tk.StringVar()
    var6=tk.StringVar()
    var1.set(n)
    n1=n
    
    L1 = tk.Label(frame1, text="welcome" ,fg="white",bg="#262523",width=29 ,height=1,font=('times', 12, ' bold '))
    L1.place(relx=0, rely=0, relwidth=0.2, relheight=0.10)

    L2 = tk.Label(frame1, textvariable=var1 ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
    L2.place(relx=0.22, rely=0, relwidth=0.3, relheight=0.10)

    B1 = tk.Button(frame1, text="Logout" ,command=fun1,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
    B1.place(relx=0.72, rely=0, relwidth=0.3, relheight=0.10)


    global frame2
        
    frame2 = tk.Frame(frame1, bg="#944dff")
    frame2.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.70)
    global tv
    tv= ttk.Treeview(frame2,height =13,columns = ('name','email','phone'))
    tv.column('#0',width=82)
    tv.column('name',width=160)
    tv.column('email',width=200)
    tv.column('phone',width=120)
    tv.grid(row=2,column=0,padx=(0,0),pady=(0,0),columnspan=4)
    tv.heading('#0',text ='ID')
    tv.heading('name',text ='NAME')
    tv.heading('email',text ='EMAIL')
    tv.heading('phone',text ='PHONE')

    try:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='sohham')
        cur=conn.cursor()
        s4="select * from `friends` order by `id` desc"
        res1=cur.execute(s4)
        for r1 in cur:
            iidd=str(r1[0])
            tv.insert('', 0, text=iidd, values=((str(r1[1]), str(r1[2]),str(r1[3]))))
            tv.bind("<Double-1>", OnDoubleClick)
        
    except:
        print("invalid")
        
    B3 = tk.Button(frame1, text="Back",command=fun3 ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
    B3.place(relx=0.25, rely=0.90, relwidth=0.5, relheight=0.10)

#display("nshm")
