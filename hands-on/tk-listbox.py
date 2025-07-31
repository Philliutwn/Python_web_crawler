import tkinter as tk

root = tk.Tk()
root.title("oxxo studio")
root.geometry("600x400")

# header label
headerLabel = tk.Label(root,text='股市即時資訊',pady=20,font=('Helvetica', 20))
headerLabel.pack()


# left frame
frame = tk.Frame(root,width=300, height=400,relief=tk.GROOVE,border=2, bg='black')
frame.pack_propagate(False)
frame.pack(side=tk.LEFT,padx=10, pady=50)


lang:list =["Python", "Java", "C++", "Swift", "Kotlin", "Dart", "C#", "PHP", "JavaScript", "Ruby", "Go", "R", "Julia"]
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, yscrollcommand=True)

for item in lang:
    listbox.insert(tk.END, item)

listbox.pack(side=tk.LEFT, padx=10)

# scroller in left listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# left frame label
selectedItem = tk.StringVar()
selectedItem.set(listbox.curselection())
print('selected item = ',selectedItem)
lblSelItem = tk.Label(frame, text= "Selected stock", font=('Helvetica', 12),bg='yellow')
lblSelItem.pack(side=tk.TOP, anchor='w',padx=10, pady=10)

root.mainloop()


