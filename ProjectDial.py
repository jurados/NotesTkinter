import tkinter as tk

class Dial():

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master=self.master, bd=2, relief='sunken')
        self.master.geometry('200x200')
        self.master.title('Dial')

        self.frame.place(x=30, y=30)

        self.dial_grid()

    def dial_grid(self):
        values = '123456789#0*'
        index = 0
        for y in range(4):
            for x in range(3):
                self.btn = tk.Button(self.frame, text=values[index])
                self.btn.config(command=lambda index=index: self.click(values[index]))
                self.btn.grid(row=y,column=x)
                index = index + 1

    def click(self,index):
        print(index)

if __name__ == '__main__':

    root = tk.Tk()
    app = Dial(root)
    root.mainloop()