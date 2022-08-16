import os # for making paths and directories
import subprocess
from pathlib import Path # for getting current directory path
import sys
from pprint import pprint

cwd = Path(os. getcwd())
parent = cwd.parent.absolute()
os.chdir(cwd)

sys.path.append(os. getcwd())
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","win32"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","win32","lib"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","openpyxl","xml"))

# Note: when exe'ing, must add "Python." in front of each file name
from genmodels import genmodels
from runmodels import runmodels
from genoutputs import genoutputs
from getdata import getdata

##############################################

# the main function

def main(gui_params):
    
    #Run getdata.py
    get_data_dict = getdata(gui_params)

    # A switch used to skip subsequent code if an error is hit
    hit_error = False

    #Run genmodels.py
    # genmodels(gui_params, get_data_dict) # for debugging

    #try:
    genmodels(gui_params, get_data_dict)

    # except Exception as e:
    #     get_data_dict["runlog"].write("!!! REEDR experienced the following error during model build: " + str(e) + " \n")
    #     get_data_dict["runlog"].close()
    #     print()
    #     print("Model build failed.")
    #     print()
    #     print("REEDR experienced the following error: " + str(e))
    #     print()
    #     input("Please press enter to continue...")
    #     hit_error = True

    #Run runmodels.py

    # runmodels(gui_params, get_data_dict) # for debugging

    if hit_error == False:
        try:
            runmodels(gui_params, get_data_dict)

        except Exception as e:
            get_data_dict["runlog"].write("!!! REEDR experienced the following error during model runs: " + str(e) + " \n")
            get_data_dict["runlog"].close()
            print()
            print("Model run failed.")
            print()
            print("REEDR experienced the following error: " + str(e))
            print()
            input("Please press enter to continue...")
            hit_error = True

    #Run genoutputs.py

    # genoutputs(gui_params, get_data_dict) # for debugging
    if hit_error == False:
        try:
            genoutputs(gui_params, get_data_dict)

        except Exception as e:
            get_data_dict["runlog"].write("!!! REEDR experienced the following error during model output generation: " + str(e) + " \n")
            get_data_dict["runlog"].close()
            print()
            print("Model output failed.")
            print()
            print("REEDR experienced the following error: " + str(e))
            print()
            input("Please press enter to continue...")
            hit_error = True

    if hit_error == False:
        input("REEDR run successful. Please press enter to continue...")

# the gui function
from gui import gui as gui
gui(main)