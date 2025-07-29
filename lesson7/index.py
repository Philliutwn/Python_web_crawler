#建立一個tkinter的基本樣板
#請使用物件導向的寫法來建立一個簡單的GUI應用程式
import tkinter as tk

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI App")
        self.root.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        
        #建立一個標籤
        self.label = tk.Label(self.root, text="股票即時資訊", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)
        
        #建立一個按鈕
        self.button = tk.Button(self.root, text="Click Me", width = 15, command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="你點擊了按鈕！")
        self.label.config(fg="red")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()

        
        
