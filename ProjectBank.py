import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simple App')
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)
        
        frame_1 = InputFrom(self)
        frame_1.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        
        frame_2 = InputFrom(self)
        frame_2.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
        
class InputFrom(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        
        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky='ew')
        self.entry.bind('<Return>', lambda event: self.add_to_list())
        
        self.entry_btn_1 = ttk.Button(self, text='Add', command=self.add_to_list)
        self.entry_btn_1.grid(row=0, column=1)
        self.entry_btn_2 = ttk.Button(self, text='Clear', command=self.clear_list)
        self.entry_btn_2.grid(row=0, column=2)
        
        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
    def add_to_list(self):
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)
            
    def clear_list(self):
        self.text_list.delete(0, tk.END)
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()