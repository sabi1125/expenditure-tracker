from tkinter import *
import sqlite3 as db
import tkinter as tk

root = Tk()
root.geometry("700x700")
root.title("spent")


#conn = db.connect("spent.db")
#cur = conn.cursor()
#sql = ("""create table expenses(
#    id INTEGER not null PRIMARY KEY ,
#    spent integer,
#    spent_on text,
#    date text
#    )""")

#cur.execute(sql)
#conn.commit()


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

#the ui for the entries

header = Label(root,text="Expenses tracker",padx=200,pady=50,bg="#607d8b",fg="white")
amount_l=Label(root,text="Amount spent: ")
amount = Entry(root,width=90)
spent_l=Label(root,text="Spent on: ")
spent = Entry(root,width=90)




#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

#the functions

#the create data function
def create():
    from datetime import date
    time = date.today()

    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = """insert into expenses (spent,spent_on,date) values(
        {},
        "{}",
        "{}"
    )""".format(amount.get(),spent.get(),time)

    cur.execute(sql)
    conn.commit()

    print("data created!")
    amount.delete(0,END)
    spent.delete(0,END)



#the show data function
def show():
        popup = tk.Toplevel()
        popup.geometry("100x100")
        popup.title("show")
        conn=db.connect("spent.db")
        cur=conn.cursor()
        sql ="""select * from expenses"""
        cur.execute(sql)
        conn.commit()

        record = cur.fetchall()
        data = ""
   
   
        for results in record:
            data += "id: "+ str(results[0]) + "\n" + "amount spent: " + str(results[1]) + "\n" + "spent on: " + str(results[2] + "\n"+ "date: ") + str(results[3])+"\n" 
    
        display = Label(popup,text=data)
        display.grid(row=8,column = 2)

#to show total 
def total():
    popup = tk.Toplevel()
    popup.geometry("100x100")
    popup.title("total")

    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = """select spent from expenses"""
    cur.execute(sql)
    conn.commit()
    record = cur.fetchall()
    total1 = 0
    for result in record:
        total1 += int(result[0])
    total2 = Label(popup,text = "Total: " + str(total1))
    total2.grid(row=3,column=2)




#to clear all the inputs

def clear():
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = """DELETE from expenses"""
    cur.execute(sql)
    conn.commit()
    print("all data cleared")

#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------

#buttons
submit = Button(
    root,
    text = "Submit",
    width=30,
    pady=20,
    border=0,
    bg="#0091ea",
    fg="white",
    command=create
    )

show_data = Button(
    root,
    text = "show expenses",
    width=30,
    pady=20,
    border=0,
    bg="#ffd600",
    fg="#616161",
    command=show
    )
total = Button(
    root,
    text = "total",
    width=30,
    pady=20,
    border=0,
    bg="#00796b",
    fg="white",
    command=total
    )
clear = Button(
    root,
    text = "clear all expenses",
    width=30,
    pady=20,
    border=0,
    bg="red",
    fg="white",
    command=clear
)



#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------


#display handlers

header.grid(row=1,column=2,pady=40)
amount_l.grid(row=3,column=1,pady=10)
amount.grid(row=3,column=2,pady=10)
spent_l.grid(row=4,column=1,pady=10)
spent.grid(row=4,column=2,pady=10)
submit.grid(row=5,column=2,pady=10)
show_data.grid(row=6,column=2,pady=10)
total.grid(row=7,column=2,pady=10)
clear.grid(row = 8,column=2,pady=10)
#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------

root.mainloop()