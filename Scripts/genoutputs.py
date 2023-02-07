#*******************************************************************************************************************************************************************

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************

## Import "external" modules needed for REEDR...
import pandas as pd # used to handle data tables, i.e. "dataframes", or "dfs"
import os # used to remove files
from pprint import pprint # used to print dataframes to command prompt in more legible way for debugging
import datetime
import pytz
from pathlib import Path

## Import "internal" modules needed for REEDR...
from Scripts.unitconversions import convert_J_to_kWh, convert_J_to_therm, convert_W_to_Btuh, convert_degC_to_degF, convert_J_to_galLPG
from Scripts.xlsxadjust import adapt_spreadsheet
from Scripts.dictmaker import dict_maker

## Main fuction used to generate custom output reports for REEDR.
## This function takes:
##   1) user inputs (i.e. instructions) on requested output granularity and end uses, and
##   2) EnergyPlus-generated outputs from individual runs
## to create a custom report that combines output from all EnergyPlus runs.
def genoutputs(gui_params, get_data_dict, control_panel_dict):

    # Set the proper working directory.
    set_dir = get_data_dict["parent"]

    ### --- Define control panel directory and file names as variables, so they can be established only once here, and flow throughout --- ###
    #... get folder and file names from CSV
    control_panel_folder_name = control_panel_dict["control_panel_folder_name"]
    control_panel_names_dict = control_panel_dict["control_panel_names_dict"]
    control_panel_names_lookup_id = control_panel_dict["control_panel_names_lookup_id"]
    #... assign fieldnames to python variables
    output_reports_dir = control_panel_names_dict["output_reports_dir"][control_panel_names_lookup_id]
    output_reports_demand_allEndUse_file = control_panel_names_dict["output_reports_demand_allEndUse_file"][control_panel_names_lookup_id]
    output_reports_demand_allHVAC_file = control_panel_names_dict["output_reports_demand_allHVAC_file"][control_panel_names_lookup_id]
    output_reports_demand_cooling_file = control_panel_names_dict["output_reports_demand_cooling_file"][control_panel_names_lookup_id]
    output_reports_demand_fan_file = control_panel_names_dict["output_reports_demand_fan_file"][control_panel_names_lookup_id]
    output_reports_demand_heating_file = control_panel_names_dict["output_reports_demand_heating_file"][control_panel_names_lookup_id]
    output_reports_demand_lighting_file = control_panel_names_dict["output_reports_demand_lighting_file"][control_panel_names_lookup_id]
    output_reports_demand_other_file = control_panel_names_dict["output_reports_demand_other_file"][control_panel_names_lookup_id]
    output_reports_demand_dhw_file = control_panel_names_dict["output_reports_demand_dhw_file"][control_panel_names_lookup_id]
    output_reports_energy_allEndUse_file = control_panel_names_dict["output_reports_energy_allEndUse_file"][control_panel_names_lookup_id]

    # candidate for revision after changes to get_data_dict
    cwd = Path(os. getcwd())
    parent = cwd.parent.absolute() 

    # Update simulation status box in Excel interface...
    status = "Generating model output..."
    print(status)

    # Used to print dataframes to command prompt in more legible way for debugging
    # Sets options to view full dataframe when printed
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000

    ## Define output dictionaries. These become the data fields (i.e. columns) for the custom report.

    Energy_All_End_Uses_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_energy_allEndUse_file)
    Energy_All_End_Uses_dict = dict_maker(Energy_All_End_Uses_path)

    Demand_All_HVAC_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_allHVAC_file)
    Demand_All_HVAC_dict = dict_maker(Demand_All_HVAC_path)

    Demand_Heating_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_heating_file)
    Demand_Heating_dict = dict_maker(Demand_Heating_path)

    Demand_Cooling_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_cooling_file)
    Demand_Cooling_dict = dict_maker(Demand_Cooling_path)

    Demand_Fan_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_fan_file)
    Demand_Fan_dict = dict_maker(Demand_Fan_path)

    Demand_Lighting_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_lighting_file)
    Demand_Lighting_dict = dict_maker(Demand_Lighting_path)

    Demand_Water_Heating_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_dhw_file)
    Demand_Water_Heating_dict = dict_maker(Demand_Water_Heating_path)

    Demand_Other_Equipment_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_other_file)
    Demand_Other_Equipment_dict = dict_maker(Demand_Other_Equipment_path)

    Demand_All_End_Uses_path = os.path.join(set_dir, control_panel_folder_name, output_reports_dir, output_reports_demand_allEndUse_file)
    Demand_All_End_Uses_dict = dict_maker(Demand_All_End_Uses_path)

    ## Determine report type to output based on user input...
    #... determine whether to create an energy or demand report
    if gui_params["output_gran"] == "Annual":
        output_type = "Energy"
        output_enduses = "All_End_Uses" # if outputting annual energy report, always report all end uses
    else:
        output_type = "Demand"
    #... determine which output dictionary to use for report, defined as a string
    output_dict_str = output_type + "_" + gui_params["output_enduses"] + "_dict" # make sure this comes from dictionary
    #... convert string to a dictionary, so that it can be properly processed below
    output_dict = locals()[output_dict_str]
    #... if demand analysis, add timestep to end of EnergyPlus output fieldname
    if output_type == "Demand":
        for key in output_dict:
            output_dict[key]["mapping_fieldname"] = str(output_dict[key]["mapping_fieldname"]) + "(" + str(gui_params["output_gran"]) + ")"

    #... create path for output workbook
    out_path = get_data_dict["master_directory"] + "/RunReport_" + str(gui_params["project_val"]) + ".xlsx"

    ## This is the main function ("sub-routine") that generates the actual custom report.
    ## It takes as arguments the working directory (set_dir), the proper output dictionary (output_dict),
    ## the proper report name (report_name), and the requested output granularity (output_gran).
    ## From there, it takes the proper outputs from the individual EnergyPlus-generated output files
    ## and creates a new, custom report in Excel that combines all runs.
    produce_output_report(output_dict, gui_params["output_gran"], output_type, get_data_dict, gui_params["output_enduses"], out_path)

    if gui_params["output_gran"] != "Annual":
        adapt_spreadsheet(out_path)

    print("...model output complete.")
    print()

    return False

