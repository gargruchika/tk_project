from Tkinter import *
from configuration import read_db_config
from mysql.connector import MySQLConnection,Error

WinStat =''
db = read_db_config()
conn = MySQLConnection(**db)
cursor = conn.cursor()


def stock():
    application.destroy()
    conn.close()
    import stockdetails
    a = stockdetails.stock()
    open_win()


def delstock():
    application.destroy()
    # login=sqlite.connect("grocery.sqlite")
    # l=login.cursor()
    conn.close()

    import stockdetails
    a = stockdetails.deletestock()

    open_win()






def again():  # for login window-----------------------------------------------------------------------------LOGIN WINDOW
    global ent1,ent2, flag,conn, root, apt, lblres, var1, var2
    if WinStat=='application':
        application.destroy()
    root = Tk()
    root.title('INDIAN GROCERY STORE')
    Label(root, text='INDIAN GROCERY STORE').grid(row=0, column=0, columnspan=5)
    Label(root, text="1602 ,MODEL TOWN,SECTOR 22C,YAMUNANAGAR").grid(row=1, column=0, columnspan=5)
    Label(root, text='--------------------------------------------------------------').grid(row=2, column=0,
                                                                                            columnspan=5)
    Label(root, text='Username').grid(row=3, column=1)
    ent1= Entry(root, width=10)
    ent1.grid(row=3, column=2)
    Label(root, text='Password').grid(row=4, column=1)
    ent2 = Entry(root, width=10, show="*")
    ent2.grid(row=4, column=2)
    lblres = Label(root, text=" ")
    lblres.grid(row=5,column=2)
    Label(root, text='').grid(row=5, column=0, columnspan=5)
    btn1 = Button(root, text="not registred yet", command=register)
    btn1.grid(row=7,column=1)
    Button(root, width=6, text='Enter', command=dblog).grid(row=6, column=1)
    Button(root, width=6, text='Close', command=root.destroy).grid(row=6, column=2)

    root.mainloop()


def register():
    global root
    root.destroy()
    root = Tk()
    root.geometry("400x400")
    root.title("register")
    global ent1
    global ent2
    global var
    global c
    global var1
    global var2
    var = StringVar()
    c = StringVar()
    var1 = StringVar()
    var2 = StringVar()

    lbl1 = Label(root, text="username")
    lbl1.place(x=100, y=80)

    ent1 = Entry(root)
    ent1.place(x=170, y=80)

    lbl2 = Label(root, text="password")
    lbl2.place(x=100, y=120)

    ent2 = Entry(root, show="*")
    ent2.place(x=170, y=120)

    btn = Button(root, text="register", command=dbreg)
    btn.place(x=200, y=300)

    root.mainloop()


def dbreg():
        try:
            db = read_db_config()
            conn = MySQLConnection(**db)
            print("connected succesfull with my data base")
            cursor = conn.cursor()
            qry = "insert into tbreg(regpwd,regnm)values(%s,%s)"
            args = ( ent2.get(), ent1.get())
            cursor.execute(qry, args)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        root.destroy()


def dblog():
    try:
        db = read_db_config()
        conn = MySQLConnection(**db)
        cursor = conn.cursor()
        qry = "select*from tbreg where regnm=%s and regpwd=%s"
        args = (ent1.get(), ent2.get())
        cursor.execute(qry, args)
        rows = cursor.fetchall()
        if cursor.rowcount == 0:
            lblres.configure(text="login failed")
        else:
            lblres.configure(text="login successfull")
            open_win()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def open_win():  # OPENS MAIN MENU----------------------------------------------------------------------------MAIN MENU
    global application, WinStat,ent1
    WinStat = 'application'
    application = Tk()
    application.title("INDIAN GROCERY STORE")
    Label(application, text="INDIAN GROCERY STORE").grid(row=0, column=0, columnspan=3)
    Label(application, text='*' * 80).grid(row=1, column=0, columnspan=3)
    Label(application, text='-' * 80).grid(row=3, column=0, columnspan=3)

    Label(application, text="Stock Maintenance").grid(row=2, column=0)
    Button(application, text='Add product to Stock', width=25, command=stock).grid(row=5, column=0)
    Button(application, text='Delete product from Stock', width=25,command = delstock).grid(row=6, column=0)

    Label(application, text="Access Database").grid(row=2, column=1)
    Button(application, text='Modify', width=15).grid(row=4, column=1)
    Button(application, text='Search', width=15).grid(row=5, column=1)
    Button(application, text='Expiry Check', width=15).grid(row=6, column=1)

    Label(application, text="Handle Cash Flows").grid(row=2, column=2)
    Button(application, text="Check Today's Revenue", width=20).grid(row=5, column=2)
    Button(application, text='Billing', width=20).grid(row=4, column=2)

    Label(application, text='-' * 80).grid(row=12, column=0, columnspan=3)
    Button(application, text='Logout', command=again).grid(row=13, column=2)
    application.mainloop()




again()