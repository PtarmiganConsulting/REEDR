import os
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

def gui(func):

    #combobox selection lists
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    sim_select = ["Annual", "Sub-Annual: enter start and end dates at right -->"] # check with CD
    gran_select = ["Annual", "Hourly", "TimeStep"]
    end_select = ["All_End_Uses", "Total_Electric_HVAC", "Heating", "Cooling", "Fan", "Water-Heating", "Lighting", "Other_Electric_Equipment"]


    # functions
    def browse(*args):
        file = filedialog.askopenfile(mode='r')
        if file:
            filepath = os.path.abspath(file.name)
            path_entry.insert(0, filepath)

    def exe_main(*args):
        gui_params={
        "path_val":path_input.get(),
        "project_val":project_input.get(),
        "sim_type":sim_input.get(),
        "output_gran":outgran_input.get(),
        "output_enduses":outenduses_input.get(),
        "begin_mo":bm_input.get(),
        "begin_day":bd_input.get(),
        "end_mo":em_input.get(),
        "end_day":ed_input.get(),
        }
        # print(gui_params.values()) # for debugging
        func(gui_params)
        # input("\n Thanks for using REEDR.  Press enter to terminate program.")
        root.quit()


    #GUI
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


    path_input = StringVar()
    path_entry = ttk.Entry(frm, width=60, style='Body.TEntry', textvariable=path_input) # path entry
    path_entry.grid(sticky=W, column=1, row=2, padx=10, pady=25, columnspan=2) # for whatever bizarre reason, unless the grid parameters are declared on their own line, path_entry is not recognized as an Entry object by py and the browse function doesn't work

    ttk.Label(frm, text="Project Name: ", style='Body.TLabel').grid(sticky=W, column=0, row=3, padx=10, pady=20)
    project_input = StringVar()
    project_entry = ttk.Entry(frm, width=48, style='Body.TEntry', textvariable=project_input).grid(sticky=W, column=1, row=3, padx=10, pady=20, columnspan=2) # project entry
    ttk.Label(frm, text="Simulation Run Period: ", style='Body.TLabel').grid(sticky=W, column=0, row=5, padx=10, pady=0)
    sim_input = StringVar()
    simperiod_entry = ttk.Combobox(frm, width=45, textvariable=sim_input, values=sim_select).grid(sticky=W, column=1, row=5, padx=10, pady=0) # simulation run period
    ttk.Label(frm, text="Output Granularity: ", style='Body.TLabel').grid(sticky=W, column=0, row=7, padx=10, pady=25)
    outgran_input = StringVar()
    outgran_entry = ttk.Combobox(frm, width=45, textvariable=outgran_input, values=gran_select).grid(sticky=W, column=1, row=7, padx=10, pady=25) # output granularity
    ttk.Label(frm, text="Output End Uses: ", style='Body.TLabel').grid(sticky=W, column=0, row=8, padx=10, pady=0)
    outenduses_input = StringVar()
    outenduses_entry = ttk.Combobox(frm, width=45, textvariable=outenduses_input, values=end_select).grid(sticky=W, column=1, row=8, padx=10, pady=0) # output end uses
    ttk.Button(frm, text="Browse", style='Browse.TButton', command=browse).grid(column=3, row=2, columnspan=2)

    ttk.Label(frm, text="Begin: ", style='Body.TLabel').grid(column=2, row=5, sticky=E)
    ttk.Label(frm, text="End: ", style='Body.TLabel').grid(column=2, row=6, sticky=E)
    ttk.Label(frm, text="Mo: ", style='Body.TLabel').grid(column=3, row=4)
    ttk.Label(frm, text="Day: ", style='Body.TLabel').grid(column=4, row=4)

    bm_input = StringVar() # this one is called "inp" because it avoids a mysterious error
    bm = ttk.Combobox(frm, width=5, values=months, textvariable=bm_input).grid(column=3, row=5) # begin month
    bd_input = StringVar()
    bd = ttk.Combobox(frm, width=5, values=days, textvariable=bd_input).grid(column=4, row=5) # begin day
    em_input = StringVar()
    em = ttk.Combobox(frm, width=5, values=months, textvariable=em_input).grid(column=3, row=6) # end month
    ed_input = StringVar()
    ed = ttk.Combobox(frm, width=5, values=days, textvariable=ed_input).grid(column=4, row=6) # end day

    ttk.Button(frm, text="RUN", style='Run.TButton', width=15, command=exe_main).grid(column=2, row=9, columnspan=3, padx=10, pady=15) # run button, idle rn

    root.mainloop()