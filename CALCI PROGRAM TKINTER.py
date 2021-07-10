# GUI Development using Tkinter
import tkinter as tk

app = tk.Tk()

app.geometry('340x310')

app.title("Calculator")
entry = tk.Entry(app,text='0',font=('arial',20,'normal'))
entry.place(x=20,y=15)

def number(n):

	if n=="C":
		entry.delete(0,'end')
	
	elif n=="ans":
		k2 = entry.get()
		entry.delete(0,'end')
		entry.insert('end',eval(k2))

	elif n=='del':
		entry.delete(len(entry.get())-1)

	else:
		entry.insert('end',n)

one_button = tk.Button(app,text = "7",font=('arial',10,'bold'),command = lambda:number(7),width = 6).place(x=30,y=70)
one_button = tk.Button(app,text = "8",font=('arial',10,'bold'),command = lambda:number(8),width = 6).place(x=100,y=70)
one_button = tk.Button(app,text = "9",font=('arial',10,'bold'),command = lambda:number(9),width = 6).place(x=170,y=70)
one_button = tk.Button(app,text = "+",font=('arial',10,'bold'),command = lambda:number('+'),width = 6).place(x=250,y=70)

one_button = tk.Button(app,text = "4",font=('arial',10,'bold'),command = lambda:number(4),width = 6).place(x=30,y=120)
one_button = tk.Button(app,text = "5",font=('arial',10,'bold'),command = lambda:number(5),width = 6).place(x=100,y=120)
one_button = tk.Button(app,text = "6",font=('arial',10,'bold'),command = lambda:number(6),width = 6).place(x=170,y=120)
one_button = tk.Button(app,text = "-",font=('arial',10,'bold'),command = lambda:number('-'),width = 6).place(x=250,y=120)

one_button = tk.Button(app,text = "1",font=('arial',10,'bold'),command = lambda:number(1),width = 6).place(x=30,y=170)
one_button = tk.Button(app,text = "2",font=('arial',10,'bold'),command = lambda:number(2),width = 6).place(x=100,y=170)
one_button = tk.Button(app,text = "3",font=('arial',10,'bold'),command = lambda:number(3),width = 6).place(x=170,y=170)
one_button = tk.Button(app,text = "*",font=('arial',10,'bold'),command = lambda:number('*'),width = 6).place(x=250,y=170)

one_button = tk.Button(app,text = "C",font=('arial',10,'bold'),command = lambda:number("C"),width = 6).place(x=30,y=220)
one_button = tk.Button(app,text = "0",font=('arial',10,'bold'),command = lambda:number(0),width = 6).place(x=100,y=220)
one_button = tk.Button(app,text = "=",font=('arial',10,'bold'),command = lambda:number('ans'),width = 6).place(x=170,y=220)
one_button = tk.Button(app,text = "/",font=('arial',10,'bold'),command = lambda:number('/'),width = 6).place(x=250,y=220)

one_button = tk.Button(app,text = ".",font=('arial',10,'bold'),command = lambda:number('.'),width = 6).place(x=30,y=270)
one_button = tk.Button(app,text = "00",font=('arial',10,'bold'),command = lambda:number("00"),width = 6).place(x=100,y=270)
one_button = tk.Button(app,text = "del",font=('arial',10,'bold'),command = lambda:number('del'),width = 6).place(x=170,y=270)


app.mainloop()
