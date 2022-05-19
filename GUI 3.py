from tkinter import*
a=Tk()
a.geometry("12000x800")
a.minsize(500,300)
a.maxsize(1600,900)

b=Label(text="FreeFire.")
b.pack()

c=PhotoImage(file="WIP-6th-anniversary-wallpaper-dark")
d=Label(image=c)
d.pack()
a.mainloop()
