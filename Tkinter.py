from tkinter import *

window = Tk()
window.title("MY GUI WINDOW!!")
#window.geometry("800x600")
# label["text"] = 로 변경가능


a = 0
def downNumber():
    global a
    a -= 1
    print("다운버튼")
    text_box.delete("1.0", END)
    text_box.insert(index="1.0", chars=str(a))

def upNumber():
    global a
    a += 1
    print("업버튼")
    text_box.delete("1.0", END)
    text_box.insert(index="1.0", chars=str(a))

label = Label(window, text=a, font=('Arial',25))


text_box = Text(master=window, font=('Arial',50), width=20, height=10)
button1 = Button(
    master=window,
    text="DOWN",
    width=20,
    height=10,
    command=downNumber
)

button2 = Button(
    master=window,
    text="UP",
    width=20,
    height=10,
    command=upNumber
)
button1.grid(row=0, column=0, padx=5, pady=5)
text_box.grid(row=0, column=1)
button2.grid(row=0, column=2)
#button1.pack(fill=BOTH, expand=True)

window.mainloop()