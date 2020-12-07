# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st 
import os
import json
import ctypes
import shutil

class ACCSetupManager(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('icon.ico')
        self.initUI()
        self.pack() #packs the Frame
    
    def initUI(self):
        self.master.title("ACC Setup Manager")
        self.master.geometry('500x550')

        self.lbl = Label(self.master, text="Setups will be saved in the following directory:",bg="yellow")
        self.lbl.place(x=250, y=490, anchor="center")

        self.lbl2 = Label(self.master, text=os.path.expanduser('~\Documents\Documents')+'\Assetto Corsa Competizione')
        self.lbl2.place(x=250, y=510, anchor="center")

        self.lbl3 = Label(self.master, text="No setup opened")
        self.lbl3.place(x=250, y=530, anchor="center")
        
        OptionList = [
        "Alpine A110 GT4",
        "AMR V8 Vantage GT3",
        "AMR V12 Vantage GT3",
        "Aston Martin Vantage GT4",
        "Audi R8 LMS",
        "Audi R8 LMS EVO",
        "Audi R8 LMS GT4",
        "Bentley Continental GT3",
        "Bentley Continental GT3",
        "BMW M4 GT4",
        "BMW M6 GT3",
        "Chevrolet Camaro GT4",
        "Emil Frey Jaguar G3",
        "Ferrari 488 GT3",
        "Ferrari 488 GT3 Evo",
        "Ginetta G55 GT4",
        "Honda NSX GT3",
        "Honda NSX GT3 EVO",
        "KTM X-Bow GT4",
        "Lamborghini Huracan GT3",
        "Lamborghini Huracan GT3 EVO",
        "Lamborghini Huracan SuperTrofeo",
        "Lexus RC F GT3",
        "Maserati MC GT4",
        "McLaren 570S GT4",
        "McLaren 650S GT3",
        "McLaren 720s GT3",
        "Mercedes AMG GT3",
        "mercedes_amg_gt3_evo",
        "Mercedes AMG GT4",
        "Nissan GT R Nismo GT3",
        "Nissan GT-R Nismo GT3",
        "Porsche 718 Cayman GT4",
        "Porsche 991 GT3-R",
        "Porsche 991 II GT3 Cup",
        "Porsche 991 II GT3 R",
        "Reiter Engineering R-EX GT3"
        ]

        OptionList2 = [
        "barcelona",
        "mount_panorama",
        "brands_hatch",
        "hungaroring",
        "imola",
        "kyalami",
        "laguna_seca",
        "misano",
        "monza",
        "nurburgring",
        "paul_ricard",
        "Silverstone",
        "spa",
        "suzuka",
        "zandvoort",
        "zolder"
        ]

        self.variable = StringVar(self)
        self.variable.set("Choose a car")
        self.opt = OptionMenu(self, self.variable, *OptionList)
        self.opt.config(width=28, font=('Helvetica', 10))
        self.opt.grid(row=1, column=0)

        self.variable1 = StringVar(self)
        self.variable1.set("Choose a track")
        self.opt1 = OptionMenu(self, self.variable1, *OptionList2)
        self.opt1.config(width=28, font=('Helvetica', 10))
        self.opt1.grid(row=1, column=1)

        var2 = StringVar()
        self.lb = Listbox(self, listvariable=var2, width=38, height=24)
        self.lb.grid(row=2, column=0)

        btn = Button(self, text="Load local setups", command=self.onLoad)
        btn.grid(column=0, row=3)
        btn = Button(self, text="Add a new setup", command=self.onOpen)
        btn.grid(column=1, row=3)

        var3 = StringVar()
        self.txt = st.ScrolledText(self,width=28, height=24)
        #self.txt.configure(state ='disabled') 
        self.txt.grid(row=2, column=1)

        #self.lb2 = Listbox(self, listvariable=var3, width=38, height=24)
        #self.lb2.grid(row=2, column=1)

    def onOpen(self):
        ftypes = [('Setup files', '*.json'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)

    def onLoad(self):
        for item in os.listdir(os.path.expanduser('~\Documents')+'\Assetto Corsa Competizione\Setups\\' + self.variable.get() + "\\" + self.variable1.get()):
            self.lb.insert('end', item)

    def readFile(self, filename):
        f = open(filename, "r", encoding='utf-8')
        text = f.read()
        data = json.loads(text)
        self.lbl3.config(text='Loaded setup file for car ' + data['carName'])
        self.txt.insert('end',text)    
        
        shutil.copyfile(filename, os.path.expanduser('~\Documents')+'\Assetto Corsa Competizione\Setups\\' + self.variable.get() + "\\" + self.variable1.get())
        return text

# Main
if __name__ == "__main__":
    # create interface
    root = Tk()
    application = ACCSetupManager(root)
    root.resizable(0,0)
    root.mainloop()