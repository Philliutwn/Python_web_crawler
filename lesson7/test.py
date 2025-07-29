import tkinter as tk


def on_button_click():
    label = tk.Label(root, text = "Button clicked!")
    label.pack()


root = tk.Tk()

root.title("Python GUI Test")
root.geometry("400x300")

label = tk.Label(root, text = "Hello Tkinter",padx=10, pady=10, fg='red')
label.pack()
button = tk.Button(root, text = "Click me!", command = on_button_click)
button.pack()

root.mainloop()
