### --- Import modules. --- ###
import pandas as pd # to import xcel, some initial data manipulation
import os # for making paths and directories and removing files
import shutil # for removing full directories
import math # used for functions like square root
from pprint import pprint
import datetime
from Scripts.unitconversions import convert_WperFt2_to_WperM2, convert_degF_to_degC, convert_IP_Uvalue_to_SI_Uvalue, convert_ft_to_m, convert_ft2_to_m2, \
    convert_ft3_to_m3, convert_Btuh_to_W, convert_CFM_to_m3PerSec, convert_W_to_ton, convert_in2_to_m2
from Scripts.dictionaries import make_foundation_and_floor_dict, make_hvac_dict, make_foundation_dict, make_foundation_and_floor_dict2
from Scripts.datavalidation import validate, convert_capacity
from Scripts.utilfunctions import estimateInfiltrationAdjustment


def genmodels(gui_params, get_data_dict):

    ### --- Set the main working directory. --- ###
    set_dir = get_data_dict["parent"]

    ### --- Define building block directory and folder names as variables, so they can be established only once here, and flow throughout. --- ###
    building_block_dir = "Building Blocks"
    schedule_dir = "Schedules"
    schedule_elec_gains_dir = "MiscElecGains"
    schedule_gas_gains_dir = "MiscGasGains"
    schedule_file = "Schedules.csv"
    location_and_climate_dir = "LocationAndClimate"
    materials_main_dir = "Materials"
    materials_wall_ins_dir = "AGWallInsulation" # Note: AG = Above Ground
    materials_attic_ins_dir = "AtticInsulation"
    dhw_main_dir = "DHW"
    dhw_wh_type_dir = "WaterHeaterType"
    gains_main_dir = "Gains"
    gains_dryertype_dir = "DryerType"
    gains_rangetype_dir = "RangeType"
    hvac_afn_main_dir = "HVAC_AirFlowNetwork" # Note: AFN = Air Flow Network
    hvac_afn_leakage_dir = "AFN_Leakage"
    hvac_afn_linkage_dir = "AFN_Linkage"
    hvac_afn_node_dir = "AFN_Nodes"
    hvac_afn_surface_dir = "AFN_Surfaces"
    hvac_afn_zone_dir = "AFN_Zones"
    hvac_airloop_main_dir = "HVAC_AirLoop"
    hvac_airloop_hvac_dir = "AirLoopHVAC"
    hvac_coil_dir = "HVAC_Coils"
    hvac_fan_dir = "HVAC_Fans"
    hvac_tstat_dir = "HVAC_Thermostat"
    hvac_zone_main_dir = "HVAC_Zone"
    hvac_zone_hvac_dir = "ZoneHVAC"
    output_dir = "Output"
    window_main_dir = "Windows"
    window_blinds_dir = "Blinds"
    geometry_main_dir = "Geometry"
    geometry_envelope_dir = "Envelope"
    geometry_window_dir = "Windows"
    geometry_zone_dir = "Zones"
    performanceprecision_dir = "PerformancePrecisionTradeoffs"

    ### --- Define user input data field names --- ###
    runLabel_fieldname = "Run Label"
    timestep_fieldname = "Timesteps Per Hour"
    weather_fieldname = "Weather File"
    orient_fieldname = "Building Orientation [deg]"
    footprint_fieldname = "Conditioned Footprint Area [ft^2]"
    volume_fieldname = "Total Conditioned Volume Above Foundation Walls [ft^3]"
    bldgRatio_fieldname = "Building Width to Depth Ratio"
    wallCon_fieldname = "Exterior Non-Foundation Wall Construction"
    ceilingCon_fieldname = "Ceiling And Roof Construction"
    floorCon_fieldname = "Foundation And Floor Construction"
    #foundWallHtAg_fieldname = "Foundation Wall Height Above Ground [ft]"
    #foundWallHtBg_fieldname = "Foundation Wall Height Below Ground [ft]"
    windowuUvalue_fieldname = "Window U-Value [Btu/h-ft^2-F]"
    windowSHGC_fieldname = "Window Solar Heat Gain Coefficient"
    windowShade_fieldname = "Window Shades"
    wtwFront_fieldname = "Window-to-Wall Ratio, Front [%]"
    wtwBack_fieldname = "Window-to-Wall Ratio, Back [%]"
    wtwLeft_fieldname = "Window-to-Wall Ratio, Left [%]"
    wtwRight_fieldname = "Window-to-Wall Ratio, Right [%]"
    infiltration_fieldname = "Conditioned Envelope Infiltration [ACH50]"
    primaryHVAC_fieldname = "Primary HVAC Type"
    primaryHtgCapacityUnits_fieldname = "Primary Heating Capacity Units"
    primaryHtgCapacity_fieldname = "Primary Rated Heating Capacity [@47F OAT]"
    primaryClgCapacityUnits_fieldname = "Primary Cooling Capacity Units"
    primaryClgCapacity_fieldname = "Primary Rated Cooling Capacity [@95F OAT]"
    hpBackupType_fieldname = "ASHP Backup Heat Type"
    hpBackupCapacityUnits_fieldname = "ASHP Backup Heat Capacity Units"
    hpBackupCapacity_fieldname = "ASHP Backup Heat Capacity"
    backupBaseboardCapacity_fieldname = "Backup Electric Baseboard Heat Capacity [kW]"
    hpBackupLockout_fieldname = "ASHP Backup Heat Lockout Temp [deg F]"
    hpCompressorLockout_fieldname = "ASHP Compressor Lockout Temp [deg F]"
    AFUE_fieldname = "Gas Furnace AFUE [%]"
    supplyLeakage_fieldname = "Supply Duct Leakage [%]"
    supplyRvalue_fieldname = "Supply Duct Insulation Nominal R-Value [h-ft^2-F/Btu]"
    returnLeakage_fieldname = "Return Duct Leakage [%]"
    returnRvalue_fieldname = "Return Duct Insulation Nominal R-Value [h-ft^2-F/Btu]"
    htgSched_fieldname = "Heating Setpoint Schedule"
    clgSched_fieldname = "Cooling Setpoint Schedule"
    dhwType_fieldname = "Water Heater Type"
    dhwSched_fieldname = "Water Heater Setpoint Schedule"
    numOfPeople_fieldname = "Number Of People"
    intLPD_fieldname = "Interior Lighting Power Density [W/ft^2]"
    extLP_fieldname = "Exterior Lighting Power [W]"
    range_fieldname = "Range"
    dryer_fieldname = "Dryer"
    frig_fieldname = "Refrigerator"
    cw_fieldname = "Clothes Washer"
    dw_fieldname = "Dishwasher"
    miscElec_fieldname = "Misc Electric Gains [Max W]"
    miscElecShed_fieldname = "Misc Electric Gains Schedule"
    miscGas_fieldname = "Misc Gas Gains [Max Btu/h]"
    miscGasShed_fieldname = "Misc Gas Gains Schedule"

    ### --- Get input variables from tkinter user interface. --- ###
    begin_mo = get_data_dict["begin_mo"]
    begin_day = get_data_dict["begin_day"]
    end_mo = get_data_dict["end_mo"]
    end_day = get_data_dict["end_day"]
    sim_type = get_data_dict["sim_type"]
    output_gran = gui_params["output_gran"]
    output_enduses = gui_params["output_enduses"]

    ### --- Allows tstat to overrun setpoint by a certain amount and drift back down to setpoint before kicking on again. A value of 0.79 empirically results in 
    ### average room temps that are +/- 1 degree F about the desired setpoint. ###
    deadband = "" #0.79

    ### --- Update simulation status in command prompt. --- ###
    print("Starting model build...")

    ### --- Create Schedules.csv file and store headers in a list --- ###
    read_file = pd.read_excel (get_data_dict["REEDR_wb"], sheet_name="Schedules_8760")
    if os.path.exists(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)) == True:
        try:
            os.remove(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file))
            read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)), index = None, header=True)
        except:
            print("\n*** ERROR: Could not remove Schedule File. Please ensure that 8760 Schedule File is not open when running REEDR.\n")
            return True
    else:
        read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)), index = None, header=True)
    
    sched_list = (list(read_file.columns))

    # Make a list for data validation that includes an option for "PNNL Default", and removes non-schedule name fields from list
    PNNL_default = ["PNNL Prototype Default"]
    sched_validation_list = (list(read_file.columns))
    sched_validation_list.extend(PNNL_default)
    del sched_validation_list[:7]

    ### --- Gather the run labels from the user specified runs, and create subdirectories that will house each run's input and output. --- ###
    directory_names = []
    for i in range(len(get_data_dict["df"])): # Note: df is a Pandas dataframe that contains user inputs from the "Model_Inputs" tab in REEDR.xlsx
        directory_names.append(get_data_dict["df"].loc[i][0])

    # get_data_dict["runlog"].write("Starting to build subdirectories under " + os.path.join(get_data_dict["master_directory"]) + ". \n")

    for name in directory_names:
        try:
            path = os.path.join(get_data_dict["master_directory"], name) # Note: the "master directory" is the user-defined "Project" folder
        except:
            print("\n*** ERROR: REEDR encountered an invalid Run Label name. Please ensure that all Run Labels are unique and non-blank.\n")
            return True
        try:
            os.mkdir(path)
        except:
            print("\n*** ERROR: Subdirectory could not be created for the run: " + name + ". ***\nPlease ensure that ALL Run Labels are unique.\n")
            return True

    ### --- Set output end uses and granularity based on user input. --- ###
    if gui_params["output_gran"] == "Annual":
        output_type = "Energy"
    else:
        output_type = "Demand"

    output_lookup = output_type + "_" + gui_params["output_enduses"]

    ### --- Define dictionaries needed for REEDR user inputs. --- ###
    # floor and foundation construction dictionary
    foundation_and_floor_dict = make_foundation_and_floor_dict()
    # hvac type dictionary
    hvac_dict = make_hvac_dict(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, hvac_coil_dir, hvac_fan_dir)
    # foundation type dictionary
    foundation_dict = make_foundation_dict()

    # foundation_and_floor_dict2 = make_foundation_and_floor_dict2()
    # test = foundation_and_floor_dict2["Vented Crawlspace - R0 Cavity Insulation"]["foundation_zone_name"]

    ### --- IDF WRITER LOOP BEGINS HERE. --- ###
    # The loop covers every dictionary (effectively a runlabel row) in the big dictionary list.
    # Each time the loop comes to a new dictionary/runlabel row, it updates the changable variables before doing anything else.

    i = 1
    for dictionary in get_data_dict["master_dict_list"]:

        # Update simulation status...
        print("...building model " + str(i) + " of " + str(len(get_data_dict["df"])) + "...")

        # Create dummy list for cases where a validation list is not needed.
        dummy_list = [999]
        dummy_int = 999

        # Get user inputs from REEDR Excel input file. Each variable below maps to a field in the Excel input sheet.
        #... run_label
        run_label = str(dictionary[runLabel_fieldname])

        try:
            #... timestep
            valid_timesteps = ["1","2","3","4","5","6","10","12","15","20","30","60"]
            timestep = validate(timestep_fieldname, str(dictionary[timestep_fieldname]), "list", dummy_int, dummy_int, valid_timesteps)

            #... location/weather file
            location_path = os.path.join(set_dir, building_block_dir, location_and_climate_dir)
            location_pull = validate(weather_fieldname, dictionary[weather_fieldname], "file", dummy_int, dummy_int, dummy_list, location_path)

             #... building orientation
            bldg_orient_lo = 0
            bldg_orient_hi = 359
            bldg_orient = validate(orient_fieldname, dictionary[orient_fieldname], "num_between", bldg_orient_lo, bldg_orient_hi, dummy_list)

            #... conditioned footprint area
            conditioned_footprint_area = float(validate(footprint_fieldname, round(convert_ft2_to_m2(dictionary[footprint_fieldname]),10), "num_not_zero", 999, 999, dummy_list))

            #... total conditioned volume
            total_conditioned_volume = float(validate(volume_fieldname, round(convert_ft3_to_m3(dictionary[volume_fieldname]),10), "num_not_zero", 999, 999, dummy_list))

            #... Width to depth ratio
            ratio_width_to_depth = validate(bldgRatio_fieldname, dictionary[bldgRatio_fieldname], "num_not_zero", 999, 999, dummy_list)

            #... above ground wall construction
            above_ground_wall_con_path = os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir)
            above_ground_wall_con = validate(wallCon_fieldname, dictionary[wallCon_fieldname], "file", 999, 999, dummy_list, above_ground_wall_con_path)

            #... ceiling and roof construction
            ceiling_and_roof_con_path = os.path.join(set_dir, building_block_dir, materials_main_dir, materials_attic_ins_dir)
            ceiling_and_roof_con = validate(ceilingCon_fieldname, dictionary[ceilingCon_fieldname], "file", 999, 999, dummy_list, ceiling_and_roof_con_path)

            #... foundation and floor construction
            foundation_and_floor_con = str(dictionary[floorCon_fieldname])
            foundation_list = foundation_and_floor_dict.keys()
            foundation_and_floor_con = validate(floorCon_fieldname, dictionary[floorCon_fieldname], "list" , 999, 999, foundation_list)

            # Establish foundation type
            chars = 4
            foundation_key = foundation_and_floor_con[:chars]
            foundation_type = foundation_dict[foundation_key][0]
            returnduct_location = foundation_dict[foundation_key][1]
            # Establish if foundation is slab or heated basement, if using regression-based infiltration estimate
            if foundation_type == "Slab" or foundation_type == "Heated Basement":
                hasSlabOrHtdBsmnt = 1
            else:
                hasSlabOrHtdBsmnt = 0

            #... Foundation wall height above and below ground
            if foundation_type == "Slab":
                #foundationwall_ht_AG = float(validate(foundWallHtAg_fieldname, round(convert_ft_to_m(dictionary[foundWallHtAg_fieldname]),10), "any_num", 999, 999, dummy_list))
                #foundationwall_ht_BG = float(validate(foundWallHtBg_fieldname, -1 * round(convert_ft_to_m(dictionary[foundWallHtBg_fieldname]),10), "any_num", 999, 999, dummy_list))
                foundationwall_ht_AG = round(convert_ft_to_m(0),10)
                foundationwall_ht_BG = -1 * round(convert_ft_to_m(0),10)
            elif foundation_type == "Vented Crawlspace":
                foundationwall_ht_AG = round(convert_ft_to_m(1),10)
                foundationwall_ht_BG = -1 * round(convert_ft_to_m(2),10)
            else:
                #foundationwall_ht_AG = float(validate(foundWallHtAg_fieldname, round(convert_ft_to_m(dictionary[foundWallHtAg_fieldname]),10), "num_not_zero", 999, 999, dummy_list))
                #foundationwall_ht_BG = float(validate(foundWallHtBg_fieldname, -1 * round(convert_ft_to_m(dictionary[foundWallHtBg_fieldname]),10), "num_not_zero", 999, 999, dummy_list))
                foundationwall_ht_AG = round(convert_ft_to_m(1),10)
                foundationwall_ht_BG = -1 * round(convert_ft_to_m(7),10)

            #... window U-value
            u_lo = 0.1
            u_hi = 1.2
            windowu_val = validate(windowuUvalue_fieldname, dictionary[windowuUvalue_fieldname], "num_between", u_lo, u_hi, dummy_list)
            windowu_val = convert_IP_Uvalue_to_SI_Uvalue(dictionary[windowuUvalue_fieldname]) # once validated, convert units...

            #... window SHGC
            SHGC_lo = 0.10
            SHGC_hi = 0.90
            window_shgc = validate(windowSHGC_fieldname, dictionary[windowSHGC_fieldname], "num_between", SHGC_lo, SHGC_hi, dummy_list)

            #... Window shades
            window_shades_list = ["Yes", "No"]
            window_shades = validate(windowShade_fieldname, dictionary[windowShade_fieldname], "list", 999, 999, window_shades_list)

            #... window to wall ratios
            wtw_lo = 0.01
            wtw_hi = 0.99
            wtw_ratio_front = validate(wtwFront_fieldname, dictionary[wtwFront_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)
            wtw_ratio_back = validate(wtwBack_fieldname, dictionary[wtwBack_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)
            wtw_ratio_left = validate(wtwLeft_fieldname, dictionary[wtwLeft_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)
            wtw_ratio_right = validate(wtwRight_fieldname, dictionary[wtwRight_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)

            #... infiltration
            infiltration = validate(infiltration_fieldname, dictionary[infiltration_fieldname], "num_not_zero", 999, 999, dummy_list)

            #... primary HVAC type
            hvac_type_list = hvac_dict.keys()
            hvac_type = validate(primaryHVAC_fieldname, dictionary[primaryHVAC_fieldname], "list", 999, 999, hvac_type_list)
            
            #... heating capacity units
            primaryHVAC_capacity_units_list = ["kBtu/h", "kW", "ton"]
            primaryHtg_capacity_units = validate(primaryHtgCapacityUnits_fieldname, dictionary[primaryHtgCapacityUnits_fieldname], "list", 999, 999, primaryHVAC_capacity_units_list)
            
            #... primary heating capacity
            primary_heating_capacity = validate(primaryHtgCapacity_fieldname, dictionary[primaryHtgCapacity_fieldname], "num_not_zero", 999, 999, dummy_list)
            primary_heating_capacity = convert_capacity(primaryHtg_capacity_units, primary_heating_capacity)

            #... cooling capacity and capacity units
            if hvac_dict[hvac_type][22] == "SS Heat Pump" or hvac_dict[hvac_type][22] == "DS Heat Pump" or hvac_dict[hvac_type][22] == "MS Heat Pump" \
            or hvac_dict[hvac_type][15] != "NA":
                primaryClg_capacity_units = validate(primaryClgCapacityUnits_fieldname, dictionary[primaryClgCapacityUnits_fieldname], "list", 999, 999, primaryHVAC_capacity_units_list)
                primary_cooling_capacity = validate(primaryClgCapacity_fieldname, dictionary[primaryClgCapacity_fieldname], "num_not_zero", 999, 999, dummy_list)
                primary_cooling_capacity = convert_capacity(primaryClg_capacity_units, primary_cooling_capacity)
            else:
                primary_cooling_capacity = 0

            #... heat pump specific inputs
            if hvac_dict[hvac_type][22] == "SS Heat Pump" or hvac_dict[hvac_type][22] == "DS Heat Pump" or hvac_dict[hvac_type][22] == "MS Heat Pump" \
            and hvac_dict[hvac_type][0] == "Central":
                #... ASHP backup heat type
                hp_supp_heat_type_list = ["Electric", "Gas"]
                hp_supp_heat_type = validate(hpBackupType_fieldname, dictionary[hpBackupType_fieldname], "list", 999, 999, hp_supp_heat_type_list)
                #... ASHP backup heat capacity units
                ASHPbackup_capacity_units_list = ["kBtu/h", "kW"]
                ASHPbackup_capacity_units = validate(hpBackupCapacityUnits_fieldname, dictionary[hpBackupCapacityUnits_fieldname], "list", 999, 999, ASHPbackup_capacity_units_list)
                #... ASHP backup heat capacity
                hp_supp_heat_capacity = convert_capacity(ASHPbackup_capacity_units, validate(hpBackupCapacity_fieldname, dictionary[hpBackupCapacity_fieldname], "num_not_zero", 999, 999, dummy_list))
                #... backup heat lockout
                hp_max_resistance_temp = validate(hpBackupLockout_fieldname, convert_degF_to_degC(dictionary[hpBackupLockout_fieldname]), "any_num", 999, 999, dummy_list)
                #... compressor lockout
                hp_min_compressor_temp = validate(hpCompressorLockout_fieldname, convert_degF_to_degC(dictionary[hpCompressorLockout_fieldname]), "any_num", 999, 999, dummy_list)
            else:
                hp_supp_heat_type = "None"
                hp_supp_heat_capacity = 0

            #... baseboard heating capacity
            if str(dictionary[backupBaseboardCapacity_fieldname]) == "nan":
                baseboard_heat_capacity = 0
            else:
                baseboard_heat_capacity = convert_capacity("kW", validate(backupBaseboardCapacity_fieldname, dictionary[backupBaseboardCapacity_fieldname], "any_num", 999, 999, dummy_list))
            
            #... duct inputs
            if hvac_dict[hvac_type][0] == "Central":
                #... duct leakage
                duct_leak_lo = 0.0001
                duct_leak_hi = 0.99
                supply_leak = validate(supplyLeakage_fieldname, dictionary[supplyLeakage_fieldname], "num_between", duct_leak_lo, duct_leak_hi, dummy_list)
                return_leak = validate(returnLeakage_fieldname, dictionary[returnLeakage_fieldname], "num_between", duct_leak_lo, duct_leak_hi, dummy_list)
                #... duct R-value
                supplyRvalue = validate(supplyRvalue_fieldname, dictionary[supplyRvalue_fieldname], "any_num", 999, 999, dummy_list)
                returnRvalue = validate(returnRvalue_fieldname, dictionary[returnRvalue_fieldname], "any_num", 999, 999, dummy_list)
                if supplyRvalue == int(0):
                    supplyUvalue = 6.8 #estimted U-value of thin piece of uninsulated metal duct
                else:
                    supplyUvalue = convert_IP_Uvalue_to_SI_Uvalue(1/supplyRvalue)
                if returnRvalue == int(0):
                    returnUvalue = 6.8 #estimted U-value of thin piece of uninsulated metal duct
                else:
                    returnUvalue = convert_IP_Uvalue_to_SI_Uvalue(1/returnRvalue)
            else:
                #assume essentially no duct leakage, i.e. "perfect ducts", although EPlus does not allow zero.
                supply_leak = 0.0001
                return_leak = 0.0001
                supplyUvalue = 0.0001
                returnUvalue = 0.0001

            #... heating setpoint schedule
            htg_stpt_sch = validate(htgSched_fieldname, dictionary[htgSched_fieldname], "list", 999, 999, sched_validation_list)

            #... cooling setpoint schedule
            clg_stpt_sch = validate(clgSched_fieldname, dictionary[clgSched_fieldname], "list", 999, 999, sched_validation_list)

            #... gas furnace AFUE
            if hvac_dict[hvac_type][18] == "Heating_Fuel_Main" or hp_supp_heat_type == "Gas":
                AFUE_lo = 0.5
                AFUE_hi = 0.99
                gas_furnace_AFUE = validate(AFUE_fieldname, dictionary[AFUE_fieldname], "num_between", AFUE_lo, AFUE_hi, dummy_list)
            
            #... water heater type
            water_heater_type_list = ["Electric Storage_50-gallon", "Gas Storage_50-gallon", "None"]
            water_heater_type = validate(dhwType_fieldname, dictionary[dhwType_fieldname], "list", 999, 999, water_heater_type_list)
            
            #... DHW setpoint schedule
            dhw_stpt_sch = validate(dhwSched_fieldname, dictionary[dhwSched_fieldname], "list", 999, 999, sched_validation_list)

            #... number of people
            people = validate(numOfPeople_fieldname, dictionary[numOfPeople_fieldname], "any_num", 999, 999, dummy_list)

            #... interior lighting power density
            interior_lpd = validate(intLPD_fieldname, convert_WperFt2_to_WperM2(dictionary[intLPD_fieldname]), "any_num", 999, 999, dummy_list) #divide total lpd by plug lights and hardwired lights

            #... exterior lighting power
            exterior_lp = validate(extLP_fieldname, dictionary[extLP_fieldname], "any_num", 999, 999, dummy_list) #divide total lp by garage lights and exterior facade lights

            #... range type
            range_type_list = ["Electric", "Gas", "None"]
            range_type = validate(range_fieldname, dictionary[range_fieldname], "list", 999, 999, range_type_list)

            #... dryer type
            dryer_type_list = ["Electric", "Gas", "None"]
            dryer_type = validate(dryer_fieldname, dictionary[dryer_fieldname], "list", 999, 999, dryer_type_list)

            #... frig type
            frig_list = ["Yes", "None"]
            frig = validate(frig_fieldname, dictionary[frig_fieldname], "list", 999, 999, frig_list)

            #... clotheswasher type
            clotheswasher_list = ["Yes", "None"]
            clotheswasher = validate(cw_fieldname, dictionary[cw_fieldname], "list", 999, 999, clotheswasher_list)

            #... dishwasher type
            dishwasher_list = ["Yes", "None"]
            dishwasher = validate(dw_fieldname, dictionary[dw_fieldname], "list", 999, 999, dishwasher_list)

            #... miscellaneous electric power
            misc_elec = validate(miscElec_fieldname, dictionary[miscElec_fieldname], "any_num", 999, 999, dummy_list)

            if misc_elec != 0:
                #... miscellaneous electric power schedule
                misc_elec_sch = validate(miscElecShed_fieldname, dictionary[miscElecShed_fieldname], "list", 999, 999, sched_validation_list)

            #... miscellaneous gas power
            misc_gas = validate(miscGas_fieldname, convert_Btuh_to_W(dictionary[miscGas_fieldname]), "any_num", 999, 999, dummy_list)

            if misc_gas != 0:
                #... miscellaneous gas power schedule
                misc_gas_sch = validate(miscGasShed_fieldname, dictionary[miscGasShed_fieldname], "list", 999, 999, sched_validation_list)
            
        except:
            return True
        
        ## Set window construction
        win_construction = "Exterior Window"

        # Set foundation parameters based on foundation type
        main_floor_construction = foundation_and_floor_dict[foundation_and_floor_con]["main_floor_construction"]
        foundation_surface = foundation_and_floor_dict[foundation_and_floor_con]["foundation_surface"]
        int_horiz_ins_mat_name = foundation_and_floor_dict[foundation_and_floor_con]["int_horiz_ins_mat_name"]
        int_horiz_ins_depth = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con]["int_horiz_ins_depth"])
        int_horiz_ins_width = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con]["int_horiz_ins_width"])
        int_vert_ins_mat_name = foundation_and_floor_dict[foundation_and_floor_con]["int_vert_ins_mat_name"]   
        int_vert_ins_depth = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con]["int_vert_ins_depth"])
        ext_vert_ins_mat_name = foundation_and_floor_dict[foundation_and_floor_con]["ext_vert_ins_mat_name"]  
        ext_vert_ins_depth = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con]["ext_vert_ins_depth"])
        wall_ht_above_grade = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con]["wall_ht_above_grade"])
        wall_ht_below_slab = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con]["wall_ht_below_slab"])
        floor_insulation_layer = foundation_and_floor_dict[foundation_and_floor_con]["floor_insulation_layer"]
        floor_main_outside_boundary_condition = foundation_and_floor_dict[foundation_and_floor_con]["floor_main_outside_boundary_condition"]
        floor_main_outside_boundary_condition_object = foundation_and_floor_dict[foundation_and_floor_con]["floor_main_outside_boundary_condition_object"]
        foundation_zone_name = foundation_and_floor_dict[foundation_and_floor_con]["foundation_zone_name"]

        # Set geometry parameters that are needed to create geometry but not needed to be changed by user. All units in ft and converted to meters.
        origin_x = convert_ft_to_m(0) 
        origin_y = convert_ft_to_m(0)
        origin_z = convert_ft_to_m(0)
        roof_ht = convert_ft_to_m(4.5)
        number_of_stories = 1

        # Calculate intermediate geometry variables
        avg_conditioned_envelope_ht = round(total_conditioned_volume / conditioned_footprint_area, 10)
        first_flr_ht_AG = round(foundationwall_ht_AG + avg_conditioned_envelope_ht, 10)
        top_flr_ht_AG = round(first_flr_ht_AG, 10)
        roof_ht_AG = round(top_flr_ht_AG + roof_ht, 10)
        building_width = round(ratio_width_to_depth * math.sqrt(conditioned_footprint_area / ratio_width_to_depth), 10)
        building_depth = round(conditioned_footprint_area / building_width, 10)
        roof_ridge_depth = round(building_depth / 2, 10)
        wall_area_front = round(building_width * avg_conditioned_envelope_ht, 10)
        wall_area_right = round(building_depth * avg_conditioned_envelope_ht, 10)
        wall_area_left = round(building_depth * avg_conditioned_envelope_ht, 10)
        wall_area_back = round(building_width * avg_conditioned_envelope_ht, 10)
        window_area_front = round(wall_area_front * wtw_ratio_front, 10)
        window_area_right = round(wall_area_right * wtw_ratio_right, 10)
        window_area_left = round(wall_area_left * wtw_ratio_left, 10)
        window_area_back = round(wall_area_back * wtw_ratio_back, 10)
        window_centerX_front = round(building_width / 2, 10)
        window_centerX_back = round(building_width / 2, 10)
        window_centerX_sides = round(building_depth / 2, 10)
        window_aspratio_front_lenToht = round(building_width / avg_conditioned_envelope_ht, 10)
        window_aspratio_back_lenToht = round(building_width / avg_conditioned_envelope_ht, 10)
        window_aspratio_sides_lenToht = round(building_depth / avg_conditioned_envelope_ht, 10)
        window_len_front = round(window_aspratio_front_lenToht * math.sqrt(window_area_front / window_aspratio_front_lenToht), 10)
        window_ht_front = round(window_area_front / window_len_front, 10)
        window_len_right = round(window_aspratio_sides_lenToht * math.sqrt(window_area_right / window_aspratio_sides_lenToht), 10)
        window_ht_right = round(window_area_right / window_len_right, 10)
        window_len_left = round(window_aspratio_sides_lenToht * math.sqrt(window_area_left / window_aspratio_sides_lenToht), 10)
        window_ht_left = round(window_area_left / window_len_left, 10)
        window_len_back = round(window_aspratio_back_lenToht * math.sqrt(window_area_back / window_aspratio_back_lenToht), 10)
        window_ht_back = round(window_area_back / window_len_back, 10)
        window_startingX_front = round(window_centerX_front - window_len_front/2, 10)
        window_startingX_right = round(window_centerX_sides - window_len_right/2, 10)
        window_startingX_left = round(window_centerX_sides - window_len_left/2, 10)
        window_startingX_back = round(window_centerX_back - window_len_back/2, 10)
        window_startingZ_front = round((avg_conditioned_envelope_ht/2)-(window_ht_front/2), 10)
        window_startingZ_right = round((avg_conditioned_envelope_ht/2)-(window_ht_right/2), 10)
        window_startingZ_left = round((avg_conditioned_envelope_ht/2)-(window_ht_left/2), 10)
        window_startingZ_back = round((avg_conditioned_envelope_ht/2)-(window_ht_back/2), 10)

        ### --- This section imports all the necessary text from .txt files and turns them into strings. --- ### 
        # The ones with changeable variables are turned into f-strings so that their values can be properly adjusted.

        # Gains
        #... add range
        if range_type == "None":
            range_t = ""
        else:
            range_file = range_type + ".txt"
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_rangetype_dir, range_file), 'r') as f:
                range_t = f.read()
        #... add dryer
        if dryer_type == "None":
            dryer_t = ""
        else:
            dryer_file = dryer_type + ".txt"
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_dryertype_dir, dryer_file), 'r') as f:
                dryer_t = f.read()
        #... add clotheswasher
        if clotheswasher == "None":
            clotheswasher_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'ClothesWasher.txt'), 'r') as f:
                clotheswasher_t = f.read()
        #... add dishwasher
        if dishwasher == "None":
            dishwasher_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'Dishwasher.txt'), 'r') as f:
                dishwasher_t = f.read()
        #... add refrigerator
        if frig == "None":
            frig_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'Refrigerator.txt'), 'r') as f:
                frig_t = f.read()
        #... add miscellaneous electric gains
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'MiscElectric.txt'), 'r') as f:
            misc_elec_t = f"{f.read()}".format(**locals())
        #... add miscellaneous gas gains
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'MiscGas.txt'), 'r') as f:
            misc_gas_t = f"{f.read()}".format(**locals())
        #... add people
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'People.txt'), 'r') as f:
            people_t = f"{f.read()}".format(**locals())
        #... add lights
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'Lights.txt'), 'r') as f:
            lights_t = f"{f.read()}".format(**locals())

        # Constructions
        with open(os.path.join(set_dir, building_block_dir, 'Constructions.txt'), 'r') as f:
            construction_t = f"{f.read()}".format(**locals())

        # Domestic Hot Water (DHW)
        if water_heater_type == "None":
            water_heater_t = ""
            dhw_t = ""
        else:
            water_heater_file = water_heater_type + ".txt"
            with open(os.path.join(set_dir, building_block_dir, dhw_main_dir, dhw_wh_type_dir, water_heater_file), 'r') as f:
                water_heater_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, dhw_main_dir, 'OtherDHW.txt'), 'r') as f:
                dhw_t = f.read()

        # Simulation Parameters
        with open(os.path.join(set_dir, building_block_dir, 'SimulationParameters.txt'), 'r') as f:
            simparam_t = f"{f.read()}".format(**locals())

        # Performance Precision Tradeoffs
        if sim_type == "Test Run":
            with open(os.path.join(set_dir, building_block_dir, performanceprecision_dir, 'HighSpeed.txt'), 'r') as f:
                performanceprecision_t = f"{f.read()}".format(**locals())
        else:
            with open(os.path.join(set_dir, building_block_dir, performanceprecision_dir, 'Normal.txt'), 'r') as f:
                performanceprecision_t = f"{f.read()}".format(**locals())

        # Windows
        #... set U-value and SHGC
        with open(os.path.join(set_dir, building_block_dir, window_main_dir, 'SimpleGlazingSystem.txt'), 'r') as f:
            glazing_t = f"{f.read()}".format(**locals())
        #... set window construction (i.e. with or without blinds)
        window_con_file = window_shades + ".txt"
        with open(os.path.join(set_dir, building_block_dir, window_main_dir, window_blinds_dir, window_con_file), 'r') as f:
            win_construction_t = f.read()

        # Location & Climate
        #... also includes design day 
        location_design_day_file = location_pull + ".txt"
        with open(os.path.join(set_dir, building_block_dir, location_and_climate_dir, location_design_day_file), 'r') as f: # our location & climate dictionary in action
            locations_t = f.read()

        # Materials
        #... insert user-entered above-ground wall insulation
        wall_ins_file = above_ground_wall_con + ".txt"
        with open(os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, wall_ins_file), 'r') as f:
            above_ground_wall_t = f.read()
        #... insert user-entered ceiling/attic insulation
        attic_ins_file = ceiling_and_roof_con + ".txt"
        with open(os.path.join(set_dir, building_block_dir, materials_main_dir, materials_attic_ins_dir, attic_ins_file), 'r') as f:
            ceiling_attic_t = f.read()
        #...insert all other materials
        with open(os.path.join(set_dir, building_block_dir, materials_main_dir, 'OtherMaterials.txt'), 'r') as f:
            mat_t = f.read()

        # Performance Curves
        with open(os.path.join(set_dir, building_block_dir, 'PerformanceCurves.txt'), 'r') as f:
            perf_t = f.read()

        # Schedules
        htg_sch_num = sched_list.index(htg_stpt_sch) + 1
        clg_sch_num = sched_list.index(clg_stpt_sch) + 1
        dhw_sch_num = sched_list.index(dhw_stpt_sch) + 1

        #... misc electric gains
        if misc_elec != 0 and misc_elec_sch != str(PNNL_default[0]):
            try:
                misc_elec_sch_num = sched_list.index(misc_elec_sch) + 1
                with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_elec_gains_dir, 'MiscElectricGainsCustom.txt'), 'r') as f:
                    misc_elec_sched_t = f"{f.read()}".format(**locals())
            except:
                print("\n*** ERROR: REEDR could not find schedule for miscellaneous electric gains. Please ensure this input is valid. \n")
                return True
        else:
            with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_elec_gains_dir, 'MiscElecPNNLdefault.txt'), 'r') as f:
                    misc_elec_sched_t = f"{f.read()}".format(**locals())
        #... misc gas gains
        if misc_gas != 0 and misc_gas_sch != str(PNNL_default[0]):
            try:
                misc_gas_sch_num = sched_list.index(misc_gas_sch) + 1
                with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_gas_gains_dir, 'MiscGasGainsCustom.txt'), 'r') as f:
                    misc_gas_sched_t = f"{f.read()}".format(**locals())
            except:
                print("\n*** ERROR: REEDR could not find schedule for miscellaneous gas gains. Please ensure this input is valid. \n")
                return True
        else:
            with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_gas_gains_dir, 'MiscGasPNNLdefault.txt'), 'r') as f:
                    misc_gas_sched_t = f"{f.read()}".format(**locals())

        #... most other schedules
        with open(os.path.join(set_dir, building_block_dir, schedule_dir, 'Schedules.txt'), 'r') as f:
            sched_t = f"{f.read()}".format(**locals())

        # Add Kiva foundation inputs
        with open(os.path.join(set_dir, building_block_dir, 'Foundation.txt'), 'r') as f:
            foundation_type_t = f"{f.read()}".format(**locals())

        ### --- Adding building geometry --- ###
        #...insert geometry rules
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, 'GlobalGeometryRules.txt'), 'r') as f:
            geom_rules_t = f.read()
        #...insert internal mass
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, 'InternalMass.txt'), 'r') as f:
            internal_mass_t = f.read()
        #...insert aspects of building geometry common to all buildings (e.g. main walls, ceiling, roof)
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, 'MainGeometry.txt'), 'r') as f:
            geom_main_envelope_t = f"{f.read()}".format(**locals())
        #...insert window geometry
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_window_dir, 'MainWindows.txt'), 'r') as f:
            geom_main_windows_t = f"{f.read()}".format(**locals())
        #...insert living zone geometry in all buildings
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, 'living.txt'), 'r') as f:
            living_zone_t = f.read()
        #...insert attic zone geometry in all buildings
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, 'attic.txt'), 'r') as f:
            attic_zone_t = f.read()
        #...if foundation type is slab, add necessary slab geometry and set non-slab geometry files as empty strings
        if foundation_type == "Slab":
            geom_nonslab_adder_t = ""
            unheatedbsmt_zone_t = ""
            crawlspace_zone_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, 'NonHeatedBsmtGeometryAdder.txt'), 'r') as f:
                geom_nonhtdbsmt_adder_t = f"{f.read()}".format(**locals())
        #...if foundation type is heated basement, add necessary heated basement geometry and set non-htd basement geometry files as empty strings
        elif foundation_type == "Heated Basement":
            unheatedbsmt_zone_t = ""
            crawlspace_zone_t = ""
            geom_nonhtdbsmt_adder_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, 'NonSlabGeometryAdder.txt'), 'r') as f:
                geom_nonslab_adder_t = f"{f.read()}".format(**locals())
        #...if foundation type is a vented crawl, add necessary crawl geometry and set non-crawl geometry files as empty strings
        elif foundation_type == "Vented Crawlspace":
            unheatedbsmt_zone_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, 'crawlspace.txt'), 'r') as f:
                crawlspace_zone_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, 'NonSlabGeometryAdder.txt'), 'r') as f:
                geom_nonslab_adder_t = f"{f.read()}".format(**locals())
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, 'NonHeatedBsmtGeometryAdder.txt'), 'r') as f:
                geom_nonhtdbsmt_adder_t = f"{f.read()}".format(**locals()) 
        else: # foundation type is unheated basement
            crawlspace_zone_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, 'unheatedbsmt.txt'), 'r') as f:
                unheatedbsmt_zone_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, 'NonSlabGeometryAdder.txt'), 'r') as f:
                geom_nonslab_adder_t = f"{f.read()}".format(**locals())
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, 'NonHeatedBsmtGeometryAdder.txt'), 'r') as f:
                geom_nonhtdbsmt_adder_t = f"{f.read()}".format(**locals())
        
        DesignSpecificationOutdoorAirObjectName = ""

        # Get HVAC characteristics from HVAC dictionary based on user selection in Excel input sheet.
        ZoneEquipment1ObjectType = hvac_dict[hvac_type][1]
        ZoneEquipment1Name = hvac_dict[hvac_type][2]
        ZoneEquipment1CoolingSequence = hvac_dict[hvac_type][3]
        ZoneEquipment1HeatingSequence = hvac_dict[hvac_type][4]
        ZoneEquipment2ObjectType = hvac_dict[hvac_type][5]
        ZoneEquipment2Name = hvac_dict[hvac_type][6]
        ZoneEquipment2CoolingSequence = hvac_dict[hvac_type][7]
        ZoneEquipment2HeatingSequence = hvac_dict[hvac_type][8]
        ZoneAirInletNodeName = hvac_dict[hvac_type][9]
        ZoneAirExhaustNodeName = hvac_dict[hvac_type][10]
        ZoneReturnAirNodeName = hvac_dict[hvac_type][11]
        AirLoopHVAC_HeatingCoil_ObjectType = hvac_dict[hvac_type][17]
        AirLoopHVAC_HeatingCoil_Name = hvac_dict[hvac_type][18]
        AirLoopHVAC_CoolingCoil_ObjectType = hvac_dict[hvac_type][19]
        AirLoopHVAC_CoolingCoil_Name = hvac_dict[hvac_type][20]
        AirLoopHVAC_Unitary_ObjectType = hvac_dict[hvac_type][21]
        AirLoopHVAC_Unitary_ObjectName = hvac_dict[hvac_type][22]
        fan_name = hvac_dict[hvac_type][23]
        heating_speeds = hvac_dict[hvac_type][24]
        cooling_speeds = hvac_dict[hvac_type][25]
        fan_CFMperTon_max = hvac_dict[hvac_type][26]
        fan_CFMmult_spd_1 = hvac_dict[hvac_type][27]
        fan_CFMmult_spd_2 = hvac_dict[hvac_type][28]
        fan_CFMmult_spd_3 = hvac_dict[hvac_type][29]
        fan_CFMmult_spd_4 = hvac_dict[hvac_type][30]
        capacitymult_spd_1 = hvac_dict[hvac_type][31]
        capacitymult_spd_2 = hvac_dict[hvac_type][32]
        capacitymult_spd_3 = hvac_dict[hvac_type][33]
        capacitymult_spd_4 = hvac_dict[hvac_type][34]

        # Assume effectively no integrated supplemental backup heat for a DHP
        if AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed" and hvac_dict[hvac_type][0] == "Zonal":
            hp_max_resistance_temp = convert_degF_to_degC(68)
            hp_min_compressor_temp = convert_degF_to_degC(-20)

        # Set capacity to use for sizing fans. If heating only, use heating capacity. If heating and cooling, use average capacity.
        if hvac_dict[hvac_type][22] == "SS Heat Pump" or hvac_dict[hvac_type][22] == "DS Heat Pump" or hvac_dict[hvac_type][22] == "MS Heat Pump" \
            or hvac_dict[hvac_type][15] != "NA":

            sizing_capacity = convert_W_to_ton((primary_heating_capacity + primary_cooling_capacity)/2)
        else:
            sizing_capacity = convert_W_to_ton(primary_heating_capacity)

        # Set max fan speed using the proper user inputted total HVAC capacity
        fan_m3PerSec_max = convert_CFM_to_m3PerSec(fan_CFMperTon_max * sizing_capacity)
        
        # Set fan speeds and capacities using characteristics from HVAC dictionary and user selected HVAC type.
        # Variable speed equipment is modeled using four speeds.
        fan_m3PerSec_spd_1 = fan_CFMmult_spd_1 * fan_m3PerSec_max
        fan_m3PerSec_spd_2 = fan_CFMmult_spd_2 * fan_m3PerSec_max
        fan_m3PerSec_spd_3 = fan_CFMmult_spd_3 * fan_m3PerSec_max
        fan_m3PerSec_spd_4 = fan_CFMmult_spd_4 * fan_m3PerSec_max
        htg_capacity_spd_1 = capacitymult_spd_1 * primary_heating_capacity
        htg_capacity_spd_2 = capacitymult_spd_2 * primary_heating_capacity
        htg_capacity_spd_3 = capacitymult_spd_3 * primary_heating_capacity
        htg_capacity_spd_4 = capacitymult_spd_4 * primary_heating_capacity
        clg_capacity_spd_1 = capacitymult_spd_1 * primary_cooling_capacity
        clg_capacity_spd_2 = capacitymult_spd_2 * primary_cooling_capacity
        clg_capacity_spd_3 = capacitymult_spd_3 * primary_cooling_capacity
        clg_capacity_spd_4 = capacitymult_spd_4 * primary_cooling_capacity

        fan_max_flow_allowed = 1 * fan_m3PerSec_max

        # Add baseboard capacity if defined
        if baseboard_heat_capacity != 0:
            ZoneEquipment2ObjectType = "ZoneHVAC:Baseboard:Convective:Electric"
            ZoneEquipment2Name = "BaseboardElectric"
            ZoneEquipment2CoolingSequence = "2"
            ZoneEquipment2HeatingSequence = "2"
            with open(os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'BaseboardHeat.txt'), 'r') as f:
                baseboard_t = f"{f.read()}".format(**locals())
        else:
            baseboard_t = ""
        
        # This is currently not used, but may be useful when HPWHs or ERVs are eventually added.
        ZoneEquipment3ObjectType = "!-"
        ZoneEquipment3Name = "!-"
        ZoneEquipment3CoolingSequence = "!-"
        ZoneEquipment3HeatingSequence = "!-"
        
        # Establish supplemental (backup) heat source for ASHPs...
        if AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirtoAir" and hp_supp_heat_type == "Gas":
            AirLoopHVAC_SuppHeatingCoil_ObjectType = "Coil:Heating:Fuel"
            AirLoopHVAC_SuppHeatingCoil_Name = "Heating_Fuel_Backup"
            AFN_main_heating_coil_outlet_node = "SuppHeatingInletNode"
            with open(os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Fuel_Backup.txt'), 'r') as f:
                supp_heating_coil_t = f"{f.read()}".format(**locals())
        elif AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed" and hp_supp_heat_type == "Gas":    
            AirLoopHVAC_SuppHeatingCoil_ObjectType = "Coil:Heating:Fuel"
            AirLoopHVAC_SuppHeatingCoil_Name = "Heating_Fuel_Backup"
            AFN_main_heating_coil_outlet_node = "SuppHeatingInletNode"
            with open(os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Fuel_Backup.txt'), 'r') as f:
                supp_heating_coil_t = f"{f.read()}".format(**locals())
        elif AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirtoAir" or AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed":
            AirLoopHVAC_SuppHeatingCoil_ObjectType = "Coil:Heating:Electric"
            AirLoopHVAC_SuppHeatingCoil_Name = "Heating_Resistance_Backup"
            AFN_main_heating_coil_outlet_node = "SuppHeatingInletNode"
            with open(os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Backup.txt'), 'r') as f:
                supp_heating_coil_t = f"{f.read()}".format(**locals())
        else:
            supp_heating_coil_t = ""
            AFN_main_heating_coil_outlet_node = "HeatingOutletNode"
        
        # Establish HVAC nodes depending on whether HVAC system has a cooling coil or not...
        if AirLoopHVAC_CoolingCoil_ObjectType == "NA":
            airloop_main_fan_coil_outlet_node = "Heating Coil Air Inlet Node"
            AFN_main_fan_coil_outlet_node = "HeatingInletNode"
            AFN_nodes_coolingcoiladder_t = ""
            AFN_linkage_coolingcoiladder_t = ""
        else:
            airloop_main_fan_coil_outlet_node = "Cooling Coil Air Inlet Node"
            AFN_main_fan_coil_outlet_node = "FanOutletNode"
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_node_dir, 'AFN_CoolingCoilNodeAdder.txt'), 'r') as f:
                AFN_nodes_coolingcoiladder_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_linkage_dir, 'AFN_CoolingCoilLinkageAdder.txt'), 'r') as f:
                AFN_linkage_coolingcoiladder_t = f"{f.read()}".format(**locals())

        # Estimate effective leakage areas (ELAs), used to represent building infiltration, in AFN model
        infiltrationInACH50 = infiltration
        total_envelope_height = dictionary[volume_fieldname] / dictionary[footprint_fieldname]
        
        adjust = []
        adjust = estimateInfiltrationAdjustment(foundation_type, infiltrationInACH50, dictionary[footprint_fieldname], total_envelope_height)
        living_adjust = adjust[0]
        attic_adjust = adjust[1]
        crawl_adjust = adjust[2]
        
        ELA_wall_frontback = living_adjust * wall_area_front * 0.00010812648958345
        ELA_wall_leftright = living_adjust * wall_area_left * 0.00010812648958345
        ELA_ceiling = living_adjust * conditioned_footprint_area * 0.00010812648958345
        ELA_floor = living_adjust * conditioned_footprint_area * 0.0000000905634180403216
        
        roof_hypotenuse = math.sqrt(roof_ht**2 + (building_depth/2)**2)
        attic_wall_area = 2*(0.5*building_depth*roof_ht) + 2*(roof_hypotenuse*building_width)
        ELA_attic = attic_adjust * attic_wall_area * 0.00010812648958345

        crawl_wall_area = 2*(abs(foundationwall_ht_AG) + abs(foundationwall_ht_BG))*building_depth + 2*(abs(foundationwall_ht_AG) + abs(foundationwall_ht_BG))*building_width
        ELA_crawl = crawl_adjust * crawl_wall_area * 0.00010812648958345
        
        
        ### --- Add Air Flow Network (AFN) and airloop. Currently all HVAC systems are modeled with ducts. "Ductless" systems are modeled with "perfect" ducts. --- ### 
        AFN_control = "MultizoneWithDistribution"
        # The following text files are added for all building models
        #...insert system sizing block
        with open(os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, 'SystemSizing.txt'), 'r') as f:
            system_sizing_t = f.read()
        #...insert air loop
        with open(os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, 'AirLoop.txt'), 'r') as f:
            airloop_t = f"{f.read()}".format(**locals())
        #...insert AFN nodes common to all buildings
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_node_dir, 'AFN_MainNodes.txt'), 'r') as f:
            AFN_nodes_main_t = f.read()
        #...insert AFN linkages common to all buildings
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_linkage_dir, 'AFN_MainLinkage.txt'), 'r') as f:
            AFN_linkage_main_t = f"{f.read()}".format(**locals()) 
        #...insert AFN simulation control
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, 'AFN_SimulationControl.txt'), 'r') as f:
            AFN_sim_control_t = f"{f.read()}".format(**locals())
        #...insert AFN zones common to all buildings (i.e., main, attic)
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_zone_dir, 'AFN_MainZones.txt'), 'r') as f:
            AFN_main_zones_t = f.read()
        #...insert AFN surface leakage
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_leakage_dir, 'AFN_MainLeakage.txt'), 'r') as f:
            AFN_main_leakage_t = f"{f.read()}".format(**locals())
        #...insert AFN surfaces common to all geometries
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_surface_dir, 'AFN_MainSurfaces.txt'), 'r') as f:
            AFN_main_surfaces_t = f.read()
        
        # Insert AFN "adders" for certain foundation types
        if foundation_dict[foundation_key][0] == "Slab" or foundation_dict[foundation_key][0] == "Heated Basement":
            AFN_crawl_zone_t = ""
            AFN_unheatedbsmt_zone_t = ""
            AFN_crawl_unheatedbsmt_leakage_adder_t = ""
            AFN_crawl_unheatedbsmt_surface_adder_t = ""
        elif foundation_dict[foundation_key][0] == "Vented Crawlspace":
            AFN_unheatedbsmt_zone_t = ""
            #...add a crawlspace AFN zone
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_zone_dir, 'AFN_CrawlZoneAdder.txt'), 'r') as f:
                AFN_crawl_zone_t = f.read()
            #...add surface leakage for crawlspace walls
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_leakage_dir, 'AFN_CrawlUnheatedBsmtLeakageAdder.txt'), 'r') as f:
                AFN_crawl_unheatedbsmt_leakage_adder_t = f"{f.read()}".format(**locals())
            #...add crawlspace surfaces
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_surface_dir, 'AFN_CrawlUnheatedBsmtSurfaceAdder.txt'), 'r') as f:
                AFN_crawl_unheatedbsmt_surface_adder_t = f.read()

        else: # foundation type is unheated basement
            AFN_crawl_zone_t = ""
            #...add an unheated basement zone
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_zone_dir, 'AFN_UnheatedbsmtZoneAdder.txt'), 'r') as f:
                AFN_unheatedbsmt_zone_t = f.read()
            #...add surface leakage for basement walls
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_leakage_dir, 'AFN_CrawlUnheatedBsmtLeakageAdder.txt'), 'r') as f:
                AFN_crawl_unheatedbsmt_leakage_adder_t = f"{f.read()}".format(**locals())
            #...add AFN surfaces for basement walls
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_surface_dir, 'AFN_CrawlUnheatedBsmtSurfaceAdder.txt'), 'r') as f:
                AFN_crawl_unheatedbsmt_surface_adder_t = f.read()

        if hvac_dict[hvac_type][0] == "Central":
            maintrunk_duct_length = 2 # units are meters
            zonesupply_duct_length = 15
            zonereturn_duct_length = 8
            mainreturn_duct_length = 1

            supply_duct_Ufactor = supplyUvalue # units are W/m2-K
            return_duct_Ufactor = returnUvalue
        elif hvac_dict[hvac_type][0] == "Zonal":
            maintrunk_duct_length = 0.0001
            zonesupply_duct_length = 0.0001
            zonereturn_duct_length = 0.0001
            mainreturn_duct_length = 0.0001

            supply_duct_Ufactor = supplyUvalue
            return_duct_Ufactor = returnUvalue
        else:
            print("\n*** ERROR: Problem assigning duct system parameters. Please ensure you have selected a valid HVAC system type. \n")
            return True

        # Add AFN ducts to all models (note: zonal/ductless systems assume "perfect" ducts)
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, 'AFN_Ducts.txt'), 'r') as f:
            AFN_ducts_t = f"{f.read()}".format(**locals())
        #  Add a theromstat (T-stat)
        with open(os.path.join(set_dir, building_block_dir, hvac_tstat_dir, 'Thermostat.txt'), 'r') as f:
            thermostat_t = f"{f.read()}".format(**locals())
        # Add zone sizing
        with open(os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, 'ZoneSizing.txt'), 'r') as f:
            zone_sizing_t = f"{f.read()}".format(**locals())
        # Add zone equipment list
        with open(os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, 'EquipListAndConnections.txt'), 'r') as f:
            zone_equip_list_t = f"{f.read()}".format(**locals())
        # Add HVAC equipment text file 1, which is typically the unitary HVAC text file
        with open(hvac_dict[hvac_type][12], 'r') as f:
            HVAC_equip_1_t = f"{f.read()}".format(**locals())
        # Add HVAC equipment text file 2, which is typically the air distribution unit
        if hvac_dict[hvac_type][13] == "NA":
            HVAC_equip_2_t = ""
        else:
            with open(hvac_dict[hvac_type][13], 'r') as f:
                HVAC_equip_2_t = f"{f.read()}".format(**locals())
        # Add heating coil text file
        if hvac_dict[hvac_type][14] == "NA":
            heating_coil_t = ""
        else:
            with open(hvac_dict[hvac_type][14], 'r') as f:
                heating_coil_t = f"{f.read()}".format(**locals())
        # Add cooling coil text file
        if hvac_dict[hvac_type][15] == "NA":    
            cooling_coil_t = ""
        else:
            with open(hvac_dict[hvac_type][15], 'r') as f:
                cooling_coil_t = f"{f.read()}".format(**locals())
        # Add fan text file
        if hvac_dict[hvac_type][16] == "NA":    
            fan_t = ""
        else:
            with open(hvac_dict[hvac_type][16], 'r') as f:
                fan_t = f"{f.read()}".format(**locals())

        # Output text files
        #... add user requested output file
        user_output_file = output_lookup + ".txt"
        with open(os.path.join(set_dir, building_block_dir, output_dir, user_output_file), 'r') as f:
            user_output_t = f"{f.read()}".format(**locals())  
        #... add general output
        with open(os.path.join(set_dir, building_block_dir, output_dir, 'OtherOutput.txt'), 'r') as f:
            output_t = f.read()

        # Output file control
        #... add general output
        with open(os.path.join(set_dir, building_block_dir, 'OutputControl_Files.txt'), 'r') as f:
            outputcontrol_t = f.read()
        
        ### --- Assemble Final IDF Text File --- ###
        # Nests all the .txt files, now morphed into strings, in a listin the order they are to be written to the new idfs.
        # Nesting them this way allows us to easily write the full idf file, because we can simply iterate over the list
        master_tl = [
            simparam_t, performanceprecision_t, locations_t, sched_t, misc_elec_sched_t, misc_gas_sched_t, \
            mat_t, above_ground_wall_t, ceiling_attic_t, glazing_t, win_construction_t, construction_t, \
            range_t, dryer_t, clotheswasher_t, dishwasher_t, frig_t, misc_elec_t, misc_gas_t, people_t, lights_t, \
            foundation_type_t, geom_rules_t, internal_mass_t, geom_main_envelope_t, geom_nonslab_adder_t, geom_main_windows_t, \
            living_zone_t, attic_zone_t, unheatedbsmt_zone_t, crawlspace_zone_t, geom_nonhtdbsmt_adder_t, \
            AFN_sim_control_t, AFN_main_zones_t, AFN_main_leakage_t, AFN_main_surfaces_t, AFN_nodes_main_t, AFN_linkage_main_t, \
            AFN_crawl_zone_t, AFN_unheatedbsmt_zone_t, AFN_crawl_unheatedbsmt_leakage_adder_t, AFN_crawl_unheatedbsmt_surface_adder_t, \
            AFN_ducts_t, system_sizing_t, airloop_t, AFN_linkage_coolingcoiladder_t, AFN_nodes_coolingcoiladder_t, \
            zone_equip_list_t, HVAC_equip_1_t, HVAC_equip_2_t, heating_coil_t, supp_heating_coil_t, cooling_coil_t, fan_t, \
            baseboard_t, thermostat_t, zone_sizing_t, water_heater_t, dhw_t, perf_t, output_t, user_output_t, outputcontrol_t
            ]

        #the idf writing actually begins here
        fullidf = "" # the full idf begins as a blank string
        # every stringified .txt file gets added to the idf
        for bigstring in master_tl:
            fullidf += bigstring
        # then it gets named after the harvested runlabel
        filename = f"{run_label}.idf"
        # the path gets set for the new idf
        path = os.path.join(get_data_dict["master_directory"], run_label, filename)
        # and voila! the idf gets written for the present runlabel, and the loop begins again
        with open(path, 'w') as newfile:
                newfile.write(fullidf)

        i = i + 1

    print("...model build complete.")
    print()

    return False
    ##########################################################################################################################