## This is the main function ("sub-routine") that generates the actual custom report.
## It takes as arguments the working directory (set_dir), the proper output dictionary (output_dict),
## the proper report name (report_name), the requested output granularity (output_gran), and the output type (energy or demand: output_type).
## From there, it takes the proper outputs from the individual EnergyPlus-generated output files
## and creates a new, custom report in Excel that combines all runs.
def produce_output_report(output_dict, output_gran, output_type, get_data_dict, output_enduses, out_path):
    
    # Get run labels for output table
    df_for_run_labels = pd.read_excel(get_data_dict["REEDR_wb"], sheet_name=get_data_dict["Model_Input_ws"]) # This is the sheet with the model inputs
    run_label_list = df_for_run_labels['Run Label'].tolist()

    # Get column names/output fields for output table
    # Note: getList is a function that takes a dictionary and returns the keys of that dictionary as a list.
    column_header_list = getList(output_dict)

    # Create output dataframes...
    if output_gran == "Annual":
        # Dimenions of annual report are pre-determined, so dataframe dims can be specified here...
        df_out = pd.DataFrame(index=run_label_list, columns=column_header_list)
    else:
        # Dimenions of sub-annual report could be pre-determined, but are more variable, so for now we just create an empty dataframe...
        df_out = pd.DataFrame()

    # Set counter used to update simulation progress to 1...
    i = 1
    ## Main loop that fills output dataframe.
    for row in get_data_dict["master_dict_list"]: # go through every runlabel row...
        run_label = row["Run Label"]
        timestep = row["Timesteps Per Hour"]

        # Update simulation status...
        status = "...generating output for run " + str(i) + " of " + str(len(df_for_run_labels)) + "..."
        print(status)

        # Get the path to the EnergyPlus output csv for each run
        eplus_out_path = get_data_dict["master_directory"] + '/' + run_label + '/' + "eplusout.csv"

        if output_gran == "Annual":
            # Read in the EnergyPlus-generated output csv
            #... skip the first rows corresponding to the HVAC design days
            rows_to_skip = range(1, 3)
            eplus_out_df = pd.read_csv (eplus_out_path, skiprows=rows_to_skip)
            
            for column in column_header_list:
                try:
                    if output_dict[column]["conversion_ID"] == "Run_Label":
                        # Fill in the first column with the Run_Labels, so we know which run the output corresponds to
                        df_out.at[run_label, column] = run_label
                    elif output_dict[column]["conversion_ID"] == "Elec":
                        # Convert electric output from joules to kWh
                        col_lookup = str(output_dict[column]["mapping_fieldname"]) + "(RunPeriod)"
                        df_out.at[run_label, column] = convert_J_to_kWh(eplus_out_df[col_lookup].sum())
                    elif output_dict[column]["conversion_ID"] == "Gas":
                        # Convert gas output from joules to therms
                        col_lookup = str(output_dict[column]["mapping_fieldname"]) + "(RunPeriod)"
                        df_out.at[run_label, column] = convert_J_to_therm(eplus_out_df[col_lookup].sum())
                    elif output_dict[column]["conversion_ID"] == "Propane":
                        # Convert propane output from joules to gallons
                        col_lookup = str(output_dict[column]["mapping_fieldname"]) + "(RunPeriod)"
                        df_out.at[run_label, column] = convert_J_to_galLPG(eplus_out_df[col_lookup].sum())
                    else:
                        # Units don't need to be converted; simply sum them up
                        col_lookup = str(output_dict[column]["mapping_fieldname"]) + "(RunPeriod)"
                        df_out.at[run_label, column] = eplus_out_df[col_lookup].sum()
                except:
                    # If it can't find an output, it means the EnergyPlus model doesn't have any equipment of this end use, so energy consumption is zero.
                    df_out.at[run_label, [column]] = 0

        else: # Case is hourly or timestep granularity...

            # Compute output timestep for hourly and timestep output
            if output_gran == "Hourly":
                output_timesteps_per_hr = 1
            elif output_gran == "TimeStep":
                output_timesteps_per_hr = timestep

            # Skip the last rows corresponding to the HVAC design days
            endrows_to_skip = 24*2*output_timesteps_per_hr
            # Read in each individual EnergyPlus-generated output file, and skip the last design day rows
            eplus_out_df = pd.read_csv(eplus_out_path, engine='python', skipfooter=endrows_to_skip)
            # Strip leading or trailing whitespace from column names...
            eplus_out_df.columns = eplus_out_df.columns.str.strip()
            # Insert the Run_label into the first column of the file
            eplus_out_df.insert(1, "Run Label", run_label)
            # Concat the individual EnergyPlus run to the end of the custom report file, thus combining output from all EnergyPlus runs
            df_out = pd.concat([df_out, eplus_out_df])

        # Update sim status counter
        i = i + 1

    # If path already exists, remove it, to be overwritten
    if os.path.exists(out_path) == True:
        try:
            os.remove(out_path)
        except:
            print("\n*** ERROR: Could not remove RunReport. Please ensure that RunReport is not open when running REEDR.\n")
            return True

    ## Rename column headers in df with simpler, more descriptive names
    ## AND convert units where necessary
    if output_type == "Demand":
        for key in output_dict:
            # Rename column headers
            try:
                df_out = df_out.rename(columns = {output_dict[key]["mapping_fieldname"]:key})
            except:
                pass
            # Convert units
            if output_dict[key]["conversion_ID"] == "Gas" or output_dict[key]["conversion_ID"] == "Propane":
                try:
                    df_out[key] = convert_W_to_Btuh(df_out[key])
                except:
                    pass
            if output_dict[key]["conversion_ID"] == "Temp":
                try:
                    df_out[key] = convert_degC_to_degF(df_out[key])
                except:
                    pass

    # Create Pandas Excel writer so that we can write to multiple Excel sheets
    writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
    
    # Paste output dataframe (custom report) to the path created just above.
    df_out.to_excel(writer, sheet_name="Model Out", header=True, index=False, startrow=0, startcol=0)

    # write model inputs to output report as well
    df_in = get_data_dict["df"]
    df_in.to_excel(writer, sheet_name="Model In", header=True, index=False, startrow=0, startcol=0)

    # get current time
    current_time = datetime.datetime.now(pytz.timezone('US/Pacific'))
    current_time_w_zone = str(current_time) + " US Pacific Time"

    # write run characteristics
    run_chars_dict = {
        "EnergyPlus Directory": [get_data_dict["eplus_directory"]],
        "Model Input Template Directory": [get_data_dict["REEDR_wb"]],
        "Simulation Type": [get_data_dict["sim_type"]],
        "Simulation Begin Month": [get_data_dict["begin_mo"]],
        "Simulation Begin Day": [get_data_dict["begin_day"]],
        "Simulation End Month": [get_data_dict["end_mo"]],
        "Simulation End Day": [get_data_dict["end_day"]],
        "Output Granularity": [output_gran],
        "Output End Uses": [output_enduses],
        "Run Complete Timestamp": [current_time_w_zone],
    }
    run_chars_df = pd.DataFrame.from_dict(run_chars_dict)
    run_chars_df_transposed = run_chars_df.T
    run_chars_df_transposed.to_excel(writer, sheet_name="Run Characteristics", header=False, index=True, startrow=0, startcol=0)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

# getList is a function that takes a dictionary and returns the keys of that dictionary as a list.
def getList(dict):
    return dict.keys()
