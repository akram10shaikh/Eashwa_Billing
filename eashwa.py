from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Billing Slip")
root.geometry("1280x720")
bg_color = '#4D0039'

global l
l = []



c_name = StringVar()
c_phone = StringVar()
item = StringVar()
Rate = IntVar()
Quantity = IntVar()
bill_no = StringVar()
x = random.randint(1000,9999)
bill_no.set(str(x))


def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t Welcome Eashwa Retails")
    textarea.insert(END,f"\n\nBill Number : \t\t {bill_no.get()}")
    textarea.insert(END,f"\n Customer Name :\t\t {c_name.get()}")
    textarea.insert(END,f"\n Phone Number : \t\t {c_phone.get()}")
    textarea.insert(END,f"\n ==================================")
    textarea.insert(END,"\n Product Name \t\t QTY\t\tPrice")
    textarea.insert(END,f"\n ==================================\n")
    textarea.configure(font="arial 15 bold")

def additm():
    n = Rate.get()
    m = Quantity.get()*n
    l.append(m)
    if item.get() == '':
        messagebox.showerror("Error","Please Enter the Item")
    else:
        textarea.insert((10.0+float(len(l)-1)),f"{item.get()}\t\t{Quantity.get()}\t\t{m}\n")

def savebill():
    op = messagebox.askyesno("Save Bill","Do you wannt to save the bill")
    if op > 0:
        bill_details = textarea.get(1.0,END)
        f1 = open("bills/"+str(bill_no)+".txt",'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f"Bill no:{bill_no.get()} Saved Successfuly")
    else:
        return

def clear():
    c_name.set('')
    c_phone.set('')
    item.set('')
    Rate.set('')
    Quantity.set('')
    welcome()

def exit():
    op = messagebox.askyesno("Exit","Do you want to exit")
    if op > 0:
        root.destroy()


def gbill():
    if c_name.get() == '' or c_phone.get() == "":
        messagebox.showerror("Error","Customer Details are missing")
    else:
        tex = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END,tex)
        textarea.insert(END, f"\n ==================================")
        textarea.insert(END, f"Total Paybill Amont : \t\t{sum(l)}")
        textarea.insert(END, f"\n ==================================")
        savebill()


# ======================Top Section=============
title = Label(root, text="Billing Software",bg=bg_color,fg="white",font=('times new romman',25,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

# ======================Customer Details==============
F1 = LabelFrame(root,text='Customer Details',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,background=bg_color,fg="gold")
F1.place(x=0,y=80,relwidth=1)

cname_lbl = Label(F1, text='Customer Details',font=('times new rommon',18,'bold'),bg=bg_color,fg="white")
cname_lbl.grid(row=0,column=0,padx=10,pady=5)

cname_txt = Entry(F1,width=15,font=('arial',15,'bold'),relief=SUNKEN, textvariable=c_name)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cphone_lbl = Label(F1, text='Phone NO.',font=('times new rommon',18,'bold'),bg=bg_color,fg="white")
cphone_lbl.grid(row=0,column=2,padx=10,pady=5)

cphone_txt = Entry(F1,width=15,font=('arial',15,'bold'),relief=SUNKEN, textvariable=c_phone)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)

# ==================== Product Detail =========================

F2 = LabelFrame(root,text='Product Details',font=('times new rommon',18,'bold'),relief=GROOVE,bd=10,background=bg_color,fg="gold")
F2.place(x=20,y=180,width=630,height=500)

itm = Label(F2, text="Product Name",font=('times new rommon', 18, 'bold'),bg=bg_color,fg="lightgreen")
itm.grid(row=0,column=0,padx=30,pady=20)

itm_txt = Entry(F2, width=20,font=('arial',15,'bold'),textvariable=item)
itm_txt.grid(row=0,column=1,padx=30,pady=20)


rate = Label(F2, text="Product rate",font=('times new rommon', 18, 'bold'),bg=bg_color,fg="lightgreen")
rate.grid(row=1,column=0,padx=30,pady=20)

rate_txt = Entry(F2, width=20,font=('arial',15,'bold'),textvariable=Rate)
rate_txt.grid(row=1,column=1,padx=30,pady=20)



quantity = Label(F2, text="Product Quantity",font=('times new rommon', 18, 'bold'),bg=bg_color,fg="lightgreen")
quantity.grid(row=2,column=0,padx=30,pady=20)

quantity_txt = Entry(F2, width=20,font=('arial',15,'bold'),textvariable=Quantity)
quantity_txt.grid(row=2,column=1,padx=30,pady=20)

#======================== Button =============================

btn1 = Button(F2, text="Add item",font=("arial",15,"bold"),padx=5,pady=10,bg='lightgreen',width=15,command=additm)
btn1.grid(row=3,column=0,padx=10,pady=30)

btn2 = Button(F2, text="Generate Bill",font=("arial",15,"bold"),padx=5,pady=10,bg='lightgreen',width=15,command=gbill)
btn2.grid(row=3,column=1,padx=10,pady=30)

btn3 = Button(F2, text="Clear",font=("arial",15,"bold"),padx=5,pady=10,bg='lightgreen',width=15,command=clear)
btn3.grid(row=4,column=0,padx=10,pady=30)

btn4 = Button(F2, text="Exit",font=("arial",15,"bold"),padx=5,pady=10,bg='lightgreen',width=15,command=exit)
btn4.grid(row=4,column=1,padx=10,pady=30)

#=========================== Bill Area ========================

F3 = Frame(root, relief=GROOVE, bd=10)
F3.place(x=700,y=180,width=500,height=500)

bill_title = Label(F3,text="Bill Area",font=('arial',15,'bold'),bd=7,relief=GROOVE).pack(fill=X)
scroll_y = Scrollbar(F3,orient=VERTICAL)
textarea = Text(F3, yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()



root.mainloop()