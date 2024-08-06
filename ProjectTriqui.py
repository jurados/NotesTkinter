import tkinter as tk

class Triqui():

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master=self.master)
        self.master.geometry('200x200')
        self.master.title('Tic Tac Toe')
        self.button_list = []
        self.current_player = 0

        self.frame.pack()

        self.gameboard()

    def gameboard(self):
        index = 0
        for y in range(0,3):
            for x in range(0,3):
                btn = tk.Button(self.frame, text=' ', width=5, height=3,
                                command=lambda index=index:self.click(index))
                btn.grid(row=y, column=x, sticky='nsew')
                index = index + 1
                self.button_list.append(btn)

    def click(self, index):
        print('Click ' + str(index))
    
        if self.current_player == 0:
            self.button_list[index].config(text='X')
            self.current_player = 1
        else:
            self.button_list[index].config(text='O')
            self.current_player = 0

if __name__ == '__main__':

    root = tk.Tk()
    app = Triqui(root)
    root.mainloop()