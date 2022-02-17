import tkinter as tk
import pymysql

def fun1():
    global frame1
    frame1.destroy()
    import admin_login
def fun2():
    global frame1
    global n2
    try:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='sohham')
        cur=conn.cursor()
        s4="delete from `friends` where `id`='"+n2+"'"
        res1=cur.execute(s4)
        conn.commit()#save change
        if(res1):
            fun3()
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
def display(n,n3):
    global frame1
    frame1=tk.Tk()
    frame1.geometry("600x400")
    frame1.title("Delete Student")
    #frame.resizable(False,False)#Width,Height
    frame1.configure(background='#f00fff')

    global var1
    global var2
    global var3
    global var4
    global var5
    global n1
    global n2
    
    var1=tk.StringVar()
    var2=tk.StringVar()
    var3=tk.StringVar()
    var4=tk.StringVar()
    var5=tk.StringVar()
    var6=tk.StringVar()
    var1.set(n)
    n1=n
    n2=n3
    try:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='sohham')
        cur=conn.cursor()
        s4="select * from `friends` where `id`='"+n3+"'"
        res1=cur.execute(s4)
        for x in cur:
            var3.set(x[1])
            var4.set(x[2])
            var5.set(x[3])
    except:
        var2.set("please check localhost/database")


    
    L1 = tk.Label(frame1, text="welcome" ,fg="white",bg="#262523",width=29 ,height=1,font=('times', 12, ' bold '))
    L1.place(relx=0, rely=0, relwidth=0.2, relheight=0.10)

    L2 = tk.Label(frame1, textvariable=var1 ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
    L2.place(relx=0.22, rely=0, relwidth=0.3, relheight=0.10)

    B1 = tk.Button(frame1, text="Logout" ,command=fun1,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
    B1.place(relx=0.72, rely=0, relwidth=0.3, relheight=0.10)


    global frame2
        
    frame2 = tk.Frame(frame1, bg="#944dff")
    frame2.place(relx=0.30, rely=0.15, relwidth=0.40, relheight=0.70)

    L3 = tk.Label(frame2, text="Name" ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
    L3.place(relx=0, rely=0, relwidth=1, relheight=0.10)

    E3 = tk.Entry(frame2, text="",textvariable=var3 ,fg="black" ,width=29,font=('times', 16, ' bold '))
    E3.place(relx=0, rely=0.11, relwidth=1, relheight=0.10)

    L4 = tk.Label(frame2, text="Email" ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
    L4.place(relx=0, rely=0.22, relwidth=1, relheight=0.10)

    E5 = tk.Entry(frame2, text="",textvariable=var4 ,fg="black" ,width=29,font=('times', 16, ' bold '))
    E5.place(relx=0, rely=0.33, relwidth=1, relheight=0.10)

    L5 = tk.Label(frame2, text="Phone" ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
    L5.place(relx=0, rely=0.44, relwidth=1, relheight=0.10)

    E6 = tk.Entry(frame2, text="",textvariable=var5 ,fg="black" ,width=29,font=('times', 16, ' bold '))
    E6.place(relx=0, rely=0.55, relwidth=1, relheight=0.10)

    B4 = tk.Button(frame2, text="Yes" ,fg="white",bg="#262523" ,width=29, command=fun2 ,height=1,font=('times', 16, ' bold '))
    B4.place(relx=0.02, rely=0.66, relwidth=0.45, relheight=0.10)
    B5 = tk.Button(frame2, text="No" ,fg="white",bg="#262523" ,width=29, command=fun3 ,height=1,font=('times', 16, ' bold '))
    B5.place(relx=0.48, rely=0.66, relwidth=0.45, relheight=0.10)

    L6 = tk.Label(frame2, textvariable=var2 ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
    L6.place(relx=0, rely=0.77, relwidth=1, relheight=0.10)

        
        
    B3 = tk.Button(frame1, text="Back",command=fun3 ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
    B3.place(relx=0.25, rely=0.90, relwidth=0.5, relheight=0.10)

#display("nshm",2)
