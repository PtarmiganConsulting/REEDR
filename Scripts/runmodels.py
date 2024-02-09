#*******************************************************************************************************************************************************************

#Copyright (C) 2024 Ptarmigan Consulting LLC

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************

#import necessary modules
import os
import subprocess
import pandas as pd
import threading
import time
from pprint import pprint # for debugging

def runmodels(gui_params, get_data_dict):

    # for enabling or disabling multithreading
    multi=gui_params["multithread"]

    # Sets the directory.
    set_dir = get_data_dict["parent"]

    # Update simulation status...
    status = "Starting model run(s)..."
    print(status)

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
        #dff = subprocess.Popen([eplus_path, '-r', '-w', weather_file, '-d', eplusout_path, eplus_file],stdout=subprocess.PIPE, universal_newlines=True)
        dff = subprocess.Popen([eplus_path, '-w', weather_file, '-d', eplusout_path, eplus_file],stdout=subprocess.PIPE, universal_newlines=True)

        # for stdout_line in dff.stdout:
        #     print(stdout_line)

        dff.stdout.close()
        return_code = dff.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, dff.args)


    ## iterates over the master dictionary list and calls eplus on all of them
    ## remember, each dictionary is effectively a complete runlabel row...
    ## and that's how we can catch every runlabel with one short loop!
    i = 1

    cpu_count = os.cpu_count()
    if cpu_count == 1:
        thread_limit = 1
    else:
        thread_limit = ((cpu_count * (3/4)) // 1)

    # print(f"cpu count = {cpu_count}")
    # print(f"thread limit = {thread_limit}")
    

    if multi:

        threads = []
        for dictionary in get_data_dict["master_dict_list"]:
            time.sleep(.25)
            # Update simulation status box in REEDR.xlsm...
            status = "...running model " + str(i) + " of " + str(len(get_data_dict["df"])) + "..."

            run_label = dictionary["Run Label"]
            location_pull = dictionary["Weather File"]

            if len(threads) >= thread_limit:
                # print("Thread limit reached.  Resolving threads...")
                for thread in threads:
                    time.sleep(.25)
                    thread.join()
                    # threads.pop(thread)
                    thread._stop()
                    time.sleep(.1)

                threads = []
                # thread_limit += 8
            
            print(status)
                

            try:
                t = threading.Thread(target=plusterwolf, args=(run_label, location_pull, get_data_dict["master_directory"], gui_params["path_val"], i, get_data_dict["df"]))
                # t.setName(run_label + "t")
                threads.append(t)
                t.start()

            except:
                print("\n*** ERROR: Problem running EnergyPlus. Please check to make sure you have a valid EnergyPlus exe path.\n")
                return True

            i = i + 1

        for thread in threads:
            # print(thread)
            thread.join()
            thread._stop()

    else:
        for dictionary in get_data_dict["master_dict_list"]:
            # Update simulation status...
            status = "...running model " + str(i) + " of " + str(len(get_data_dict["df"])) + "..."
            print(status)
    
            run_label = dictionary["Run Label"]
            location_pull = dictionary["Weather File"]
    
            try:
                plusterwolf(run_label, location_pull, get_data_dict["master_directory"], gui_params["path_val"], i, get_data_dict["df"])
            except:
                print("\n*** ERROR: Problem running EnergyPlus. Please check to make sure you have a valid EnergyPlus exe path.\n")
                return True
    
            i = i + 1

    print("...model runs complete.")
    print()

    return False