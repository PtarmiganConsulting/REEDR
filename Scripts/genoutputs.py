## Import "external" modules needed for REEDR...
import pandas as pd # used to handle data tables, i.e. "dataframes", or "dfs"
import os # used to remove files
from pprint import pprint # used to print dataframes to command prompt in more legible way for debugging

## Import "internal" modules needed for REEDR...
from unitconversions import convert_J_to_kWh, convert_J_to_therm, convert_W_to_Btuh, convert_degC_to_degF


## Main fuction used to generate custom output reports for REEDR.
## This function takes:
##   1) user inputs (i.e. instructions) on requested output granularity and end uses, and
##   2) EnergyPlus-generated outputs from individual runs
## to create a custom report that combines output from all EnergyPlus runs.
def genoutputs(gui_params, get_data_dict):

    # Set the proper working directory.
    set_dir = get_data_dict["parent"]

    # Update simulation status box in Excel interface...
    status = "Generating model output..."
    #sht1.range('status_line_3').value = status
    print(status)

    # Used to print dataframes to command prompt in more legible way for debugging
    # Sets options to view full dataframe when printed
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000

    ## Define output dictionaries. These become the data fields (i.e. columns) for the custom report.
    Energy_All_End_Uses_dict = {"Run_Label": ['Run_Label', "Run_Label"],
    "Total_Elec[kWh]": ['Electricity:Facility [J](Annual)', "Elec"],
    "Total_Gas[therm]": ['NaturalGas:Facility [J](Annual)', "Gas"],
    "Total_Heat_Elec[kWh]": ['Heating:Electricity [J](Annual)', "Elec"],
    "Prim_Furnace_Heat_Elec[kWh]": ['HEATING_RESISTANCE_MAIN:Heating Coil Heating Energy [J](Annual)', "Elec"],
    "ASHP_Backup_Heat_Elec[kWh]": ['HEATING_RESISTANCE_BACKUP:Heating Coil Heating Energy [J](Annual)', "Elec"],
    "Baseboard_Heat_Elec[kWh]": ['BASEBOARDELECTRIC:Baseboard Total Heating Energy [J](Annual)', "Elec"],
    "Cool_Elec[kWh]": ['Cooling:Electricity [J](Annual)', "Elec"],
    "Fan_Elec[kWh]": ['Fans:Electricity [J](Annual)', "Elec"],
    "Pump_Elec[kWh]": ['Pumps:Electricity [J](Annual)', "Elec"],
    "DHW_Elec[kWh]": ['WaterSystems:Electricity [J](Annual)', "Elec"],
    "IntLights_Elec[kWh]": ['InteriorLights:Electricity [J](Annual)', "Elec"],
    "ExtLights_Elec[kWh]": ['ExteriorLights:Electricity [J](Annual)', "Elec"],
    "Total_IntEquip_Elec[kWh]": ['InteriorEquipment:Electricity [J](Annual)', "Elec"],
    "IntEquip_Range_Elec[kWh]": ['electric_range:InteriorEquipment:Electricity [J](Annual)', "Elec"],
    "IntEquip_Dryer_Elec[kWh]": ['electric_dryer:InteriorEquipment:Electricity [J](Annual)', "Elec"],
    "IntEquip_Misc_Elec[kWh]": ['electric_mels:InteriorEquipment:Electricity [J](Annual)', "Elec"],
    "HeatRecov_Elec[kWh]": ['HeatRecovery:Electricity [J](Annual)', "Elec"],
    "Total_Heat_Gas[therm]": ['Heating:NaturalGas [J](Annual)', "Gas"],
    #"Prim_Furnace_Heat_Gas[therm]": ['HEATING_FUEL_MAIN:Heating Coil Heating Energy [J](Annual)', "Gas"],
    #"ASHP_Backup_Heat_Gas[kWh]": ['HEATING_FUEL_BACKUP:Heating Coil Heating Energy [J](Annual)', "Gas"],
    "DHW_Gas[therm]": ['WaterSystems:NaturalGas [J](Annual)', "Gas"],
    "Total_IntEquip_Gas[therm]": ['InteriorEquipment:NaturalGas [J](Annual)', "Gas"],
    "IntEquip_Range_Gas[therm]": ['gas_range:InteriorEquipment:NaturalGas ', "Gas"],
    "IntEquip_Dryer_Gas[therm]": ['gas_dryer:InteriorEquipment:NaturalGas [J](Annual)', "Gas"],
    "UnmetHours_Heating": ['Facility:Facility Heating Setpoint Not Met Time [hr](Annual)', "NA"],
    "UnmetHours_Cooling": ['Facility:Facility Cooling Setpoint Not Met Time [hr](Annual)', "NA"],
    "Infiltration_Living[ACH]": ['LIVING:AFN Zone Infiltration Air Change Rate [ach](Annual)', "NA"],
    "Infiltration_Attic[ACH]": ['ATTIC:AFN Zone Infiltration Air Change Rate [ach](Annual)', "NA"],
    "Infiltration_Crawlspace[ACH]": ['CRAWLSPACE:AFN Zone Infiltration Air Change Rate [ach](Annual)', "NA"],
    "Infiltration_UnheatedBasement[ACH]": ['UNHEATEDBSMT:AFN Zone Infiltration Air Change Rate [ach](Annual)', "NA"],
    }

    Demand_Total_Electric_HVAC_dict = {"Total_Electric_HVAC[W]": ['Whole Building:Facility Total HVAC Electricity Demand Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Living_Zone_Air_Temperature[F]": ['LIVING_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Attic_Zone_Air_Temperature[F]": ['ATTIC_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Crawlspace_Zone_Air_Temperature[F]": ['CRAWLSPACE_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    }

    Demand_Heating_dict = {"ASHP_Compressor_Heat[W]": ['MAIN DX HEATING COIL_UNIT1:Heating Coil Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "ASHP_Resistance_Backup_Heat[W]": ['SUPP HEATING COIL_UNIT1:Heating Coil Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Electric_Furnace_Heat[W]": ['MAIN ELECTRIC HEATING COIL_UNIT1:Heating Coil Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Gas_Furnace_Gas_Heat[Btu/h]": ['MAIN FUEL HEATING COIL_UNIT1:Heating Coil NaturalGas Rate [W]' + '(' + gui_params["output_gran"] +')', "Gas"],
    "Gas_Furnace_Electric_Heat[W]": ['MAIN FUEL HEATING COIL_UNIT1:Heating Coil Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Living_Zone_Air_Temperature[F]": ['LIVING_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Attic_Zone_Air_Temperature[F]": ['ATTIC_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Crawlspace_Zone_Air_Temperature[F]": ['CRAWLSPACE_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    }

    Demand_Cooling_dict = {"Cooling[W]": ['DX COOLING COIL_UNIT1:Cooling Coil Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Living_Zone_Air_Temperature[F]": ['LIVING_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Attic_Zone_Air_Temperature[F]": ['ATTIC_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Crawlspace_Zone_Air_Temperature[F]": ['CRAWLSPACE_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    }

    Demand_Fan_dict = {"Main_Supply_Fan[W]": ['SUPPLY FAN_UNIT1:Fan Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "OA_Supply_Fan[W]": ['OASUPPLYFAN_UNIT1:Fan Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "OA_Exhaust_Fan[W]": ['OAEXHAUSTFAN_UNIT1:Fan Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Living_Zone_Air_Temperature[F]": ['LIVING_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Attic_Zone_Air_Temperature[F]": ['ATTIC_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    "Crawlspace_Zone_Air_Temperature[F]": ['CRAWLSPACE_UNIT1:Zone Mean Air Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    }

    Demand_Lighting_dict = {"Hardwired_Lighting[W]": ['LIVING HARDWIRED LIGHTING1:Lights Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Plugin_Lighting[W]": ['LIVING PLUG-IN LIGHTING1:Lights Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    }

    Demand_Water_Heating_dict = {"Electric_Water_Heater[W]": ['WATER HEATER_UNIT1:Water Heater Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Gas_Water_Heater[Btu/h]": ['WATER HEATER_UNIT1:Water Heater NaturalGas Rate [W]' + '(' + gui_params["output_gran"] +')', "Gas"],
    "Mains_Water_Temp[F]": ['Environment:Site Mains Water Temperature [C]' + '(' + gui_params["output_gran"] +')', "Temp"],
    }

    Demand_Other_Electric_Equipment_dict = {"Dishwasher[W]": ['DISHWASHER1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Refrigerator[W]": ['REFRIGERATOR1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Clothes_Washer[W]": ['CLOTHESWASHER1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Electric_Dryer[W]": ['ELECTRIC_DRYER1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Electric_Range[W]": ['ELECTRIC_RANGE1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Television[W]": ['TELEVISION1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Miscellaneous_Electric_Loads_1[W]": ['ELECTRIC_MELS1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    "Miscellaneous_Electric_Loads_2[W]": ['IECC_ADJ1:Electric Equipment Electricity Rate [W]' + '(' + gui_params["output_gran"] +')', "Elec"],
    }

    # Build Demand_All_End_Use dictionary by combining all individual end use dictionaries
    Demand_All_End_Uses_dict = {}
    for d in (Demand_Total_Electric_HVAC_dict, Demand_Heating_dict, Demand_Cooling_dict, Demand_Fan_dict, Demand_Lighting_dict, Demand_Water_Heating_dict, Demand_Other_Electric_Equipment_dict):
        Demand_All_End_Uses_dict.update(d)

    # Write to RunLog...
    get_data_dict["runlog"].write("Starting to read model outputs... \n ...\n")

    ## Determine report type to output based on user input...
    #... determine whether to create an energy or demand report
    if gui_params["output_gran"] == "Annual":
        output_type = "Energy"
        output_enduses = "All_End_Uses" # if outputting annual energy report, always report all end uses
    else:
        output_type = "Demand"
    #... determine report name
    report_name = output_type + "_" + gui_params["output_enduses"] # make sure this comes from dictionary
    #... determine which output dictionary to use for report, defined as a string
    output_dict_str = output_type + "_" + gui_params["output_enduses"] + "_dict" # make sure this comes from dictionary
    #... convert string to a dictionary, so that it can be properly processed below
    output_dict = locals()[output_dict_str]
    #... write to RunLog...
    get_data_dict["runlog"].write("Producing report for " + report_name + "... \n")

    ## This is the main function ("sub-routine") that generates the actual custom report.
    ## It takes as arguments the working directory (set_dir), the proper output dictionary (output_dict),
    ## the proper report name (report_name), and the requested output granularity (output_gran).
    ## From there, it takes the proper outputs from the individual EnergyPlus-generated output files
    ## and creates a new, custom report in Excel that combines all runs.
    produce_output_report(set_dir, output_dict, report_name, gui_params["output_gran"], output_type, get_data_dict)

    # Update simulation status box in REEDR.xlsm...
    #sht1.range('status_line_3').value = "Generating model output... Model output complete."
    get_data_dict["runlog"].write("...\nModel output complete.")

    # sub = subprocess.Popen("cmd /k")

    print("...model output complete.")
    print()

    return False

## This is the main function ("sub-routine") that generates the actual custom report.
## It takes as arguments the working directory (set_dir), the proper output dictionary (output_dict),
## the proper report name (report_name), the requested output granularity (output_gran), and the output type (energy or demand: output_type).
## From there, it takes the proper outputs from the individual EnergyPlus-generated output files
## and creates a new, custom report in Excel that combines all runs.
def produce_output_report(set_dir, output_dict, end_use_report_name, output_gran, output_type, get_data_dict):

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
        timestep = row["Timesteps Per Hr"]

        # Update simulation status box in REEDR.xlsm...
        status = "...generating output for run " + str(i) + " of " + str(len(df_for_run_labels)) + "..."
        print(status)
        #sht1.range('status_line_3').value = status

        # Get the path to the EnergyPlus output csv for each run
        eplus_out_path = get_data_dict["master_directory"] + '/' + run_label + '/' + "eplusout.csv"

        if output_gran == "Annual":
            # Read in the EnergyPlus-generated output csv
            eplus_out_df = pd.read_csv (eplus_out_path)

            for column in column_header_list:
                try:
                    if output_dict[column][1] == "Run_Label":
                        # Fill in the first column with the Run_Labels, so we know which run the output corresponds to
                        df_out.at[run_label, column] = run_label
                    elif output_dict[column][1] == "Elec":
                        # Convert electric output from joules to kWh
                        df_out.at[run_label, column] = convert_J_to_kWh(eplus_out_df[output_dict[column][0]].sum())
                    elif output_dict[column][1] == "Gas":
                        # Convert gas output from joules to therms
                        df_out.at[run_label, column] = convert_J_to_therm(eplus_out_df[output_dict[column][0]].sum())
                    else:
                        # Units don't need to be converted; simply sum them up
                        df_out.at[run_label, column] = eplus_out_df[output_dict[column][0]].sum()
                except:
                    # If it can't find an output, it means the EnergyPlus model doesn't have any equipment of this end use, so energy consumption is zero.
                    df_out.at[run_label, [column]] = 0

        else: # Case is hourly or timestep granularity...

            # Compute output timestep for hourly and timestep output
            if output_gran == "Hourly":
                output_timesteps_per_hr = 1
            elif output_gran == "TimeStep":
                output_timesteps_per_hr = timestep

            # Skip the first rows corresponding to the HVAC design days
            rows_to_skip = range(1, 24*2*output_timesteps_per_hr+1)
            # Read in each individual EnergyPlus-generated output file, and skip the first design day rows
            eplus_out_df = pd.read_csv (eplus_out_path, skiprows=rows_to_skip)
            # Strip leading or trailing whitespace from column names...
            eplus_out_df.columns = eplus_out_df.columns.str.strip()
            # Insert the Run_label into the first column of the file
            eplus_out_df.insert(1, "Run Label", run_label)
            # Concat the individual EnergyPlus run to the end of the custom report file, thus combining output from all EnergyPlus runs
            df_out = pd.concat([df_out, eplus_out_df])

        # Update run log
        get_data_dict["runlog"].write("... sucessfully read outputs for run " + run_label + "\n")
        # Update sim status counter
        i = i + 1

    # Create path string for new custom report
    out_path = get_data_dict["master_directory"] + '/' + end_use_report_name + ".xlsx"
    # If path already exists, remove it, to be overwritten
    if os.path.exists(out_path) == True:
        try:
            os.remove(out_path)
        except Exception as e:
            print(e)
            # Write error to RunLog
            get_data_dict["runlog"].write("!!! Could not remove existing output file. REEDR experienced the following error: " + str(e) + " \n")

    ## Rename column headers in df with simpler, more descriptive names
    ## AND convert units where necessary
    if output_type == "Demand":
        for key in output_dict:
            # Rename column headers
            try:
                df_out = df_out.rename(columns = {output_dict[key][0]:key})
            except Exception as e:
                print("Could not rename column" + output_dict[key][0] + " to " + key)
                print(e)
            # Convert units
            if output_dict[key][1] == "Gas":
                try:
                    df_out[key] = convert_W_to_Btuh(df_out[key])
                except Exception as e:
                    print(e)
            if output_dict[key][1] == "Temp":
                try:
                    df_out[key] = convert_degC_to_degF(df_out[key])
                except Exception as e:
                    print(e)

    # Paste output dataframe (custom report) to the path created just above.
    df_out.to_excel(out_path, sheet_name="Sheet1", float_format="%.2f", header=True, index=False, startrow=0, startcol=0)


# getList is a function that takes a dictionary and returns the keys of that dictionary as a list.
def getList(dict):
    return dict.keys()
