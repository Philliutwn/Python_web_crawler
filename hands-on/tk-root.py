import tkinter as tk

def btn_pressed():
    myLabel = tk.Label(root,text="Happy Birthday!", fg='red', font=('Helvetica', 30))
    myLabel.pack()


root = tk.Tk()
root.title('oxxo studio')
root.geometry("600x300")

myLabel = tk.Label(root, text='Hello TkInter', fg='white', font=('Helvetica', 20), pady=30)
myLabel.pack()

myButton = tk.Button(root, text='OK', command = btn_pressed)
myButton.pack()



root.mainloop()

