import tkinter as tk
## learning from https://www.youtube.com/watch?v=ibf5cx221hk
# new series https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1
root = tk.Tk()
root.geometry("500x500")

label = tk.Label(root, text="hello world", font = ('Arial', 18))
label.pack(padx = 20, pady = 20)

# multi line entry
textbox = tk.Text(root, height = 3, font =('Arial', 16))
textbox.pack()

#single line entry
myentry = tk.Entry(root)
myentry.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 =tk.Button(buttonframe, text = "1", font = ('Arial', 18))
btn1.grid(row = 0, column = 0, sticky = tk.W+tk.E)


btn2 =tk.Button(buttonframe, text = "2", font = ('Arial', 18))
btn2.grid(row = 0, column = 1, sticky = tk.W+tk.E)


btn3 =tk.Button(buttonframe, text = "3", font = ('Arial', 18))
btn3.grid(row = 0, column = 2, sticky = tk.W+tk.E)


btn4 =tk.Button(buttonframe, text = "4", font = ('Arial', 18))
btn4.grid(row = 1, column = 0, sticky = tk.W+tk.E)

buttonframe.pack(fill = 'x')

root.mainloop()
