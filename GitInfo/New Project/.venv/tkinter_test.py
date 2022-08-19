from tkinter import *
from tkinter import messagebox

root = Tk()

def btn_click():
    login = login_input.get()
    password = pass_field.get()

    info_str = f'Данные: {login},{password}'
    messagebox.showinfo(title='Yeho',message=info_str)

root['bg'] = '#fafafa'
root.title('Oh My!')
root.wm_attributes('-alpha',0.7)
root.geometry('300x250')

root.resizable(width=False,height=False)

canvas = Canvas(root,height=300,width=250)
canvas.pack()

frame = Frame(root,bg='red')
frame.place(relx=0.15,rely=0.15,relwidth=0.7,relheight=0.7)

my_title = Label(frame,text='Xaxa',bg='green',font=40)
my_title.pack()
btn = Button(frame,text='Push',bg='yellow',command=btn_click)
btn.pack()

login_input = Entry(frame,bg='white')
login_input.pack()

pass_field = Entry(frame,bg='white',show='*')
pass_field.pack()

root.mainloop()