import keyboard
import time
from keyboard import press
import tkinter as tk
import tkinter
from tkinter import messagebox
a = []
a.append("#")
int_y = 50
nummer = []
#test
def the_best():
  global a
  x = entry2.get()
  if a != ["#"] or x != "":
    True_False = tkinter.messagebox.askyesno(title="continue?", message="Yes-Continue\nNo-Exit\n\nIt will start in 5 seconds")
    if True_False:  
      y = entry1.get()
      if y == "":
        timee = 0.4
      else:
        try:
          timee = float(y)
        except:
          timee = 0.4

      if x == "":
        pass
      else:
        c = x.split(' ')
        for i in range(len(c)):
          if c[i] == "":
            pass
          else:
            for h in c[i]:
              a.append(h)
          a.append(" ")
        a.append("#")

      time.sleep(5)
      for d in range(len(a)):
        if a[d] == "#":
          press("enter")
          time.sleep(timee)
        else:
          keyboard.write(" " + a[d] + " ")
          time.sleep(timee)
      if x == "":
        pass
      else:
        nummer.clear()
        for i in range(len(a)):
          if a[i] == "#":
            nummer.append(i)
        del a[nummer[-2]:nummer[-1]]
      entry2.delete(0 ,'end')
  else:
    ok = tkinter.messagebox.showinfo(title="Writer", message="Write enything")

def func(y):
  global int_y
  def button():
    global int_y
    nummer.clear()
    for i in range(len(a)):
      if a[i] == "#":
        nummer.append(i)
    try:
      button.destroy()
      entry3.destroy()
      int_y = int_y - 30
      del a[nummer[-2]:nummer[-1]]
    except:
      pass

  x = entry2.get()
  if x == "":
    pass
  else:
    c = x.split(' ')
    for i in range(len(c)):
      if c[i] == "":
        pass
      else:
        for h in c[i]:
          a.append(h)
      a.append(" ")
    a.append("#")
    int_y = int_y + 30
    entry3 = tk.Entry(width = 80)
    entry3.insert(0,x)
    entry3.place(x=0,y=int_y)
    button = tk.Button(text="Delete last line", command = button, bg = "red")
    button.place(x=307,y=40)
    entry2.delete(0 ,'end')
  
def func1():
  global int_y
  def button():
    global int_y
    nummer.clear()
    for i in range(len(a)):
      if a[i] == "#":
        nummer.append(i)
    try:
      button.destroy()
      entry3.destroy()
      int_y = int_y - 30
      del a[nummer[-2]:nummer[-1]]
    except:
      pass

  x = entry2.get()
  if x == "":
    pass
  else:
    c = x.split(' ')
    for i in range(len(c)):
      if c[i] == "":
        pass
      else:
        for h in c[i]:
          a.append(h)
      a.append(" ")
    a.append("#")
    int_y = int_y + 30
    entry3 = tk.Entry(width = 80)
    entry3.insert(0,x)
    entry3.place(x=0,y=int_y)
    button = tk.Button(text="Delete last line", command = button, bg = "red")
    button.place(x=307,y=40)
    entry2.delete(0 ,'end')
  
window = tk.Tk()
label2 = tk.Label(text="✔Your own writer", fg="green", font=20)
label2.place(x=0,y=0)

entry2 = tk.Entry(width = 80)
entry2.place(x=0,y=20)
entry2.focus()

label = tk.Label(text="Waiting time(In Seconds)")
label.place(x=0,y=40)

entry1 = tk.Entry(width = 12)
entry1.place(x=150,y=40)

button = tk.Button(text="Start", command = the_best, bg = "green")
button.place(x=270,y=40)

button = tk.Button(text="Enter", command = func1)
button.place(x=230,y=40)

def close_win(e):
   window.destroy()

window.bind('<Escape>', close_win)

window.geometry('500x600') 
window.bind('<Return>', func)
window.title('Writer') 
window.mainloop()
