import os # for making paths and directories
import subprocess
from pathlib import Path # for getting current directory path
import sys

cwd = Path(os. getcwd())
parent = cwd.parent.absolute()
os.chdir(cwd)

sys.path.append(os. getcwd())
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","win32"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","win32","lib"))
sys.path.append(os.path.join(parent,"python-3.10.0","Lib","site-packages","openpyxl","xml"))

# Note: when exe'ing, must add "Python." in front of each file name
from getdata import sht1, runlog, begin_mo, begin_day, end_mo, end_day, sim_type, output_gran, output_enduses
from genmodels import genmodels
from runmodels import runmodels
from genoutputs import genoutputs

def main():

    # A switch used to skip subsequent code if an error is hit
    hit_error = False

    #Run genmodels.py
    try:
        genmodels(begin_mo, begin_day, end_mo, end_day, sim_type, output_gran, output_enduses)

    except Exception as e:
        runlog.write("!!! REEDR experienced the following error during model build: " + str(e) + " \n")
        runlog.close()
        print()
        print("Model build failed.")
        print()
        print("REEDR experienced the following error: " + str(e))
        print()
        input("Please press enter to continue...")
        hit_error = True

    #Run runmodels.py
    if hit_error == False:
        try:
            runmodels()

        except Exception as e:
            runlog.write("!!! REEDR experienced the following error during model runs: " + str(e) + " \n")
            runlog.close()
            print()
            print("Model run failed.")
            print()
            print("REEDR experienced the following error: " + str(e))
            print()
            input("Please press enter to continue...")
            hit_error = True

    #Run genoutputs.py
    if hit_error == False:
        try:
            genoutputs(begin_mo, begin_day, end_mo, end_day, sim_type, output_gran, output_enduses)

        except Exception as e:
            runlog.write("!!! REEDR experienced the following error during model output generation: " + str(e) + " \n")
            runlog.close()
            print()
            print("Model output failed.")
            print()
            print("REEDR experienced the following error: " + str(e))
            print()
            input("Please press enter to continue...")
            hit_error = True

    if hit_error == False:
        input("REEDR run successful. Please press enter to continue...")

if __name__ == "__main__":
    main()
