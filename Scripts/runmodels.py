#import necessary modules
import os
import subprocess
import pandas as pd
from pprint import pprint # for debugging

# from getdata import cwd, parent, sht1, master directory, master_dict_list, df, eplus_directory, runlog

def runmodels(gui_params, get_data_dict):

    # Sets the directory. When calling from __main__, needs to be set to "parent". When calling from entry exe script, needs to be set to "cwd".
    set_dir = get_data_dict["parent"]

    # Update simulation status box in REEDR.xlsm...
    status = "Starting model run(s)..."
    print(status)
    #sht1.range('status_line_2').value = "Starting model run(s)..."

    ################################################################################################################

    def plusterwolf(runlabel, weatherfile, projname, epluslocation, i, df):
        """
        This is the function that calls eplus and deposits the results
        in the appropriate place.

        This only runs one idf at a time based on the input parameters,
        but by iterating over our super handy dictionary list
        (again the hero of the day), we can do all of them at once.

        (Don't worry, I'm not gonna call it "plusterwolf" forever...
        It's just a doofy homage to a 90s fighting game.)
        """
    	## from https://unmethours.com/question/22157/run-energyplus-from-python/

        ## define eplus path, IDF file, and weather file
        eplus_path = epluslocation
        ##eplus_path = r'C:\EnergyPlusV9-5-0\energyplus.exe'
        runidf = runlabel + ".idf"
        eplus_file = os.path.join(set_dir, projname, runlabel, runidf)

        weathidf = weatherfile + ".epw"
        weather_file = os.path.join(set_dir, "Weather", weathidf)

    	## set output directory
        output_path = os.path.join(set_dir, projname, runlabel)

    	## if output folder does not exist, create it
        ## I don't think we need this, but I left it in to be safe
        if os.path.exists(output_path) == False:
            os.mkdir(output_path)

    	## set directory for eplus output
    	##-d, --output-directory ARG   Output directory path (default: current directory)
        eplusout_path = output_path

        ## https://github.com/jamiebull1/eplus_worker/blob/master/worker/runner.py
        dff = subprocess.Popen([eplus_path, '-r', '-w', weather_file, '-d', eplusout_path, eplus_file],stdout=subprocess.PIPE, universal_newlines=True)

        # for stdout_line in dff.stdout:
        #     print(stdout_line)

        dff.stdout.close()
        return_code = dff.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, dff.args)


    ## iterates over the master dictionary list and calls eplus on all of them
    ## remember, each dictionary is effectively a complete runlabel row...
    ## and that's how we can catch every runlabel with one short loop!
    get_data_dict["runlog"].write("Starting model runs... \n")
    i = 1
    for dictionary in get_data_dict["master_dict_list"]:
        # Update simulation status box in REEDR.xlsm...
        status = "...running model " + str(i) + " of " + str(len(get_data_dict["df"])) + "..."
        print(status)
        #sht1.range('status_line_2').value = status

        run_label = dictionary["Run_Label"]
        location_pull = dictionary["Weather_File"]

        try:
            plusterwolf(run_label, location_pull, get_data_dict["master_directory"], gui_params["path_val"], i, get_data_dict["df"])
            get_data_dict["runlog"].write("... model run for " + run_label + " complete. \n")
        except Exception as e:
            get_data_dict["runlog"].write("!!! problem running model " + run_label + "\n")
            get_data_dict["runlog"].write("!!! REEDR experienced the following error: " + str(e) + "\n")
            print(e)

        i = i + 1

    get_data_dict["runlog"].write("... \n")

    #sub = subprocess.Popen("cmd /k")

    print("...model runs complete.")
    print()

    # Update simulation status box in REEDR.xlsm...
    #sht1.range('status_line_2').value = "Starting model run(s)... Model run(s) complete."
