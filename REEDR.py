#*******************************************************************************************************************************************************************

#Copyright (C) 2023 Ptarmigan Consulting LLC

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************

print("***********************************************************************************************************************")
print("Copyright (C) 2023 Ptarmigan Consulting LLC\n")
print("This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n")
print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n")
print("You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>")
print("***********************************************************************************************************************\n")

print("Initializing REEDR interface...\n")

import os # for making paths and directories
from pathlib import Path # for getting current directory path
import sys
import time
from pprint import pprint

cwd = Path(os. getcwd())
parent = cwd.parent.absolute()
os.chdir(cwd)

# add paths for Python to be able to find modules and libraries
# sys.path.append(os. getcwd())
# sys.path.append(os.path.join(cwd,"python-3.10.0","Lib","site-packages"))

# import main functions needed for REEDR
from Scripts.genmodels import genmodels
from Scripts.runmodels import runmodels
from Scripts.genoutputs import genoutputs
from Scripts.getdata import getdata
from Scripts.dictmaker import dict_maker

##############################################

# the main function

def main(gui_params):

    # For timing REEDER.  Swap booleans to toggle run-timing on and off
    # time_val = False
    time_val = True
    if time_val:
        start_time = time.time()
    
    # A switch used to skip subsequent code if an error is hit
    hit_error = False

    ### --- Run getdata --- ###
    #...get data from Excel input template.
    get_data_dict = getdata(gui_params)
    #... if an error is experienced, send back a dictionary with the key "error" equal to True.
    if get_data_dict["error_status"] == True:
        hit_error = True

    ### --- Get inputs from Control Panel. --- ###
    set_dir = get_data_dict["parent"]
    control_panel_dict = {}
    control_panel_dict["control_panel_folder_name"] = "Control Panel"
    control_panel_dict["control_panel_names_file"] = "Control Panel Names.csv"
    control_panel_dict["control_panel_names_path"] = os.path.join(set_dir, \
        control_panel_dict["control_panel_folder_name"], control_panel_dict["control_panel_names_file"])
    control_panel_dict["control_panel_names_dict"] = dict_maker(control_panel_dict["control_panel_names_path"])
    control_panel_dict["control_panel_names_lookup_id"] = "folder_or_file_name"
    
    ### --- Run genmodels --- ###
    # Generates EnergyPlus IDF files and directories for each.
    if hit_error == False:
        hit_error = genmodels(gui_params, get_data_dict, control_panel_dict) # for debugging

    ### --- Run runmodels --- ###
    # Runs IDF files through EnergyPlus in a batch process.
    if hit_error == False:
        hit_error = runmodels(gui_params, get_data_dict) # for debugging

    ### --- Run genoutputs --- ###
    # Combines outputs from individual IDFs into custom reports.
    if hit_error == False:
        hit_error = genoutputs(gui_params, get_data_dict, control_panel_dict) # for debugging

    if hit_error == False:
        if time_val:
            end_time = time.time()
            print(f"Run time = {end_time - start_time} seconds. \n")
            
        input("REEDR run successful.  You may now close this window or press enter.")
    else:
        input("REEDR experienced an error.  You may now close this window or press enter.")


# the gui function
from Scripts.gui import gui as gui

gui(main)