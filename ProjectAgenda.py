import tkinter as tk

class Agenda():

    def __init__(self, master):

        self.master = master
        self.master.title('Agenda')
        self.master.geometry('700x500')
        self.color_background = '#006'
        self.color_text = '#FFF'
        self.master.config(background=self.color_background)

        self.name = tk.StringVar()
        self.surname = tk.StringVar()
        self.email = tk.StringVar()
        self.phone = tk.StringVar()
        self.erase = tk.StringVar()
        
        self.title_label = tk.Label(self.master, text='My Application',
                                    fg=self.color_text, bg=self.color_background).place(x=270, y=10)
    
        self.users_list = []
    
    def app_widgets(self):

        ########################################################
        self.name_label = tk.Label(self.master, text='Name',
                                   fg=self.color_text, bg=self.color_background)
        self.name_label.place(x=50, y=50)
        self.entry_1 = tk.Entry(self.master, textvariable=self.name)
        self.entry_1.place(x=150, y=50)

        self.surname_label = tk.Label(self.master, text='Surname',
                                   fg=self.color_text, bg=self.color_background)
        self.surname_label.place(x=50, y=80)
        self.entry_2 = tk.Entry(self.master, textvariable=self.surname)
        self.entry_2.place(x=150, y=80)

        ########################################################
        self.email_label = tk.Label(self.master, text='Email',
                                   fg=self.color_text, bg=self.color_background)
        self.email_label.place(x=50, y=140)
        self.entry_3 = tk.Entry(self.master, textvariable=self.email)
        self.entry_3.place(x=150, y=140)
        
        self.phone_label = tk.Label(self.master, text='Phone',
                                   fg=self.color_text, bg=self.color_background)
        self.phone_label.place(x=50, y=170)
        self.entry_4 = tk.Entry(self.master, textvariable=self.phone)
        self.entry_4.place(x=150, y=170)
        
        self.erase_label = tk.Label(self.master, text='Phone',
                                   fg=self.color_text, bg=self.color_background)
        self.erase_label.place(x=370, y=50)
        
        ########################################################
        spin_phone = tk.Spinbox(self.master, textvariable=self.erase)
        spin_phone.place(x=450, y=50)

        ########################################################
        btn_save = tk.Button(self.master, text='Save',
                             fg='white', bg="#009",
                             command=self._save)
        btn_save.place(x=180, y=200)
        
        ########################################################
        btn_delete = tk.Button(self.master, text='Delete',
                               fg='white', bg="#009",
                               command=self._delete)
        btn_delete.place(x=490, y=80)
    
    def _save(self):
        name = self.name.get()
        surname = self.surname.get()
        email = self.email.get()
        phone = self.phone.get()
        
        self.users_list.append(f'{name}_{surname}_{email}_{phone}')
        self._write_contact()
        
        name = self.name.set("")
        surname = self.surname.set("")
        email = self.email.set("")
        phone = self.phone.set("")
        
        self._consult()
        
    def _delete(self):
        eraser_content = self.erase.get()
        remove = False
        
        for user in self.users_list:
            element = user.split('_')
            if eraser_content == element[3]:
                self.users_list.remove(user)
                remove = True
        
        self.write_contact()
        self._consult()
        
        if remove:
            tk.messagebox.showinfo('Eliminate', 'Element eliminated' + ' ' + eraser_content)
            
    def _consult(self):
        new_user = tk.Text(self.master, width=80, height=15)
        self.users_list.sort()
        values = []
        new_user.insert('insert', 'Name\tSurname\t\tEmail\tPhone\n')
        
        for user in self.users_list:
            element = user.split('_')
            values.append(element[3])
            new_user.insert('insert',f'{element[0]}\t{element[1]}\t{element[2]}\t{element[3]}\n')
            new_user.place(x=20, y=230)
            spin_phone = tk.Spinbox(self.master, values=(values), textvariable=self.erase)
            spin_phone.place(x=450, y=50)
        
        if self.surname_label == []:
            spin_phone = tk.Spinbox(self.master, values=(values))
            spin_phone.place(x=450, y=50)
            
        new_user.config(state='disabled')
    
    def open_archive(self):
        archive = open('agenda.txt','a')
        archive.close()
        
    def load_archive(self):
        archive = open('agenda.txt', 'r')
        line = archive.readline()
        if line:
            while line:
                if line[-1] == '\n':
                    line = line[:-1]
                self.users_list.append(line)
                line = archive.readline()
        archive.close()
        
    def _write_contact(self):
        archive = open('agenda.txt', 'w')
        self.users_list.sort()
        for user in self.users_list:
            archive.write(user + '\n')
        archive.close()
        
if __name__ == '__main__':
    root = tk.Tk()
    agenda = Agenda(root)
    agenda.app_widgets()
    root.mainloop()