from tkinter import *
import time

def mv():
    for i in range(120):
        w.move(text1, 10, 0)
        time.sleep(0.1);
        w.update()



root = Tk()
w = Canvas(root, width=500, height=500)
w.pack()
text1 = w.create_text(0, 250, text='王硕')
btn = Button(root, text='点击这里',command=mv)
btn.pack();
mainloop()


