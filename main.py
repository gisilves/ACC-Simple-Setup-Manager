""" ACC Simple Setup Manager

Copyright (c) 2020 Gianluigi Silvestre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """


import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as st 
import os
import json
import io
import ctypes
import shutil

class ACCSetupManager(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.master = master
        #self.master.iconbitmap('icon.ico')
        self.initUI()
        self.pack()
    
    def initUI(self):
        self.master.title("ACC Simple Setup Manager")
        self.master.geometry('600x550')

        self.lbl = tk.Label(self.master, text="Setups will be saved in the following directory:",bg="#DCDCDC")
        self.lbl.place(x=300, y=490, anchor="center")

        self.lbl2 = tk.Label(self.master, text=os.path.expanduser('~\Documents\Documents')+'\Assetto Corsa Competizione\Setups')
        self.lbl2.place(x=300, y=510, anchor="center")

        self.lbl3 = tk.Label(self.master, text="No setup opened")
        self.lbl3.place(x=300, y=530, anchor="center")
        
        self.CarList = [
        "Alpine A110 GT4",
        "AMR V12 Vantage GT3",
        "AMR V8 Vantage GT3",
        "Aston Martin Vantage GT4",
        "Audi R8 LMS",
        "Audi R8 LMS EVO",
        "Audi R8 LMS GT4",
        "Bentley Continental GT3 2016",
        "Bentley Continental GT3 2018",
        "BMW M4 GT4",
        "BMW M6 GT3",
        "Chevrolet Camaro GT4",
        "Ferrari 488 GT3",
        "Ferrari 488 GT3 Evo",
        "Ginetta G55 GT4",
        "Honda NSX GT3",
        "Honda NSX GT3 EVO",
        "Emil Frey Jaguar G3",
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
        "Mercedes Amg GT3 EVO",
        "Mercedes AMG GT4",
        "Nissan GT R Nismo GT3 2017",
        "Nissan GT-R Nismo GT3 2018",
        "Porsche 718 Cayman GT4",
        "Porsche 991 GT3-R",
        "Porsche 991 II GT3 Cup",
        "Porsche 991 II GT3 R",
        "Reiter Engineering R-EX GT3"
        ]

        self.CarListFolder = [
        "alpine_a110_gt4",
        "amr_v12_vantage_gt3",
        "amr_v8_vantage_gt3",
        "amr_v8_vantage_gt4",
        "audi_r8_lms",
        "audi_r8_lms_evo",
        "audi_r8_gt4",
        "bentley_continental_gt3_2016",
        "bentley_continental_gt3_2018",
        "bmw_m4_gt4",
        "bmw_m6_gt3",
        "chevrolet_camaro_gt4r",
        "ferrari_488_gt3",
        "ferrari_488_gt3_evo",
        "ginetta_g55_gt4",
        "honda_nsx_gt3",
        "honda_nsx_gt3_evo",
        "jaguar_g3",
        "ktm_xbow_gt4",
        "lamborghini_huracan_gt3",
        "lamborghini_huracan_gt3_evo",
        "lamborghini_huracan_st",
        "lexus_rc_f_gt3",
        "maserati_mc_gt4",
        "mclaren_570s_gt4",
        "mclaren_650s_gt3",
        "mclaren_720s_gt3",
        "mercedes_amg_gt3",
        "mercedes_amg_gt3_evo",
        "mercedes_amg_gt4",
        "nissan_gt_r_gt3_2017",
        "nissan_gt_r_gt3_2018",
        "porsche_718_cayman_gt4_mr",
        "porsche_991_gt3_r",
        "porsche_991ii_gt3_cup",
        "porsche_991ii_gt3_r",
        "lamborghini_gallardo_rex"
        ]

        self.TrackList = [
        "Barcelona",
        "Mount Panorama",
        "Brands Hatch",
        "Hungaroring",
        "Imola",
        "Kyalami",
        "Laguna Seca",
        "Misano",
        "Monza",
        "Nurburgring",
        "Paul Ricard",
        "Silverstone",
        "Spa",
        "Suzuka",
        "Zandvoort",
        "Zolder"
        ]

        self.TrackListFolder = [
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

        self.car_variable = tk.StringVar(self)
        self.car_variable.set("Choose a car")
        self.car_menu = tk.OptionMenu(self, self.car_variable, *self.CarList)
        self.car_menu.config(width=35, font=('TkDefaultFont', 10))
        self.car_menu.grid(row=1, column=0)

        self.track_variable = tk.StringVar(self)
        self.track_variable.set("Choose a track")
        self.track_menu = tk.OptionMenu(self, self.track_variable, *self.TrackList)
        self.track_menu.config(width=35, font=('TkDefaultFont', 10))
        self.track_menu.grid(row=1, column=1)

        self.current_setup = tk.StringVar()
        self.setuplist = tk.Listbox(self, listvariable=self.current_setup, width=47, height=24)
        self.setuplist.grid(row=2, column=0)
        self.setuplist.bind('<Double-1>', self.display)

        btn = tk.Button(self, text="Load local setups", command=self.onLoad)
        btn.grid(column=0, row=3,padx=10)
        btn2 = tk.Button(self, text="Copy a new setup", command=self.onOpen)
        btn2.grid(column=1, row=3)

        self.txt = st.ScrolledText(self,width=33, height=24)
        self.txt.grid(row=2, column=1)

    def onOpen(self):
        ftypes = [('Setup files', '*.json'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            text = self.readFile(fl, True)

    def onLoad(self):
        self.setuplist.delete(0,'end')

        try:
            localdir =(os.path.expanduser('~\Documents')+'\Assetto Corsa Competizione\Setups\\'
            + self.CarListFolder[self.CarList.index(self.car_variable.get())] 
            + "\\" 
            + self.TrackListFolder[self.TrackList.index(self.track_variable.get())])
            
            if not os.path.isdir(localdir):
                os.makedirs(localdir)

            if len(os.listdir(localdir)) == 0:
                self.popup('No setups in local folder')
                return

            for item in os.listdir(localdir):
                self.setuplist.insert('end', item)
        
        except ValueError:
            self.popup('You must select a car and a track first')

    def readFile(self, filename, to_copy):
        self.txt.delete(1.0,'end')
        with io.open(filename, 'r', encoding='utf-8-sig') as json_file:
            data = json.load(json_file)
            data = self.flatten_json(data)

            try:
                self.lbl3.config(text='Loaded setup file for car ' + data['carName'])
                self.txt.insert('end', 'Setup file: ' + os.path.basename(filename) + '\n\n')
                for key, value in data.items():
                    self.txt.insert('end', str(key).replace('basicSetup_', '').replace('advancedSetup_', '').replace('strategy_','') + ':\n' + str(value) + '\n\n')
            except KeyError:
                self.popup('File is not a compatible setup file')
                return

        if(to_copy):
            if(self.CarListFolder[self.CarList.index(self.car_variable.get())] == data['carName']):
                destination = os.path.join( os.path.expanduser('~\Documents'), 'Assetto Corsa Competizione', 'Setups', self.CarListFolder[self.CarList.index(self.car_variable.get())], self.TrackListFolder[self.TrackList.index(self.track_variable.get())])
                shutil.copy2(filename, destination)
            else:
                self.popup('Setup is not for the car selected, it won\'t be copied')

    def flatten_json(self,y):
        out = {}

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[name[:-1]] = x
        flatten(y)
        return out

    def display(self,event): 
        current_filename = os.path.join( os.path.expanduser('~\Documents'), 'Assetto Corsa Competizione', 'Setups', self.CarListFolder[self.CarList.index(self.car_variable.get())], self.TrackListFolder[self.TrackList.index(self.track_variable.get())], self.setuplist.get(self.setuplist.curselection()))
        self.readFile(current_filename, False)

    def popup(self,messagetext):
        win = tk.Toplevel()
        win.title('WARNING')
        l = tk.Label(win, text=messagetext, bg='white')
        l.pack(ipadx=50, ipady=10, fill='both', expand=True)
        b = tk.Button(win, text="OK", command=win.destroy)
        b.pack(pady=10, padx=10, ipadx=20, side='right')
        x = self.winfo_x()
        y = self.winfo_y()
        win.geometry("+%d+%d" % (x + 320, y + 350))

# Main
if __name__ == "__main__":
    # create interface
    root = tk.Tk()
    application = ACCSetupManager(root)
    root.resizable(0,0)
    root.mainloop()