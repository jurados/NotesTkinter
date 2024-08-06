import tkinter as tk
from tkinter import filedialog

class TextEditor():

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master=self.master, bd=2, relief='sunken')
        self.master.geometry('200x200')
        self.master.title('Text Editor')

        self.add_menu(self.master)
        self.text_box(self.master)

        self.frame.pack()

    def add_menu(self, master):
        menu_bar = tk.Menu(master)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New',command=self.new_file)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Close')
        file_menu.add_separator()
        file_menu.add_command(label='Exit',command=master.quit)
        
        master.config(menu=menu_bar)

    def text_box(self, master):
        self.text = tk.Text(master, height=20, width=60)
        self.scroll = tk.Scrollbar(master)
        
        self.scroll.pack(side='right', fill='y')
        self.text.pack(side='left', fill='y')

        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)
        self.text.pack()

    def new_file(self):
        self.text.delete('1.0', 'end')

    def open_file(self):
        self.text.delete('1.0', 'end')
        file_name = filedialog.askopenfilename(filetypes=[('Text Files','*.txt')])
        print(file_name)

        fobj = open(file_name, 'r')
        data = fobj.readlines()
        fobj.close()

        self.text.insert('end',data)

    def save_file(self):
        file_name = filedialog.asksaveasfile(filetypes=[('Text Files','*.txt')])
        data = self.text.get(1.0, 'end-1c') 
        print(file_name)

        fobj = open(file_name,'w')
        fobj.write(data)
        fobj.close()

if __name__ == '__main__':

    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()