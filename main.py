from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st 
import os
import json
import io
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
        
        self.CarList = [
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
        "Mercedes Amg GT3 EVO",
        "Mercedes AMG GT4",
        "Nissan GT R Nismo GT3",
        "Nissan GT-R Nismo GT3",
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
        "audi_r8_gt4",
        "audi_r8_lms",
        "audi_r8_lms_evo",
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
        "lamborghini_gallardo_rex",
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
        "porsche_991ii_gt3_r"
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

        self.variable = StringVar(self)
        self.variable.set("Choose a car")
        self.opt = OptionMenu(self, self.variable, *self.CarList)
        self.opt.config(width=28, font=('TkDefaultFont', 10))
        self.opt.grid(row=1, column=0)

        self.variable1 = StringVar(self)
        self.variable1.set("Choose a track")
        self.opt1 = OptionMenu(self, self.variable1, *self.TrackList)
        self.opt1.config(width=28, font=('TkDefaultFont', 10))
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
        for item in os.listdir(os.path.expanduser('~\Documents')+'\Assetto Corsa Competizione\Setups\\' 
                                                                + self.CarListFolder[self.CarList.index(self.variable.get())] 
                                                                + "\\" 
                                                                + self.TrackListFolder[self.TrackList.index(self.variable1.get())]):

            self.lb.insert('end', item)

    def readFile(self, filename):

        with io.open(filename, 'r', encoding='utf-8-sig') as json_file:
            data = json.load(json_file)
            data = self.flatten_json(self, data)
            self.lbl3.config(text='Loaded setup file for car ' + data['carName'])
            #self.txt.insert('end',text)            
        shutil.copyfile(filename, os.path.expanduser('~\Documents')+'\Assetto Corsa Competizione\Setups\\' + self.variable.get() + "\\" + self.variable1.get())

    def flatten_json(self, y):
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

# Main
if __name__ == "__main__":
    # create interface
    root = Tk()
    application = ACCSetupManager(root)
    root.resizable(0,0)
    root.mainloop()