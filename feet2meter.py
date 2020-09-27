from tkinter import *
windows=Tk()
windows.title("feet to meter conversion")
windows.configure(background="blue")
windows.geometry("300x220")
windows.resizable(width=False,height=False)

def convert():
    value=float(ft_value.get())
    meter=value*0.3048
    mt_value.set("%.4f" %meter)

def clear():
    ft_value.set("")
    mt_value.set("")

ft_lbl=Label(windows,text="feet",bg="red",fg="white",width=10)
ft_lbl.grid(column=0,row=0,padx=10,pady=10)


ft_value=DoubleVar()
ft_Entry=Entry(windows,textvariable=ft_value,width=15)
ft_Entry.grid(column=1,row=0,padx=10)
ft_Entry.delete(0,'end')


mt_label=Label(windows,text="meter",bg="red",fg="white",width=10)
mt_label.grid(column=0,row=1,pady=15)

mt_value=DoubleVar()
mt_Entry=Entry(windows,textvariable=mt_value,width=15)
mt_Entry.grid(column=1,row=1,padx=10)
mt_Entry.delete(0,'end')

convert_btn=Button(windows,text="convert",bg="black",fg="white",width=15,command=convert)
convert_btn.grid(column=0,row=3,padx=14)

clear_btn=Button(windows,text="clear",bg="green",fg="black",width=15,command=clear)
clear_btn.grid(column=1,row=3,padx=15)

windows.mainloop()
