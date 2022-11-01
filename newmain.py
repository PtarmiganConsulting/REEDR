import os # for making paths and directories
from pathlib import Path # for getting current directory path
import sys
from pprint import pprint

cwd = Path(os. getcwd())
parent = cwd.parent.absolute()
os.chdir(cwd)

# add paths for Python to be able to find modules and libraries
sys.path.append(os. getcwd())
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","win32"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","win32","lib"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","openpyxl","xml"))

# import main functions needed for REEDR
from Scripts.genmodels import genmodels
from Scripts.runmodels import runmodels
from Scripts.genoutputs import genoutputs
from Scripts.getdata import getdata

##############################################

# the main function

def main(gui_params):
    
    # A switch used to skip subsequent code if an error is hit
    hit_error = False
    
    ### --- Run getdata --- ###
    #...get data from Excel input template.
    get_data_dict = getdata(gui_params)
    #... if an error is experienced, send back a dictionary with the key "error" equal to True.
    if get_data_dict["error_status"] == True:
        hit_error = True
        
    ### --- Run genmodels --- ###
    # Generates EnergyPlus IDF files and directories for each.
    if hit_error == False:
        hit_error = genmodels(gui_params, get_data_dict) # for debugging

    ### --- Run runmodels --- ###
    # Runs IDF files through EnergyPlus in a batch process.
    if hit_error == False:
        hit_error = runmodels(gui_params, get_data_dict) # for debugging

    ### --- Run genoutputs --- ###
    # Combines outputs from individual IDFs into custom reports.
    if hit_error == False:
        hit_error = genoutputs(gui_params, get_data_dict) # for debugging

    if hit_error == False:
        input("REEDR run successful. Please press enter to continue...")
    else:
        input("REEDR experienced an error. Please press enter to continue...")

# the gui function
from Scripts.gui import gui as gui

gui(main)