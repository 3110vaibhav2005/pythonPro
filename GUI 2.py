from tkinter import*
a_root = Tk()

#lable
b=Label(text="Hello User...")
b.pack()

A=Label(text='This is SpiderMan Interface...')
A.pack()

#Image
a_root.geometry("1400x800")
photo = PhotoImage(file="spider-man-far-from-home-2019-1600x900_949564-mm-90.png")
c = Label(image=photo)
c.pack()



a_root.mainloop()
