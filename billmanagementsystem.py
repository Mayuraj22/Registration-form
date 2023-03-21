from tkinter import *

root=Tk()
root.geometry("1000x600")
root.title("Bill Management System")
root.resizable(FALSE,FALSE)

def Reset():
    entry_dosa.delete(0,END)
    entry_coldcoffee.delete(0,END)
    entry_idli.delete(0,END)
    entry_momos.delete(0,END)
    entry_samosa.delete(0,END)
    entry_pizza.delete(0,END)
    entry_tea.delete(0,END)
    entry_vada.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(samosa.get())
    except:a2=0

    try:a3=int(idli.get())
    except:a3=0

    try:a4=int(vada.get())
    except:a4=0

    try:a5=int(momos.get())
    except:a5=0

    try:a6=int(pizza.get())
    except:a6=0

    try:a7=int(coldcoffee.get())
    except:a7=0

    try:a8=int(tea.get())
    except:a8=0
#define cost of each item per quantity
    c1=50*a1
    c2=20*a2
    c3=30*a3
    c4=30*a4
    c5=80*a5
    c6=150*a6
    c7=50*a7
    c8=20*a8

    

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,bg="black",fg="lightyellow")
    lbl_total.place(x=0,y=80)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightpink")
    entry_total.place(x=20,y=140)


    totalcost=c1+c2+c3+c4+c5+c6+c7+c8
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)
    print("Thanks for using this platform!")


Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#MENU CARD
f=Frame(root,bg="light yellow",highlightbackground="black",highlightthickness=1,width=300,height=420)
f.place(x=10,y=145)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="white").place(x=80,y=0)
Label(f,font=("Times new roman",15,"bold"),text="Samosa             Rs.20/plate",fg="black",bg="light yellow").place(x=10,y=90)
Label(f,font=("Times new roman",15,"bold"),text="Dosa                 Rs.50/plate",fg="black",bg="light yellow").place(x=10,y=120)
Label(f,font=("Times new roman",15,"bold"),text="Vada                 Rs.30/plate",fg="black",bg="light yellow").place(x=10,y=150)
Label(f,font=("Times new roman",15,"bold"),text="Idli                    Rs.30/plate",fg="black",bg="light yellow").place(x=10,y=180)
Label(f,font=("Times new roman",15,"bold"),text="Sandwich          Rs.40/plate",fg="black",bg="light yellow").place(x=10,y=210)
Label(f,font=("Times new roman",15,"bold"),text="Momos              Rs.80/plate",fg="black",bg="light yellow").place(x=10,y=240)
Label(f,font=("Times new roman",15,"bold"),text="Pizza                Rs.150/plate",fg="black",bg="light yellow").place(x=10,y=270)
Label(f,font=("Times new roman",15,"bold"),text="Cold Coffee      Rs.50/cup",fg="black",bg="light yellow").place(x=10,y=300)
Label(f,font=("Times new roman",15,"bold"),text="Tea                   Rs.10/cup",fg="black",bg="light yellow").place(x=10,y=330)

#BILL
f2=Frame(root,bd=5,highlightbackground="black",highlightthickness=1,width=300,height=370,bg="lightgreen")
f2.place(x=690,y=150)

Bill=Label(f2,text="BILL",font=('calibri',20,'bold'),bg="lightgreen")
Bill.place(x=120,y=30)


#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.place(x=320,y=145)

dosa=StringVar()
samosa=StringVar()
idli=StringVar()
vada=StringVar()
tea=StringVar()
coldcoffee=StringVar()
momos=StringVar()
pizza=StringVar()
Total_bill=StringVar()

#Label
lbl_samosa=Label(f1,font=("aria",20,'bold'),text="Samosa",width=12,fg="blue4")
lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lbl_vada=Label(f1,font=("aria",20,'bold'),text="Vada",width=12,fg="blue4")
lbl_idli=Label(f1,font=("aria",20,'bold'),text="Idli",width=12,fg="blue4")
lbl_momos=Label(f1,font=("aria",20,'bold'),text="Momos",width=12,fg="blue4")
lbl_pizza=Label(f1,font=("aria",20,'bold'),text="Pizza",width=12,fg="blue4")
lbl_coldcoffee=Label(f1,font=("aria",20,'bold'),text="Cold Coffee",width=12,fg="blue4")
lbl_tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=12,fg="blue4")

lbl_samosa.grid(row=1,column=0)
lbl_dosa.grid(row=2,column=0)
lbl_vada.grid(row=3,column=0)
lbl_idli.grid(row=4,column=0)
lbl_momos.grid(row=5,column=0)
lbl_pizza.grid(row=6,column=0)
lbl_coldcoffee.grid(row=7,column=0)
lbl_tea.grid(row=8,column=0)


#Entry
entry_samosa=Entry(f1,font=("aria",20,'bold'),textvariable=samosa,bd=6,width=8,bg="lightpink")
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_vada=Entry(f1,font=("aria",20,'bold'),textvariable=vada,bd=6,width=8,bg="lightpink")
entry_idli=Entry(f1,font=("aria",20,'bold'),textvariable=idli,bd=6,width=8,bg="lightpink")
entry_momos=Entry(f1,font=("aria",20,'bold'),textvariable=momos,bd=6,width=8,bg="lightpink")
entry_pizza=Entry(f1,font=("aria",20,'bold'),textvariable=pizza,bd=6,width=8,bg="lightpink")
entry_coldcoffee=Entry(f1,font=("aria",20,'bold'),textvariable=coldcoffee,bd=6,width=8,bg="lightpink")
entry_tea=Entry(f1,font=("aria",20,'bold'),textvariable=tea,bd=6,width=8,bg="lightpink")

entry_samosa.grid(row=1,column=1)
entry_dosa.grid(row=2,column=1)
entry_vada.grid(row=3,column=1)
entry_idli.grid(row=4,column=1)
entry_momos.grid(row=5,column=1)
entry_pizza.grid(row=6,column=1)
entry_coldcoffee.grid(row=7,column=1)
entry_tea.grid(row=8,column=1)

#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()