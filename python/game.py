from tkinter import*
tk=Tk()
tk.title('Play with ball')
tk.resizable(0,0) 
tk.wm_attributes('-topmost',1)
canvas=Canvas(tk, width=1440,height=750,bd=0,highlightthickness=0)
canvas.pack()
ball=canvas.create_oval(710,365,730,385,fill='red',)
def playgame(event):
  if event.keysym == 'Up':
    canvas.move(ball,0,-2)
  elif event.keysym == 'Down':
    canvas.move(ball,0,2)
  elif event.keysym == 'Left':
    canvas.move(ball,-2,0)
  elif event.keysym == 'Right':
    canvas.move(ball,2,0)
canvas.bind_all('<KeyPress-Up>',playgame)
canvas.bind_all('<KeyPress-Down>',playgame)
canvas.bind_all('<KeyPress-Left>',playgame)
canvas.bind_all('<KeyPress-Right>',playgame)
def changecoluor(event):
  if event.keysym == 'b':
    canvas.itemconfig(ball,fill='blue')
  elif event.keysym == 'r':
    canvas.itemconfig(ball,fill='red')
  elif event.keysym == 'y':
    canvas.itemconfig(1,fill='yellow')
  elif event.keysym == 'p':
    canvas.itemconfig(ball,fill='pink')
  elif event.keysym == 'g':
    canvas.itemconfig(ball,fill='#FFD700')
canvas.bind_all('<KeyPress-b>',changecoluor)
canvas.bind_all('<KeyPress-r>',changecoluor)
canvas.bind_all('<KeyPress-y>',changecoluor)
canvas.bind_all('<KeyPress-p>',changecoluor)
canvas.bind_all('<KeyPress-g>',changecoluor)
