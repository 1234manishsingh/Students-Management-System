import tkinter as tk
import pymysql

def fun1():
    global frame1
    frame1.destroy()
    import admin_login
def add_stud():
    global frame1
    global n1
    frame1.destroy()
    import add_student
    add_student.display(n1)
def all_stud():
    global frame1
    global n1
    frame1.destroy()
    import all_student
    all_student.display(n1)

def display(n):
    global frame1
    frame1=tk.Tk()
    frame1.geometry("600x400")
    frame1.title("Admin Profile")
    #frame.resizable(False,False)#Width,Height
    frame1.configure(background='#ffff00')
    var1=tk.StringVar()
    global n1
    n1=n
    var1.set(n)
    L1 = tk.Label(frame1, text="welcome" ,fg="white",bg="#262523",width=29 ,height=1,font=('times', 12, ' bold '))
    L1.place(relx=0, rely=0, relwidth=0.2, relheight=0.10)

    L2 = tk.Label(frame1, textvariable=var1 ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
    L2.place(relx=0.22, rely=0, relwidth=0.3, relheight=0.10)

    B1 = tk.Button(frame1, text="Logout" ,command=fun1,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 12, ' bold '))
    B1.place(relx=0.72, rely=0, relwidth=0.3, relheight=0.10)

    B2 = tk.Button(frame1, text="Add Student" ,command=add_stud ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
    B2.place(relx=0.25, rely=0.32, relwidth=0.5, relheight=0.10)
        
    B3 = tk.Button(frame1, text="All Student" ,command=all_stud ,fg="white",bg="#262523" ,width=29 ,height=1,font=('times', 16, ' bold '))
    B3.place(relx=0.25, rely=0.50, relwidth=0.5, relheight=0.10)
#main
