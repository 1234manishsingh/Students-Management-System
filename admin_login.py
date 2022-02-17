import tkinter as tk
import pymysql

def fun1():
    v1=E1.get()
    v2=E2.get()
    if(v1==""  or v2==""):
        var1.set("please filled properly")
    else:
        try:
            conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='sohham')
            cur=conn.cursor()
            s1="select * from admin where userid='"+v1+"' and password='"+v2+"'"
            res=cur.execute(s1)
            if res:
                #var1.set("weldone")
                frame1.destroy()
                import admin_profile
                admin_profile.display(v1)
                
            else:
                var1.set("invalid login details")
        except:
            var1.set("cannot connect to localhost")


frame1=tk.Tk()
frame1.geometry("600x400")
frame1.title("Admin Login")
#frame.resizable(False,False)#Width,Height
frame1.configure(background='#ffff00')

frame2 = tk.Frame(frame1, bg="#944dff")
frame2.place(relx=0.30, rely=0.12, relwidth=0.40, relheight=0.76)

L1 = tk.Label(frame2, text="Adminid" ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
L1.place(relx=0, rely=0, relwidth=1, relheight=0.10)

E1 = tk.Entry(frame2, text="" ,fg="black" ,width=29,font=('times', 16, ' bold '))
E1.place(relx=0, rely=0.13, relwidth=1, relheight=0.10)

L2 = tk.Label(frame2, text="Password" ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
L2.place(relx=0, rely=0.26, relwidth=1, relheight=0.10)

E2 = tk.Entry(frame2, text="",show="*" ,fg="black" ,width=29,font=('times', 16, ' bold '))
E2.place(relx=0, rely=0.39, relwidth=1, relheight=0.10)

B1 = tk.Button(frame2, text="Login" ,fg="white",bg="#262523",command=fun1 ,width=29,height=1,font=('times', 16, ' bold '))
B1.place(relx=0, rely=0.52, relwidth=1, relheight=0.10)

var1=tk.StringVar()


L3 = tk.Label(frame2,textvariable=var1,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
L3.place(relx=0, rely=0.65, relwidth=1, relheight=0.10)

frame1.mainloop()
