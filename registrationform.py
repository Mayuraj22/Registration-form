from tkinter import *

root=Tk()
root.title("REGISTRATION FORM")
root.geometry("1000x700")
root.configure(bg="#E1EE14")

root.resizable(FALSE,FALSE)

def register():
  print("You have registered succesfully!")

Label(root,text="Student Registration Form", font="arial 25").pack(pady=50)
Label(text="Name",font=50).place(x=100,y=150)
Label(text="Father's Name ",font=50).place(x=100,y=200)
Label(text="Gender",font=50).place(x=100,y=250)
Label(text="Email",font=50).place(x=100,y=300)
Label(text="DOB",font=50).place(x=100,y=350)
Label(text="Address",font=50).place(x=100,y=400)
Label(text="Branch",font=50).place(x=100,y=450)


#entry
nameValue=StringVar()
phoneValue=StringVar()
genderValue=StringVar()
emailValue=StringVar()
dobValue=StringVar()
addressValue=StringVar()
designationValue=StringVar()


nameEntry=Entry(root,textvariable=nameValue,width=40,bd=2,font=30)
phoneEntry=Entry(root,textvariable=phoneValue,width=40,bd=2,font=30)
genderEntry=Entry(root,textvariable=genderValue,width=40,bd=2,font=30)
emailEntry=Entry(root,textvariable=emailValue,width=40,bd=2,font=30)
dobEntry=Entry(root,textvariable=dobValue,width=40,bd=2,font=30)
addressEntry=Entry(root,textvariable=addressValue,width=40,bd=2,font=30)
designationEntry=Entry(root,textvariable=designationValue,width=40,bd=2,font=30)

nameEntry.place(x=300,y=150)
phoneEntry.place(x=300,y=200)
genderEntry.place(x=300,y=250)
emailEntry.place(x=300,y=300)
dobEntry.place(x=300,y=350)
addressEntry.place(x=300,y=400)
designationEntry.place(x=300,y=450)

#check button
checkValue=IntVar
Checkbtn=Checkbutton(text="REAP",font=28,width=11,variable=checkValue)
Checkbtn.place(x=300,y=500)

Checkbtn=Checkbutton(text="LEAP",font=28,width=10, variable=checkValue)
Checkbtn.place(x=450,y=500)

Button(text="REGISTER", font=30,width=15,height=2,command=register).place(x=300,y=550)

root.mainloop()
