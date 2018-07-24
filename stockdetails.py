from Tkinter import *
from configuration import read_db_config
import mysql.connector
from mysql.connector import MySQLConnection,Error

columns=('Item_No', 'Item_Name', 'Item_Type', 'Quantity_Remain', 'Item_Cost', 'Expiry_Date','Manufactured_By')

db = read_db_config()
conn = MySQLConnection(**db)
cursor = conn.cursor()



def stock():
    global cursor, conn, columns, ent1,ent2,ent3,ent4,ent5,ent6,ent7,flag, sto, application,Item_no
    flag='sto'
    #value=['']*len(columns)
    sto=Tk()
    sto.title('ADD STOCK')
    Label(sto,text='ENTER NEW ITEM TOTO THE STOCK').grid(row=0,column=0,columnspan=2)
    Label(sto,text='-'*50).grid(row=1,column=0,columnspan=2)


    Label(sto, width=15, text=str(columns[1]) + ':', justify=LEFT).grid(row=4, column=0, sticky=W)
    ent1 = Entry(sto)
    ent1.grid(row=4, column=1)
    Label(sto, width=15, text=str(columns[2]) + ':', justify=LEFT).grid(row=5, column=0, sticky=W)
    ent2 = Entry(sto)
    ent2.grid(row=5, column=1)
    Label(sto, width=15, text=str(columns[3]) + ':', justify=LEFT).grid(row=6, column=0, sticky=W)
    ent3 = Entry(sto)
    ent3.grid(row=6, column=1)
    Label(sto, width=15, text=str(columns[4]) + ':', justify=LEFT).grid(row=7, column=0, sticky=W)
    ent4 = Entry(sto)
    ent4.grid(row=7, column=1)
    Label(sto, width=15, text=str(columns[5]) + ':', justify=LEFT).grid(row=8, column=0, sticky=W)
    ent5 = Entry(sto)
    ent5.grid(row=8, column=1)
    Label(sto, width=15, text=str(columns[6]) + ':', justify=LEFT).grid(row=9, column=0, sticky=W)
    ent6 = Entry(sto)
    ent6.grid(row=9, column=1)

    ref()
    Button(sto, width=15, text='Submit',command=chk).grid(row=12, column=1)
    Label(sto, text='-' * 165).grid(row=13, column=0, columnspan=7)
    #Button(sto, width=15, text='Refresh stock',command=ref).grid(row=12, column=4)
    for i in range(1,7):
        Label(sto,text=columns[i]).grid(row=14,column=i-1)

    Button(sto,width=10,text='Main Menu',command=mainmenu).grid(row=12,column=5)

    sto.mainloop()

def mainmenu():
    global sto
    sto.destroy()


def chk(): #checks if the medicine is already present so that can be modified
    global cursor, conn, value, sto,columns
    try:
        db = read_db_config()
        conn = MySQLConnection(**db)
        cursor = conn.cursor()
        #cursor.execute("select * from grocery")
        qry = "insert into grocery( Item_Name, Item_Type, Quantity_Remain, Item_Cost, Expiry_Date,Manufactured_By)values(%s,%s,%s,%s,%s,%s)"
        args=( ent1.get(),ent2.get(),ent3.get(), ent4.get(),ent5.get(), ent6.get())
        #qry = "insert into grocery values('%s','%s','%s','%s','%s','%s','%s')" % (y, x[1], x[2], x[3], x[4], x[5], x[6])
        cursor.execute(qry,args)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.execute("select * from grocery")
    #print(z)

    top=Tk()
    Label(top,width=20, text='Success!').pack()
    top.mainloop()
    #main_menu()


def deletestock():
    global cursor,sto, conn, flag, lb1, d,ent7
    # apt.destroy()
    flag = 'delsto'
    d = Tk()
    d.title("Delete grocery item from Stock")
    Label(d, text='Enter Item_Name to delete:').grid(row=0, column=0)
    ent7 = Entry(d, width=30)
    ent7.grid(row=0, column=1)
    #Label(d, text='', width=30, bg='white').grid(row=0, column=1)
    Label(d, text='Item').grid(row=2, column=0)
    Label(d, text='Qty Remain').grid(row=2, column=1)
    Label(d, text='Cost').grid(row=2, column=2)
    Label(d, text='Expiry Date').grid(row=2, column=3)

    displayren()
    b = Button(d, width=20, text='Delete', command=deletestockbutton).grid(row=0, column=3)
    b = Button(d, width=20, text='Main Menu', command=mainmenu).grid(row=5, column=3)
    d.mainloop()

def deletestockbutton():
    global p,conn,cursor,sto,d,ent7
    try:
        db = read_db_config()
        conn = MySQLConnection(**db)
        cursor = conn.cursor()
        qry = "delete from grocery where Item_Name=%s"
        args = (ent7.get(),)
        cursor.execute(qry, args)
        conn.commit()
        displayren()
    except Error as e:
        print(e)


def displayren():
    global lb1, d, cursor,sto, conn,ent7

    def onvsb(*args):
        lb1.yview(*args)
        lb2.yview(*args)

    index = 0
    vsb = Scrollbar(orient='vertical', command=onvsb)
    lb1 = Listbox(d, width=25, yscrollcommand=vsb.set)
    lb2 = Listbox(d, width=7, yscrollcommand=vsb.set)
    lb3 = Listbox(d, width=7, yscrollcommand=vsb.set)
    lb4 = Listbox(d, width=13, yscrollcommand=vsb.set)
    #vsb.grid(row=3, column=3)
    lb1.grid(row=3, column=0)
    lb2.grid(row=3, column=1)
    lb3.grid(row=3, column=2)
    lb4.grid(row=3, column=3)

    cursor.execute("select * from grocery")
    for i in cursor:
        index += 1
        lb1.insert(index, str(i[0]) + ')  ' + i[1])
        lb2.insert(index, i[3])
        lb3.insert(index, i[4])
        lb4.insert(index, i[5])
    conn.commit()


def ref():  # creates a multi-listbox manually to show the whole database
    global sto, conn, cursor

    def scrollbarv(*args):
        lb1.yview(*args)
        lb2.yview(*args)
        lb3.yview(*args)
        lb4.yview(*args)
        lb5.yview(*args)
        lb6.yview(*args)
    index=0
    sc_bar=Scrollbar(orient='vertical',command=scrollbarv)
    lb1 = Listbox(sto, yscrollcommand=sc_bar.set)
    lb2 = Listbox(sto, yscrollcommand=sc_bar.set)
    lb3 = Listbox(sto, yscrollcommand=sc_bar.set, width=7)
    lb4 = Listbox(sto, yscrollcommand=sc_bar.set, width=7)
    lb5 = Listbox(sto, yscrollcommand=sc_bar.set, width=20)
    lb6 = Listbox(sto, yscrollcommand=sc_bar.set, width=20)
    sc_bar.grid(row=15, column=6)
    lb1.grid(row=15, column=0)
    lb2.grid(row=15, column=1)
    lb3.grid(row=15, column=2)
    lb4.grid(row=15, column=3)
    lb5.grid(row=15, column=4)
    lb6.grid(row=15, column=5)
    cursor.execute("select * from grocery")
    for i in cursor:
            #print(i)
            index += 1
            lb1.insert(index,str(i[0]) + '. ' + str(i[1]))
            lb2.insert(index,i[2])
            lb3.insert(index,i[3])
            lb4.insert(index,i[4])
            lb5.insert(index,i[5])
            lb6.insert(index,i[6])
    conn.commit()

def mainmenu():
    if flag=='sto':
        sto.destroy()
    elif flag=='delsto':
        d.destroy()

#stock()