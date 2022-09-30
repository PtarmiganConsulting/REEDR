import os
import pandas as pd # to import xcel, some initial data manipulation
from pathlib import Path # for getting current directory path
import shutil # for removing full directories
from openpyxl import load_workbook
import warnings
from pprint import pprint #for debugging

def getdata(gui_params):

    warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

    # Update simulation status...
    status = "Reading user input data..."
    print(status)

    # Get paths for the current and parent directories
    cwd = Path(os. getcwd())
    parent = cwd.parent.absolute()

    # Sets the directory.
    set_dir = parent

    # Get REEDR workbook path and directory
    REEDR_wb_dirname = set_dir
    REEDR_wb_name = "Model Input Template.xlsx"
    REEDR_wb = os.path.join(set_dir, REEDR_wb_name)
    
    #Define project directory name
    project_dirname = "Projects"

    # Define Project Setup and Model Input worksheets. These need to be the exact tabnames in the "REEDR.xlsx" workbook.
    Model_Input_ws = 'Model_Inputs'
    #Project_Setup_ws = 'Project Setup' - KEEP IN CASE WE NEED TO REVERT TO EXCEL PROJECT SETUP INTERFACE

    # Load Excel workbook with model inputs
    try:
        wb = load_workbook(REEDR_wb) # add argument "keep_vba=True" if reverting back to macro-enabled workbook
    except:
        print("\n*** ERROR: Could not load model input template. ***")
        print("Please ensure the input file \"" + REEDR_wb_name + "\" is available in the directory \"" + str(REEDR_wb_dirname) + "\".\n")
        get_data_d = {
            "error_status":True,
        }
        return get_data_d
    #sht1 = wb[Project_Setup_ws] - KEEP IN CASE WE NEED TO REVERT TO EXCEL PROJECT SETUP INTERFACE

    ## Next block reads "Project Setup" sheet in "REEDR.xlsm" into a Pandas dataframe, and read in Project Name and Output Granularity.
    # ... read in sheet as dataframe...
    #dir_sheet = pd.read_excel(REEDR_wb, sheet_name=Project_Setup_ws)
    #... harvest EPlus.exe directory
    eplus_directory = gui_params["path_val"]
    #eplus_directory = sht1.range('EPlus_exe').value
    # # ... read in user-assigned Project Name and create Project path...
    project_name = gui_params["project_val"]
    # project_name = sht1.range('project_name').value
    master_directory = os.path.join(set_dir, project_dirname, project_name) # note -- python indexes start at 0, and Pandas excludes the labels row from the dataframe
    # # ... read in user-assigned Output Granularity...
    output_gran =gui_params["output_gran"]
    # output_gran = sht1.range('output_gran').value
    # # ... read in user-assigned Output End Uses...
    output_enduses = gui_params["output_enduses"]
    # output_enduses = sht1.range('output_enduses').value
    # # ... read in user-assigned simulation run period...
    sim_runperiod = gui_params["sim_type"]
    # sim_runperiod = sht1.range('sim_runperiod').value
    # # ... read in user-assigned begin mo (only used for sub-annual sim_runperiods)...
    begin_mo_in = gui_params["begin_mo"]
    # begin_mo_in = sht1.range('begin_mo').value
    # # ... read in user-assigned begin day (only used for sub-annual sim_runperiods)...
    begin_day_in = gui_params["begin_day"]
    # begin_day_in = sht1.range('begin_day').value
    # # ... read in user-assigned end mo (only used for sub-annual sim_runperiods)...
    end_mo_in = gui_params["end_mo"]
    # end_mo_in = sht1.range('end_mo').value
    # # ... read in user-assigned end day (only used for sub-annual sim_runperiods)...
    end_day_in = gui_params["end_day"]
    # end_day_in = sht1.range('end_day').value

    # Determine Annual or Sub-Annual simulation period...
    if sim_runperiod == "Annual":
        begin_mo = 1
        begin_day = 1
        end_mo = 12
        end_day = 31
        sim_type = "Annual"
    elif sim_runperiod == "Sub-Annual: enter start and end dates at right -->":
        try:
            begin_mo = int(begin_mo_in)
            begin_day = int(begin_day_in)
            end_mo = int(end_mo_in)
            end_day = int(end_day_in)
            sim_type = "Sub-Annual"
        except:
            print("\n*** ERROR: Requested sub-annual simulation without valid start and end dates. ***")
            print("Please enter a valid start month, start day, end month, and end day.\n")
            get_data_d = {
                "error_status":True,
            }
            return get_data_d
    else:
        sim_type = "Test Run"
        begin_mo = 1
        begin_day = 1
        end_mo = 1
        end_day = 1

    # Creates the user-assigned project directory; removes it first if it exists.
    if os.path.exists(master_directory) == True:
        shutil.rmtree(master_directory) # first delete the directory if it already exists
        os.mkdir(master_directory) # and then make new directory
    else:
        os.mkdir(master_directory) # if directory doesn't exist, just create it

    #Create RunLog.txt...
    runlog_path = os.path.join(master_directory, "RunLog.txt")
    if os.path.exists(os.path.join(runlog_path)) == True:
        os.remove(os.path.join(runlog_path))
    else:
        runlog = open(runlog_path,'w')
        runlog.write("Run log successfully created at " + runlog_path + ". \n" + "... \n")

    ## Next block reads in user model inputs into a Pandas dataframe and creates a master list with a bunch of dictionaries in it.
    # ... read in "Model Input" sheet in "REEDR.xlsm" as a Pandas dataframe.
    try:
        df = pd.read_excel(REEDR_wb, sheet_name=Model_Input_ws)
    except:
        print("\n*** ERROR: Could not find necessary model input worksheet. ***")
        print("Please ensure the worksheet \"" + Model_Input_ws + "\" is available in the file \"" + str(REEDR_wb) + "\".\n")
        get_data_d = {
            "error_status":True,
        }
        return get_data_d

    runlog.write("User inputs successfully read from " + Model_Input_ws + " sheet of " + REEDR_wb + " workbook. \n" + "... \n")

    #... creates one master list with a bunch of dictionaries in it
    #... Each dictionary corresponds to a complete runlabel row.
    #... The dictionaries naturally appear in the list in the order their runlabels appear on the Excel sheet.
    keylist = (list(df.columns)) # grabs keys for our dictionary by harvesting the column names on our excel sheet
    master_dict_list = []
    for i in range(len(df)): # go through every runlabel row...
        present_row = list(df.loc[i])
        dict = {}
        for ii in range(len(keylist)):
            dict.update({keylist[ii]:present_row[ii]}) # ...pair every field with the corresponding key...
        master_dict_list.append(dict) # ...and add it to the dict list
    
    # print(master_dict_list) for debugging...once again looks good, wtf #####

    get_data_d = {
        "cwd":cwd,
        "parent":parent,
        #"sht1":sht1, - CURRENTLY UNUSED
        "REEDR_wb":REEDR_wb,
        "master_directory":master_directory,
        "Model_Input_ws":Model_Input_ws,
        "master_dict_list":master_dict_list,
        "df":df,
        "runlog":runlog,
        "eplus_directory":eplus_directory,
        "begin_mo": begin_mo,
        "begin_day": begin_day, 
        "end_mo": end_mo, 
        "end_day": end_day, 
        "sim_type": sim_type,
        "error_status": False,
    }
    
    # Update simulation status...
    status = "... input data processing complete.\n"
    print(status)

    # print("Get data dict") ###
    # pprint(get_data_d) ### for debugging
    return  get_data_d
