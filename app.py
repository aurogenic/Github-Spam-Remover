import database as db
from discussions import moderate_discussion_comments

from customtkinter import CTk, CTkButton, CTkEntry, CTkFrame, CTkLabel, CTkScrollableFrame

#colors
bg = "#240046"
navbar_clr = "#C77DFF"
sec1_clr = "#4C197C" 

clr1 = "#10002B"

class App:
    def __init__(self):
        self.win = CTk(fg_color=bg)
        self.win.geometry("1000x550")
        
        self.grid_config()
        self.add_navbar()
        self.add_view_sec()
        self.add_add_sec()
        self.add_list_sec()
        self.win.resizable(False, False)
        self.win.mainloop()
    

    def grid_config(self):
        self.win.grid_rowconfigure(1, weight=1)
        self.win.grid_columnconfigure([0, 1], weight=1)

    def add_navbar(self):
        self.navbar = CTkFrame(self.win, fg_color=navbar_clr, height=65, corner_radius=0)
        self.navbar.grid(row=0, column=0, columnspan=2, sticky='NEW')
    
    def add_view_sec(self):
        self.view_sec = CTkFrame(self.win,fg_color=sec1_clr, height=455, width=400, corner_radius=25)
        self.view_sec.grid(row=1, column=0, padx=15, pady=15, sticky='NSEW')

    def add_add_sec(self):
        self.add_sec = CTkFrame(self.win,fg_color=sec1_clr, height=455, width=400, corner_radius=25)
        self.add_sec.grid(row=1, column=0, padx=15, pady=15, sticky='NSEW')
        title = CTkLabel(self.add_sec, text="New Repository", font=("Roboto bold",  30), text_color="white", width=360)
        title.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky='NEW')

        self.add_sec.grid_columnconfigure([0, 1], weight=1)

    def add_list_sec(self):
        self.list_sec = CTkScrollableFrame(self.win,fg_color=sec1_clr, height=455, width=500, corner_radius=25)
        self.list_sec.grid(row=1, column=1, padx=15, pady=15, sticky='NSEW')

a = App()