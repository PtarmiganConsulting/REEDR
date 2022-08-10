## module imports...
import pandas as pd # to import xcel, some initial data manipulation
import os # for making paths and directories and removing files
import shutil # for removing full directories
from pprint import pprint # for debugging

## Note: when exe'ing, must add "Python." in front of each file name
from unitconversions import convert_WperFt2_to_WperM2, convert_degF_to_degC, convert_IP_Uvalue_to_SI_Uvalue

def genmodels(gui_params, get_data_dict):

    # Sets the directory. When calling from __main__, needs to be set to "parent". When calling from entry exe script, needs to be set to "cwd".
    set_dir = get_data_dict["parent"]

    #Set directory and file names as variables, so they can be established only once here, and flow throughout.
    building_block_dir = "Building Blocks"
    schedule_dir = "Schedules"
    schedule_file = "Schedules.csv"
    location_and_climate_dir = "LocationAndClimate"
    materials_main_dir = "Materials"
    materials_wall_ins_dir = "AGWallInsulation"
    materials_attic_ins_dir = "AtticInsulation"
    materials_floor_ins_dir = "FloorInsulation"
    materials_slab_ins_dir = "SlabInsulation"
    materials_basement_ins_dir = "BasementInsulation"
    dhw_main_dir = "DHW"
    dhw_wh_type_dir = "WaterHeaterType"
    gains_main_dir = "Gains"
    gains_dryertype_dir = "DryerType"
    gains_rangetype_dir = "RangeType"
    hvac_main_dir = "HVAC"
    hvac_type_dir = "HVACType"
    hvac_returnduct_dir = "ReturnDuctLocation"
    output_dir = "Output"
    window_main_dir = "Windows"
    window_blinds_dir = "Blinds"
    zones_surfaces_main_dir = "ZonesAndSurfaces"
    zones_surfaces_foundation_dir = "FoundationType"

    # it looks like these are unused, but actually they need to be here for the localization
    begin_mo = get_data_dict["begin_mo"]
    begin_day = get_data_dict["begin_day"]
    end_mo = get_data_dict["end_mo"]
    end_day = get_data_dict["end_day"]
    sim_type = get_data_dict["sim_type"]
    output_gran = gui_params["output_gran"]
    output_enduses = gui_params["output_enduses"]


    # Update simulation status box in REEDR.xlsm...
    print("Starting model build...")

    # # Create Schedules.csv file and store headers in a list
    # read_file = pd.read_excel (REEDR_wb, sheet_name="Schedules_8760")
    # if os.path.exists(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)) == True:
    #     try:
    #         os.remove(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file))
    #         read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)), index = None, header=True)
    #         runlog.write("Schedules.csv successfully overwritten at " + os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file) + ". \n" + "... \n")
    #     except Exception as e:
    #         runlog.write("!!! Schedules.csv could not be made at " + os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file) + ". \n")
    #         runlog.write("!!! REEDR experienced the following error: " + str(e) + ". \n")
    # else:
    #     read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)), index = None, header=True)
    #     runlog.write(schedule_file + " successfully created at " + os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file) + ". \n" + "... \n")
    #
    # sched_list = (list(read_file.columns))

    # gathers the subdirectory names for each runlabel by skimming them from the excel file
    # Note: df is a dataframe that contains user inputs from the "Model_Inputs" tab in REEDR.xlsm
    directory_names = []
    for i in range(len(get_data_dict["df"])):
        directory_names.append(get_data_dict["df"].loc[i][0])

    # Creates subdirectories for each model under the main project directory.
    get_data_dict["runlog"].write("Starting to build subdirectories under " + os.path.join(get_data_dict["master_directory"]) + ". \n")

    for name in directory_names:
        path = os.path.join(get_data_dict["master_directory"], name)
        try:
            os.mkdir(path)
            get_data_dict["runlog"].write("... subdirectory successfully created at " + path + ". \n")
        except Exception as e:
            get_data_dict["runlog"].write("!!! subdirectory could not be created at " + path + ". \n")
            get_data_dict["runlog"].write("!!! REEDR experienced the following error: " + str(e) + ". \n")
            get_data_dict["runlog"].close()
            print(e)

    get_data_dict["runlog"].write("... \n")

    ## IDF WRITER LOOP BEGINS HERE
    ## the loop covers every dictionary (effectively a runlabel row) in the big dictionary list we made,
    ## each time the loop comes to a new dictionary/runlabel row, it updates the changable variables before doing anything else
    ## that's how we make sure the changeable values get properly filled into each created idf
    get_data_dict["runlog"].write("Starting to build EnergyPlus .idf model files... \n")

    # Set output end uses and granularity based on user input...
    if gui_params["output_gran"] == "Annual":
        output_type = "Energy"
    else:
        output_type = "Demand"
    output_lookup = output_type + "_" + gui_params["output_enduses"]

    i = 1
    for dictionary in get_data_dict["master_dict_list"]:

        # Update simulation status box in REEDR.xlsm...
        status = "...building model " + str(i) + " of " + str(len(get_data_dict["df"])) + "..."
        print(status)
        #sht1['D16'] = status

        run_label = dictionary["Run_Label"]
        timestep = dictionary["Timesteps_Per_Hr"]
        location_pull = dictionary["Weather_File"] # I should name this something better.
        people = dictionary["Number_Of_People"]
        bldg_orient = dictionary["Bldg_Orient"]
        above_ground_wall_con = dictionary["Above_Ground_Wall_Construction"]
        ceiling_and_roof_con = dictionary["Ceiling_And_Roof_Construction"]
        foundation_and_floor_con = dictionary["Foundation_And_Floor_Construction"]
        windowu_val = convert_IP_Uvalue_to_SI_Uvalue(dictionary["Window_U-Value"])
        window_shgc = dictionary["Window_SHGC"]
        window_shades = dictionary["Window_Shades"]
        window_overhangs = dictionary["Window_Overhangs"]
        hvac_type = dictionary["HVAC_Type"]
        htg_stpt_sch = dictionary["Htg_StPt_Sch"]
        clg_stpt_sch = dictionary["Clg_StPt_Sch"]
        supply_leak = dictionary["Supply_Duct_Leakage"]
        return_leak = dictionary["Return_Duct_Leakage"]
        hp_max_resistance_temp = convert_degF_to_degC(dictionary["HP_Max_Resistance_Temp"])
        hp_min_compressor_temp = convert_degF_to_degC(dictionary["HP_Min_Compressor_Temp"])
        water_heater_type = dictionary["Water_Heater_Type"]
        dhw_stpt_sch = dictionary["DHW_StPt_Sch"]
        interior_lpd = convert_WperFt2_to_WperM2(dictionary["Interior_LPD"])/2 #divide total lpd by plug lights and hardwired lights
        exterior_lp = dictionary["Exterior_W"]/2 #divide total lp by garage lights and exterior facade lights
        range_type = dictionary["Range"]
        dryer_type = dictionary["Dryer"]
        frig = dictionary["Refrigerator"]
        clotheswasher = dictionary["ClothesWasher"]
        dishwasher = dictionary["Dishwasher"]
        misc_elec = dictionary["MiscElectric_W"]
        misc_gas = dictionary["MiscGas_W"]

        ## Set window construction
        win_construction = "Exterior Window"

        ## locations & climate dictionary
        ## this determines what location and climate file will later be pulled to the idf
        location_dict = {"USA_OR_Portland.Intl.AP.726980_TMY3": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_OR_Portland.Intl.AP.726980_TMY3.txt'),
        "USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3.txt'),
        "USA_WA_Spokane.Intl.AP.727850_TMY3": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_WA_Spokane.Intl.AP.727850_TMY3.txt'),
        "USA_ID_Boise.AP-Gowen.Field.ANGB.726810_TMY3": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_ID_Boise.AP-Gowen.Field.ANGB.726810_TMY3.txt'),
        "USA_MT_Kalispell-Glacier.Park.Intl.AP.727790_TMY3": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_MT_Kalispell-Glacier.Park.Intl.AP.727790_TMY3.txt'),
        "USA_ID_Coeur.dAlene.AP-Boyington.Field.727834_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_ID_Coeur.dAlene.AP-Boyington.Field.727834_TMYx.2004-2018.txt'),
        "USA_ID_Craters.of.the.Moon.Natl.Monument.725790_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_ID_Craters.of.the.Moon.Natl.Monument.725790_TMYx.2004-2018.txt'),
        "USA_ID_Jerome.County.AP.726816_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_ID_Jerome.County.AP.726816_TMYx.2004-2018.txt'),
        "USA_MT_Baker.Muni.AP.726777_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_MT_Baker.Muni.AP.726777_TMYx.2004-2018.txt'),
        "USA_MT_Kalispell-Glacier.Park.Intl.AP.727790_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_MT_Kalispell-Glacier.Park.Intl.AP.727790_TMYx.2004-2018.txt'),
        "USA_OR_Baker.City.Muni.AP.726886_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_OR_Baker.City.Muni.AP.726886_TMYx.2004-2018.txt'),
        "USA_OR_Salem.Muni.AP-McNary.Field.726940_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_OR_Salem.Muni.AP-McNary.Field.726940_TMYx.2004-2018.txt'),
        "USA_WA_Pasco-Tri.Cities.AP.727845_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_WA_Pasco-Tri.Cities.AP.727845_TMYx.2004-2018.txt'),
        "USA_WA_Tacoma-JB.Lewis-McChord-Gray.AAF.742070_TMYx.2004-2018": os.path.join(set_dir, building_block_dir, location_and_climate_dir, 'USA_WA_Tacoma-JB.Lewis-McChord-Gray.AAF.742070_TMYx.2004-2018.txt'),
        }

        ## above ground wall construction dictionary
        ## this determines what above ground wall insulation layer will later be pulled to the idf
        above_ground_wall_dict = {"Wood-Framed - 2x4 - 16 in OC - R-0 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x4 - 16 in OC - R-0 Cavity.txt'),
        "Wood-Framed - 2x4 - 16 in OC - R-11 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x4 - 16 in OC - R-11 Cavity.txt'),
        "Wood-Framed - 2x4 - 16 in OC - R-13 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x4 - 16 in OC - R-13 Cavity.txt'),
        "Wood-Framed - 2x4 - 16 in OC - R-15 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x4 - 16 in OC - R-15 Cavity.txt'),
        "Wood-Framed - 2x6 - 16 in OC - R-0 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 16 in OC - R-0 Cavity.txt'),
        "Wood-Framed - 2x6 - 16 in OC - R-19 Cavity - R-10 Header": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 16 in OC - R-19 Cavity - R-10 Header.txt'),
        "Wood-Framed - 2x6 - 16 in OC - R-19 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 16 in OC - R-19 Cavity.txt'),
        "Wood-Framed - 2x6 - 16 in OC - R-21 Cavity - R-10 Header": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 16 in OC - R-21 Cavity - R-10 Header.txt'),
        "Wood-Framed - 2x6 - 16 in OC - R-21 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 16 in OC - R-21 Cavity.txt'),
        "Wood-Framed - 2x6 - 24 in OC - R-0 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 24 in OC - R-0 Cavity.txt'),
        "Wood-Framed - 2x6 - 24 in OC - R-19 Cavity - R-10 Header": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 24 in OC - R-19 Cavity - R-10 Header.txt'),
        "Wood-Framed - 2x6 - 24 in OC - R-19 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 24 in OC - R-19 Cavity.txt'),
        "Wood-Framed - 2x6 - 24 in OC - R-21 Cavity - R-10 Header": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 24 in OC - R-21 Cavity - R-10 Header.txt'),
        "Wood-Framed - 2x6 - 24 in OC - R-21 Cavity": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_wall_ins_dir, 'Wood-Framed - 2x6 - 24 in OC - R-21 Cavity.txt'),
        }

        ## ceiling/attic construction dictionary
        ## this determines what ceiling/attic insulation layer will later be pulled to the idf
        ceiling_and_roof_dict = {"Attic - R0 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_attic_ins_dir, 'Attic - R0 Cavity Insulation.txt'),
        "Attic - R30 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_attic_ins_dir, 'Attic - R30 Cavity Insulation.txt'),
        "Attic - R38 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_attic_ins_dir, 'Attic - R38 Cavity Insulation.txt'),
        "Attic - R49 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_attic_ins_dir, 'Attic - R49 Cavity Insulation.txt'),
        "Attic - R60 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_attic_ins_dir, 'Attic - R60 Cavity Insulation.txt'),
        }

        ## floor and foundation construction dictionary
        ## this determines what ceiling/attic insulation layer will later be pulled to the idf
        foundation_and_floor_dict = {"Vented Crawlspace - R0 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_floor_ins_dir, 'Vented Crawlspace - R0 Cavity Insulation.txt'),
        "Vented Crawlspace - R13 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_floor_ins_dir, 'Vented Crawlspace - R13 Cavity Insulation.txt'),
        "Vented Crawlspace - R19 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_floor_ins_dir, 'Vented Crawlspace - R19 Cavity Insulation.txt'),
        "Vented Crawlspace - R30 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_floor_ins_dir, 'Vented Crawlspace - R30 Cavity Insulation.txt'),
        "Vented Crawlspace - R38 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_floor_ins_dir, 'Vented Crawlspace - R38 Cavity Insulation.txt'),
        "Slab - Uninsulated": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_slab_ins_dir, 'Slab - Uninsulated.txt'),
        "Slab - R5 Perimeter with No Thermal Break": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_slab_ins_dir, 'Slab - R5 Perimeter with No Thermal Break.txt'),
        "Slab - R10 Perimeter with No Thermal Break": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_slab_ins_dir, 'Slab - R10 Perimeter with No Thermal Break.txt'),
        "Slab - R5 Perimeter with R5 Thermal Break": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_slab_ins_dir, 'Slab - R5 Perimeter with R5 Thermal Break.txt'),
        "Slab - R10 Perimeter with R5 Thermal Break": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_slab_ins_dir, 'Slab - R10 Perimeter with R5 Thermal Break.txt'),
        "Slab - R5 Under Full Slab with R5 Thermal Break": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_slab_ins_dir, 'Slab - R5 Under Full Slab with R5 Thermal Break.txt'),
        "Slab - R10 Under Full Slab with R5 Thermal Break": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_slab_ins_dir, 'Slab - R10 Under Full Slab with R5 Thermal Break.txt'),
        "Heated Basement - Uninsulated": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Heated Basement - Uninsulated.txt'),
        "Heated Basement - R5 Exterior Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Heated Basement - R5 Exterior Insulation.txt'),
        "Heated Basement - R10 Exterior Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Heated Basement - R10 Exterior Insulation.txt'),
        "Heated Basement - R15 Exterior Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Heated Basement - R15 Exterior Insulation.txt'),
        "Unheated Basement - Uninsulated": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Unheated Basement - Uninsulated.txt'),
        "Unheated Basement - R13 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Unheated Basement - R13 Cavity Insulation.txt'),
        "Unheated Basement - R19 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Unheated Basement - R19 Cavity Insulation.txt'),
        "Unheated Basement - R30 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Unheated Basement - R30 Cavity Insulation.txt'),
        "Unheated Basement - R38 Cavity Insulation": os.path.join(set_dir, building_block_dir, materials_main_dir, materials_basement_ins_dir, 'Unheated Basement - R38 Cavity Insulation.txt'),
        }

        ## water heater type dictionary
        ## this determines what water heater type will later be pulled to the idf
        water_heater_dict = {"Electric Storage_50-gallon": os.path.join(set_dir, building_block_dir, dhw_main_dir, dhw_wh_type_dir, 'Electric Storage_50-gallon.txt'),
        "Gas Storage_50-gallon": os.path.join(set_dir, building_block_dir, dhw_main_dir, dhw_wh_type_dir, 'Gas Storage_50-gallon.txt'),
        }

        ## hvac type dictionary
        ## this determines what water heater type will later be pulled to the idf
        hvac_dict = {"Air Source Heat Pump_Single Speed": os.path.join(set_dir, building_block_dir, hvac_main_dir, hvac_type_dir, 'Air Source Heat Pump_Single Speed.txt'),
        "Electric Furnace with CAC": os.path.join(set_dir, building_block_dir, hvac_main_dir, hvac_type_dir, 'Electric Furnace with CAC.txt'),
        "Electric Furnace with No CAC": os.path.join(set_dir, building_block_dir, hvac_main_dir, hvac_type_dir, 'Electric Furnace with No CAC.txt'),
        "Gas Furnace with CAC": os.path.join(set_dir, building_block_dir, hvac_main_dir, hvac_type_dir, 'Gas Furnace with CAC.txt'),
        "Gas Furnace with No CAC": os.path.join(set_dir, building_block_dir, hvac_main_dir, hvac_type_dir, 'Gas Furnace with No CAC.txt'),
        }

        ## output dictionary
        output_dict = {"Energy_All_End_Uses": os.path.join(set_dir, building_block_dir, output_dir, 'Energy_All_End_Uses.txt'),
        "Demand_All_End_Uses": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_All_End_Uses.txt'),
        "Demand_Total_Electric_HVAC": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_Total_Electric_HVAC.txt'),
        "Demand_Heating": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_Heating.txt'),
        "Demand_Cooling": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_Cooling.txt'),
        "Demand_Fan": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_Fan.txt'),
        "Demand_Lighting": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_Lighting.txt'),
        "Demand_Water_Heating": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_Water_Heating.txt'),
        "Demand_Other_Electric_Equipment": os.path.join(set_dir, building_block_dir, output_dir, 'Demand_Other_Electric_Equipment.txt'),
        }

        ## foundation type dictionary
        # contents of dictionary: foundation type name, text file required in ZonesAndSurfaces --> FoundationType, text file required in HVAC --> ReturnDuctLocation
        foundation_dict = {"Vent": ["Vented Crawlspace", 'Vented Crawl.txt', 'CrawlReturn.txt'],
        "Slab": ["Slab", 'Slab.txt', 'AtticReturn.txt'],
        "Heat": ["Heated Basement", 'Heated Basement.txt', 'InsideReturn.txt'],
        "Unhe": ["Unheated Basement", 'Unheated Basement.txt', 'UnheatedBasementReturn.txt'],
        }

        ## range type dictionary
        range_dict = {"Electric": os.path.join(set_dir, building_block_dir, gains_main_dir, gains_rangetype_dir, 'ElectricRange.txt'),
        "Gas": os.path.join(set_dir, building_block_dir, gains_main_dir, gains_rangetype_dir, 'GasRange.txt'),
        }

        ## dryer type dictionary
        dryer_dict = {"Electric": os.path.join(set_dir, building_block_dir, gains_main_dir, gains_dryertype_dir, 'ElectricDryer.txt'),
        "Gas": os.path.join(set_dir, building_block_dir, gains_main_dir, gains_dryertype_dir, 'GasDryer.txt'),
        }

        ## window blinds dictionary
        blinds_dict = {"Yes": os.path.join(set_dir, building_block_dir, window_main_dir, window_blinds_dir, 'YesBlinds.txt'),
        "No": os.path.join(set_dir, building_block_dir, window_main_dir, window_blinds_dir, 'NoBlinds.txt'),
        }

        #Find foundation type
        chars = 4
        foundation_key = foundation_and_floor_con[:chars]
        foundation_type = foundation_dict[foundation_key][0]

        ## this section imports all the necessary text from .txt files and turns them into strings
        ## the ones with changeable variables are turned into f-strings so that their values can be properly adjusted.

        ## Gains
        if range_type == "None":
            range_t = ""
        else:
            with open(range_dict[range_type], 'r') as f:
                range_t = f.read()
        if dryer_type == "None":
            dryer_t = ""
        else:
            with open(dryer_dict[dryer_type], 'r') as f:
                dryer_t = f.read()
        if clotheswasher == "None":
            clotheswasher_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'ClothesWasher.txt'), 'r') as f:
                clotheswasher_t = f.read()
        if dishwasher == "None":
            dishwasher_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'Dishwasher.txt'), 'r') as f:
                dishwasher_t = f.read()
        if frig == "None":
            frig_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'Refrigerator.txt'), 'r') as f:
                frig_t = f.read()
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'MiscElectric.txt'), 'r') as f:
            misc_elec_t = f"{f.read()}".format(**locals())
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'MiscGas.txt'), 'r') as f:
            misc_gas_t = f"{f.read()}".format(**locals())
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'People.txt'), 'r') as f:
            people_t = f"{f.read()}".format(**locals())
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, 'Lights.txt'), 'r') as f:
            lights_t = f"{f.read()}".format(**locals())

        ## Constructions
        with open(os.path.join(set_dir, building_block_dir, 'Constructions.txt'), 'r') as f:
            construction_t = f.read()

        ## DHW
        if water_heater_type == "None":
            water_heater_t = ""
            dhw_t = ""
        else:
            with open(water_heater_dict[water_heater_type], 'r') as f:
                water_heater_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, dhw_main_dir, 'OtherDHW.txt'), 'r') as f:
                dhw_t = f.read()

        ## Simulation Parameters
        with open(os.path.join(set_dir, building_block_dir, 'SimulationParameters.txt'), 'r') as f:
            simparam_t = f"{f.read()}".format(**locals())

        ## Windows
        #... set U-value and SHGC
        with open(os.path.join(set_dir, building_block_dir, window_main_dir, 'SimpleGlazingSystem.txt'), 'r') as f:
            glazing_t = f"{f.read()}".format(**locals())
        #... set window construction (i.e. with or without blinds)
        if window_shades == "Yes":
            with open(blinds_dict[window_shades], 'r') as f:
                win_construction_t = f.read()
        else:
            with open(blinds_dict[window_shades], 'r') as f:
                win_construction_t = f.read()
        #... choose whether to add window overhangs
        if window_overhangs == "Yes":
            with open(os.path.join(set_dir, building_block_dir, window_main_dir, 'Overhangs.txt'), 'r') as f:
                overhangs_t = f"{f.read()}".format(**locals())
        else:
            overhangs_t = ""

        ## Locations and Climate
        with open(location_dict[location_pull], 'r') as f: # our location & climate dictionary in action
            locations_t = f.read()

        ## HVAC
        #... get main HVAC type
        with open(hvac_dict[hvac_type], 'r') as f:
            hvac_type_t = f"{f.read()}".format(**locals())
        #... get appropriate return duct location, which depends on foundation type
        with open(os.path.join(set_dir, building_block_dir, hvac_main_dir, hvac_returnduct_dir, foundation_dict[foundation_key][2]), 'r') as f:
            hvac_returnduct_t = f.read()
        #... get duct leakage
        with open(os.path.join(set_dir, building_block_dir, hvac_main_dir, 'DuctLeakage.txt'), 'r') as f:
            duct_leak_t = f"{f.read()}".format(**locals())
        #... get all other HVAC code
        with open(os.path.join(set_dir, building_block_dir, hvac_main_dir, 'OtherHVAC.txt'), 'r') as f:
            hvac_t = f.read()

        ## Materials
        #... insert user-entered above-ground wall insulation
        with open(above_ground_wall_dict[above_ground_wall_con], 'r') as f:
            above_ground_wall_t = f.read()
        #... insert user-entered ceiling/attic insulation
        with open(ceiling_and_roof_dict[ceiling_and_roof_con], 'r') as f:
            ceiling_attic_t = f.read()
        with open(foundation_and_floor_dict[foundation_and_floor_con], 'r') as f:
            foundation_floor_t = f.read()
        #...insert all other materials
        with open(os.path.join(set_dir, building_block_dir, materials_main_dir, 'OtherMaterials.txt'), 'r') as f:
            mat_t = f.read()

        ## Performance Curves
        with open(os.path.join(set_dir, building_block_dir, 'PerformanceCurves.txt'), 'r') as f:
            perf_t = f.read()

        ## Schedules
        # htg_sch_num = sched_list.index(htg_stpt_sch) + 1
        # clg_sch_num = sched_list.index(clg_stpt_sch) + 1
        # dhw_sch_num = sched_list.index(dhw_stpt_sch) + 1
        with open(os.path.join(set_dir, building_block_dir, schedule_dir, 'Schedules.txt'), 'r') as f:
            sched_t = f"{f.read()}".format(**locals())

        ## Zones and Surfaces
        #... insert zones and surfaces specific to foundation types
        with open(os.path.join(set_dir, building_block_dir, zones_surfaces_main_dir, zones_surfaces_foundation_dir, foundation_dict[foundation_key][1]), 'r') as f:
            foundation_type_t = f"{f.read()}".format(**locals())
        #... insert zones and surfaces in common across foundation types
        with open(os.path.join(set_dir, building_block_dir, zones_surfaces_main_dir, 'OtherZonesAndSurfaces.txt'), 'r') as f:
            otherzones_t = f.read()

        ## Output
        with open(os.path.join(set_dir, building_block_dir, output_dir, 'OtherOutput.txt'), 'r') as f:
            output_t = f.read()
        with open(output_dict[output_lookup], 'r') as f:
            user_output_t = f"{f.read()}".format(**locals())

        ## nests all the .txt files, now morphed into strings, in a listin the order they are to be written to the new idfs.
        ## nesting them this way allows us to easily write the full idf file, because we can simply iterate over the list
        master_tl = [simparam_t, locations_t, sched_t, mat_t, above_ground_wall_t, ceiling_attic_t, foundation_floor_t, glazing_t, win_construction_t, \
            overhangs_t, construction_t, foundation_type_t, otherzones_t, range_t, dryer_t, clotheswasher_t, dishwasher_t, frig_t, misc_elec_t, misc_gas_t,\
            people_t, lights_t, hvac_type_t, hvac_t, duct_leak_t, hvac_returnduct_t, water_heater_t, dhw_t, perf_t, output_t, user_output_t]

        #the idf writing actually begins here
        fullidf = "" # the full idf begins as a blank string
        for bigstring in master_tl:
            fullidf += bigstring # every stringified .txt file gets added to the idf
        filename = f"{run_label}.idf" # then it gets named after the harvested runlabel
        path = os.path.join(get_data_dict["master_directory"], run_label, filename) # the path gets set for the new idf
        with open(path, 'w') as newfile:
                newfile.write(fullidf) # and voila! the idf gets written for the present runlabel, and the loop begins again

        i = i + 1
        get_data_dict["runlog"].write("... successfully built EnergyPlus model at " +  path + " \n")

    # Update simulation status box in REEDR.xlsm...
    #sht1['D16'] = "Starting model build... Model build complete."
    print("...model build complete.")
    print()

    get_data_dict["runlog"].write("... \n")

    ##########################################################################################################################
