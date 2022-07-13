
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
root.title("REEDR Project Setup")

s = ttk.Style()
s.configure('Title.TLabel', font=('Helvetica', 12, 'bold'))
s.configure('Version.TLabel', font=('Helvetica', 11, 'italic'))
s.configure('Body.TLabel', font=('Helvetica', 11))
s.configure('Body.TEntry', font=('Helvetica', 11), relief = SUNKEN)
s.configure('Browse.TButton', font=('Helvetica', 11))
s.configure('Run.TButton', font=('Helvetica', 12, 'bold'))

ttk.Label(frm, text="Residential Energy Efficiency and Demand Response (REEDR) Tool", style='Title.TLabel').grid(sticky=W, column=0, row=0, padx=10, columnspan=2)
ttk.Label(frm, text="v0.5.0", style='Version.TLabel').grid(sticky=W, column=0, row=1, padx=10)
ttk.Label(frm, text="EnergyPlus v9.5 Executable Path: ", style='Body.TLabel').grid(sticky=W, column=0, row=2, padx=10, pady=25)
e1 = ttk.Entry(frm, width=60, style='Body.TEntry').grid(sticky=W, column=1, row=2, padx=10, pady=25, columnspan=2)
ttk.Label(frm, text="Project Name: ", style='Body.TLabel').grid(sticky=W, column=0, row=3, padx=10, pady=20)
e2 = ttk.Entry(frm, width=48, style='Body.TEntry').grid(sticky=W, column=1, row=3, padx=10, pady=20, columnspan=2)
ttk.Label(frm, text="Simulation Run Period: ", style='Body.TLabel').grid(sticky=W, column=0, row=5, padx=10, pady=0)
e3 = ttk.Combobox(frm, width=45).grid(sticky=W, column=1, row=5, padx=10, pady=0)
ttk.Label(frm, text="Output Granularity: ", style='Body.TLabel').grid(sticky=W, column=0, row=7, padx=10, pady=25)
e4 = ttk.Combobox(frm, width=45).grid(sticky=W, column=1, row=7, padx=10, pady=25)
ttk.Label(frm, text="Output End Uses: ", style='Body.TLabel').grid(sticky=W, column=0, row=8, padx=10, pady=0)
e5 = ttk.Combobox(frm, width=45).grid(sticky=W, column=1, row=8, padx=10, pady=0)

ttk.Button(frm, text="Browse", style='Browse.TButton').grid(column=3, row=2, columnspan=2)

ttk.Label(frm, text="Begin: ", style='Body.TLabel').grid(column=2, row=5, sticky=E)
ttk.Label(frm, text="End: ", style='Body.TLabel').grid(column=2, row=6, sticky=E)
ttk.Label(frm, text="Mo: ", style='Body.TLabel').grid(column=3, row=4)
ttk.Label(frm, text="Day: ", style='Body.TLabel').grid(column=4, row=4)
bm = ttk.Combobox(frm, width=5).grid(column=3, row=5)
bd = ttk.Combobox(frm, width=5).grid(column=4, row=5)
em = ttk.Combobox(frm, width=5).grid(column=3, row=6)
ed = ttk.Combobox(frm, width=5).grid(column=4, row=6)

ttk.Button(frm, text="RUN", style='Run.TButton', width=15).grid(column=2, row=9, columnspan=3, padx=10, pady=15)

root.mainloop()
