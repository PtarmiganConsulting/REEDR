#*******************************************************************************************************************************************************************

#Copyright (C) 2023 Ptarmigan Consulting LLC

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************

# Imports
import os
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import threading

# from pathlib import Path

from time import sleep as sleep
from tkinter import messagebox as mb

# Master GUI Function
def gui(func):

    # Dropdown Selection Data
    dropdown_dict = {
        "annual_sim_granularity": ["Annual", "Hourly", "TimeStep"],
        "subannual_sim_granularity": ["Hourly", "TimeStep"],
        "testrun_sim_granularity": ["Test Run"],
        "annual_gran_enduses": ["All_End_Uses"],
        "subannual_gran_enduses": ["All_End_Uses", "All_HVAC", "Heating", "Cooling", "Fan", "Water_Heating", "Lighting", "Other_Equipment"],
        "testrun_gran_enduses": ["Test Run"],
    }

    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    calendar_dict = {
        # jan
        1 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # feb
        2 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
        # mar
        3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # apr
        4 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        # may
        5: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # jun
        6 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        # jul
        7: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # aug
        8 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # sept
        9 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        # oct
        10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # nov
        11 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        # dec
        12: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
        # empty
        "": [],
    }
    
    sim_select = ["Annual", "Sub-Annual: enter start and end dates at right -->", "Test Run"]
    gran_select = dropdown_dict["annual_sim_granularity"]
    end_select = dropdown_dict["annual_gran_enduses"]
    default_string = "C:\EnergyPlusV22-2-0\energyplus.exe!@##@!New Project!@##@!Annual!@##@!Annual!@##@!All_End_Uses!@##@!True!@##@!BLANKSTR!@##@!BLANKSTR!@##@!BLANKSTR!@##@!BLANKSTR!@##@!True"
    ## even if the default string is not in use, it's handy for resetting defaults for version control.

    # Acquire User Settings Path
    gui_cwd = os.getcwd()

    # Revisit if time...directory fool-proofing
    if "REEDR" in gui_cwd:
        path_path = os.path.join(gui_cwd, r"Scripts\usersettings.txt")
    else:
        path_path = os.path.join(gui_cwd, r"REEDR\Scripts\usersettings.txt")

    # Acquire User Settings, creates new usersettings.txt if one is not found.
    try:
        with open(path_path, 'r') as pathread:
            settings_import = pathread.read()
            import_list = settings_import.split("!@##@!")
            pathread.close()
    except:

        print("\nusersettings.txt not found.  Loading default parameters...\n")

        with open(path_path, 'w') as data_storage:
                data_storage.write(default_string)
        
        import_list = [
            "C:\EnergyPlusV22-2-0\energyplus.exe",
            "New Project",
            "Annual",
            "Annual",
            "All_End_Uses",
            "True",
            "BLANKSTR",
            "BLANKSTR",
            "BLANKSTR",
            "BLANKSTR",
            "True",
        ]

    # Functions Begin
    def browse(*args):
        """
        Wired to the browse button, allows you to search for the EPlus path.
        """

        file = filedialog.askopenfile(mode='r')
        if file:
            filepath = os.path.abspath(file.name)
            path_input.set(filepath)

    def overwrite_warning(*args):
        """
        Raises an overwrite warning if the proper checkbox is checked and a project folder with the new project name already exists.
        """

        proj_name = project_input.get()
        
        res=mb.askquestion('Overwrite Warning', f"There is already a project folder entitled '{proj_name}'.  Do you want to overwrite it?")
        
        if res == 'yes' :
            return True
        
        return False
    
    def exe_main(*args):
        """
        Launches main REEDR script with data acquired from the GUI, and saves user's input settings to usersettings.txt. 
        """
        # Overwrite handling begins
        overwrite_allowed = True
        
        # Acquire project name, names of project folders
        proj_name = project_input.get()
        proj_dir = f"{gui_cwd}\Projects"
        proj_folders = os.listdir(proj_dir)

        # Warns About Overwriting if the Warning Combobox is checked
        if over_val.get():
            if proj_name in proj_folders:    
                overwrite_allowed = overwrite_warning()

        # Proceeds with launching REEDR unless halted by user
        if overwrite_allowed:
              
            # Harvest data from gui to be passed through the REEDR scripts.
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
            "multithread":multi_val.get(),
            }

            # Data-massaging some booleans.
            if multi_val.get() == True:
                multi_str = "True"
            else:
                multi_str = "False"

            if over_val.get() == True:
                over_str = "True"
            else:
                over_str = "False"

            # Harvests user settings to be converted into a list, later used to make the string that saves user settings.
            input_list = [
                path_input.get(),
                project_input.get(),
                sim_input.get(),
                outgran_input.get(),
                outenduses_input.get(),
                multi_str,
                bm_input.get(),
                bd_input.get(),
                em_input.get(),
                ed_input.get(),
                over_str,
            ]

            # Creates the string stored by usersettings.txt to save user settings
            data_string = ""
            for i in range(len(input_list)):
                if input_list[i]:
                    data_string += input_list[i]
                else:
                    data_string += "BLANKSTR"

                if i != (len(input_list) - 1):
                    data_string += "!@##@!"

            # Saves user settings in usersettings.txt 
            with open(path_path, 'w') as data_storage:
                data_storage.write(data_string)

            # If test run, assume hardcoded input values; genmodels will later assume single day for simulation
            if gui_params["sim_type"] == "Test Run":
                gui_params["output_gran"] = "Hourly"
                gui_params["output_enduses"] = "Heating"
            
            # Terminate the GUI during program run cycle
            print("Reading user input data...")
            sleep(1) # slight delay on the gui terming
            root.quit()
            root.destroy()
            func(gui_params)

        
    def update(*args):
        """
        Updates dropdown menus & toggles sub-annual parameter entry on and off.
        """

        # Adjusts output granularity and output enduses if annual is selected for simulation run period
        if sim_input.get() == "Annual":
            outgran_entry.config(values=dropdown_dict["annual_sim_granularity"])
            if outgran_input.get() == "Test Run":
                outgran_input.set("Annual")
                outenduses_input.set("All_End_Uses")


        # Adjusts output granularity and output enduses if sub-annual is selected for simulation run period
        elif sim_input.get() == "Sub-Annual: enter start and end dates at right -->":
            outgran_entry.config(values=dropdown_dict["subannual_sim_granularity"])
            if outgran_input.get() == "Annual":
                outgran_input.set("Hourly")
            if outgran_input.get() == "Test Run":
                outgran_input.set("Hourly")
                outenduses_input.set("All_End_Uses")

        # Adjusts output granularity and output enduses if testrun is selected for simulation run period
        elif sim_input.get() == "Test Run":
            outgran_entry.config(values=dropdown_dict["testrun_sim_granularity"])
            outenduses_entry.config(values=dropdown_dict["testrun_gran_enduses"])
            outgran_input.set("Test Run")
            outenduses_input.set("Test Run")

        # Locks output enduses to All_End_Uses if output granularity is Annual
        if outgran_input.get() == "Annual":
            outenduses_entry.config(values=dropdown_dict["annual_gran_enduses"])
            outenduses_input.set("All_End_Uses")

        elif outgran_input.get() == "Hourly":
            outenduses_entry.config(values=dropdown_dict["subannual_gran_enduses"])
        elif outgran_input.get() == "TimeStep":
            outenduses_entry.config(values=dropdown_dict["subannual_gran_enduses"])

        # Enables sub-annual parameter entry when sub-annual simulation period is selected.
        if sim_input.get() == "Sub-Annual: enter start and end dates at right -->":
            begin_label.config(foreground="black")
            end_label.config(foreground="black")
            mo_label.config(foreground="black")
            day_label.config(foreground="black")

            bm.config(state="readonly")
            em.config(state="readonly")
            bd.config(state="readonly")
            ed.config(state="readonly")

            # adaptive month/day selection set code
            begin_month = bm_input.get()
            end_month = em_input.get()

            begin_day = bd_input.get()
            end_day = ed_input.get()

            

            if begin_month:
                bd.config(values=calendar_dict[int(begin_month)])
                if begin_day:
                    if int(begin_day) not in calendar_dict[int(begin_month)]:
                        bd_input.set(calendar_dict[int(begin_month)][-1])
            else:
                bd.config(values=calendar_dict[""])

            if end_month:
                ed.config(values=calendar_dict[int(end_month)])
                if end_day:
                    if int(end_day) not in calendar_dict[int(end_month)]:
                        ed_input.set(calendar_dict[int(end_month)][-1])
            else:
                ed.config(values=calendar_dict[""])

        else:
            begin_label.config(foreground="gray")
            end_label.config(foreground="gray")
            mo_label.config(foreground="gray")
            day_label.config(foreground="gray")

            bm.config(state="disabled")
            em.config(state="disabled")
            bd.config(state="disabled")
            ed.config(state="disabled")

            bm_input.set("")
            em_input.set("")
            bd_input.set("")
            ed_input.set("")
    
    # Main Window Dimensions and Placement
    root = Tk()
    frm = ttk.Frame(root, padding=20)
    frm.grid()
    root.title("REEDR Project Setup")
    app_width = 795
    app_height = 530
    # app_height = 470 # B4
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        ## special thanks to codemy.com for help with the window-centering code

    # Main Window Labels
    ttk.Label(frm, text="the Residential Energy Efficiency and Demand Response tool (REEDR)", style='Title.TLabel').grid(sticky=W, column=0, row=0, padx=10, columnspan=2)
    ttk.Label(frm, text="v1.1.0-beta", style='Version.TLabel').grid(sticky=W, column=0, row=1, padx=10)

    # Widget Formatting
    s = ttk.Style()
    s.configure('Title.TLabel', font=('Helvetica', 12, 'bold'))
    s.configure('Version.TLabel', font=('Helvetica', 11, 'italic'))
    s.configure('Body.TLabel', font=('Helvetica', 11))
    s.configure('Body.TEntry', font=('Helvetica', 11), relief = SUNKEN)
    s.configure('Browse.TButton', font=('Helvetica', 11))
    s.configure('Run.TButton', font=('Helvetica', 12, 'bold'))
    s.configure('Copyright.TLabel', font=('Helvetica', 9))
    s.configure('LicenseBody.TLabel', font=('Helvetica', 7))

    # Path
    ttk.Label(frm, text="EnergyPlus v22.2 Executable Path: ", style='Body.TLabel').grid(sticky=W, column=0, row=2, padx=10, pady=25)
    path_input = StringVar()
    path_input.set("C:\EnergyPlusV22-2-0\energyplus.exe")
    path_entry = ttk.Entry(frm, width=60, style='Body.TEntry', textvariable=path_input, foreground="black") # path entry
    path_entry.grid(sticky=W, column=1, row=2, padx=10, pady=25, columnspan=2)

    # Project Name
    ttk.Label(frm, text="Project Name: ", style='Body.TLabel').grid(sticky=W, column=0, row=3, padx=10, pady=20)
    project_input = StringVar()
    project_input.set("New Project")
    project_entry = ttk.Entry(frm, width=48, style='Body.TEntry', textvariable=project_input, foreground="black")
    project_entry.grid(sticky=W, column=1, row=3, padx=10, pady=20, columnspan=2)

    # Simulation Run Period
    ttk.Label(frm, text="Simulation Run Period: ", style='Body.TLabel').grid(sticky=W, column=0, row=5, padx=10, pady=0)
    sim_input = StringVar()
    sim_input.set("Annual")
    simperiod_entry = ttk.Combobox(frm, width=45, textvariable=sim_input, values=sim_select, state="readonly", foreground="black")
    simperiod_entry.grid(sticky=W, column=1, row=5, padx=10, pady=0)

    # Output Granularity
    ttk.Label(frm, text="Output Granularity: ", style='Body.TLabel').grid(sticky=W, column=0, row=7, padx=10, pady=25)
    outgran_input = StringVar()
    outgran_input.set("Annual")
    outgran_entry = ttk.Combobox(frm, width=45, textvariable=outgran_input, values=gran_select, state="readonly", foreground="black")
    outgran_entry.grid(sticky=W, column=1, row=7, padx=10, pady=25) # output granularity
    
    # Output End Uses
    ttk.Label(frm, text="Output End Uses: ", style='Body.TLabel').grid(sticky=W, column=0, row=8, padx=10, pady=0)
    outenduses_input = StringVar()
    outenduses_input.set("All_End_Uses")
    outenduses_entry = ttk.Combobox(frm, width=45, textvariable=outenduses_input, values=end_select, state="readonly", foreground="black")
    outenduses_entry.grid(sticky=W, column=1, row=8, padx=10, pady=5)
    # outenduses_entry.grid(sticky=W, column=1, row=8, padx=10, pady=0) # B4

    # Browse Button
    ttk.Button(frm, text="Browse", style='Browse.TButton', command=browse).grid(column=3, row=2, columnspan=2, sticky = E)

    # Segmented Run Labels and Positioning
    begin_label = ttk.Label(frm, text="Begin: ", style='Body.TLabel', foreground="black")
    begin_label.grid(column=2, row=5, sticky=E)

    end_label = ttk.Label(frm, text="End: ", style='Body.TLabel', foreground="black")
    end_label.grid(column=2, row=6, sticky=E)

    mo_label = ttk.Label(frm, text="Mo: ", style='Body.TLabel', foreground="black")
    mo_label.grid(column=3, row=4, sticky=S)

    day_label = ttk.Label(frm, text="Day: ", style='Body.TLabel', foreground="black")
    day_label.grid(column=4, row=4, sticky=S)

    bm_input = StringVar()
    bm = ttk.Combobox(frm, width=5, values=months, textvariable=bm_input, state="disabled") ## begin month
    bm.grid(column=3, row=5)

    bd_input = StringVar()
    bd = ttk.Combobox(frm, width=5, values=days, textvariable=bd_input, state="disabled") ## begin day
    bd.grid(column=4, row=5)

    em_input = StringVar()
    em = ttk.Combobox(frm, width=5, values=months, textvariable=em_input, state="disabled") ## end month
    em.grid(column=3, row=6)

    ed_input = StringVar()
    ed = ttk.Combobox(frm, width=5, values=days, textvariable=ed_input, state="disabled") ## end day
    ed.grid(column=4, row=6)

    # Multi Threading
    multi_val = BooleanVar()
    multi_val.set(True)
    multibox = ttk.Checkbutton(frm, text='Enable multithreading', variable=multi_val, onvalue=True, offvalue=False)
    multibox.grid(sticky=W, column=1, row=9, columnspan=3, padx=10, pady=15)
    # multibox.grid(sticky=W, column=1, row=9, columnspan=3, padx=10, pady=15) # B4

    # Overwrite Project Files
    over_val = BooleanVar()
    over_val.set(True)
    over_box = ttk.Checkbutton(frm, text='Ask before overwriting project folders', variable=over_val, onvalue=True, offvalue=False)
    over_box.grid(sticky=NW, column=1, row=10, columnspan=3, padx=10, pady=0)

    # Run Button
    ttk.Button(frm, text="RUN", style='Run.TButton', width=15, command=threading.Thread(target=exe_main).start).grid(column=2, row=11, columnspan=3, padx=0, pady=15, sticky=E) # threaded v
    ttk.Button(frm, text="RUN", style='Run.TButton', width=15, command=exe_main).grid(column=2, row=11, columnspan=3, padx=0, pady=15, sticky=E)

    # Copyright label
    ttk.Label(frm, text="Copyright (C) 2023 Ptarmigan Consulting LLC. All rights reserved.", style='Copyright.TLabel').grid(sticky=W, column=0, row=16, padx=10, columnspan=5)
 
    # Activate Tracing
    path_input.trace_add("write", update)
    project_input.trace_add("write", update)
    sim_input.trace_add("write", update)
    outgran_input.trace_add("write", update)
    outenduses_input.trace_add("write", update)
    # bd_input.trace_add("write", update)
    # ed_input.trace_add("write", update)
    bm_input.trace_add("write", update)
    em_input.trace_add("write", update)
    
    # Set Imported User Settings
    for i in range(len(import_list)):
        if import_list[i] == "True":
            import_list[i] = True
        elif import_list[i] == "False":
            import_list[i] = False
        elif import_list[i] == "BLANKSTR":
            import_list[i] = ""
        
        if i == 0:
            path_input.set(import_list[i])
        elif i == 1:
            project_input.set(import_list[i])
        elif i == 2:
            sim_input.set(import_list[i])
            if sim_input.get() == "Sub-Annual: enter start and end dates at right -->":
                bm.config(state="readonly")
                em.config(state="readonly")
                bd.config(state="readonly")
                ed.config(state="readonly")
                begin_label.config(foreground="black")
                end_label.config(foreground="black")
                mo_label.config(foreground="black")
                day_label.config(foreground="black")
        elif i == 3:
            outgran_input.set(import_list[i])
        elif i == 4:
            outenduses_input.set(import_list[i])
        elif i == 5:
            if import_list[i]:
                multi_val.set(True)
            else:
                multi_val.set(False)
        elif i == 6:
            bm_input.set(import_list[i])
        elif i == 7:
            bd_input.set(import_list[i])
        elif i == 8:
            em_input.set(import_list[i])
        elif i == 9:
            ed_input.set(import_list[i])
        elif i == 10:
            if import_list[i]:
                over_val.set(True)
            else:
                over_val.set(False)

    # Activate the main GUI loop
    root.mainloop()