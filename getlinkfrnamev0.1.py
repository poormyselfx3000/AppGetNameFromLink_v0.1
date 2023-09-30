from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("app get name from link ver 0.1")
root.minsize(1080, 480)  
root.geometry("300x300+50+50")
root.configure(background="pink")

def xuly_dulieu():
    Link = LayLink.get()
    chuoi_tach = Link.split(".com/")[0] 
    chuoi_tach = chuoi_tach.split("https://www.")[-1]
    chuoi_tach = chuoi_tach.split("https://")[-1] 
    messagebox.showinfo("đây là web \/",chuoi_tach)
    print(chuoi_tach)

cauhoi = Label(root, text="hãy nhập link của một trang web để có thể lấy tên",bg = "pink")
cauhoi.pack()

LayLink = Entry(root,width=50) 
LayLink.pack()

nut_GetLink = Button(root, text="nhấn vào đây để get name",bg = "lightblue",command = xuly_dulieu)
nut_GetLink.pack()






root.mainloop()