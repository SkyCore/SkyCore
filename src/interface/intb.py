# Copyright (C) 2010 SkyCore <http://github.com/imetallica/SkyCore>

from Tkinter import *

class c_WinBuild:
    def __init__(self, master):
        self.f = Frame(master)
        self.m = master
        self.h = Menu(self.m)
        self.m.config(menu=self.h)

    def f_CreateMenu(self, name):
        self.i = Menu(self.h)
        self.h.add_cascade(label=name, menu=self.i)

    def f_AddCommandOnMenu(self, name, cmd):
        self.i.add_command(label=name, command = cmd)

    def f_AddSeparatorOnMenu(self):
        self.i.add_separator()

    def f_AddButton(self, name, clr, X, Y, cmd):
        i = Button(self.f, text=name, fg=clr, command=cmd)
        i.grid(row=X, column=Y)
        
