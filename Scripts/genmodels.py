### --- Import modules. --- ###
import pandas as pd # to import xcel, some initial data manipulation
import os # for making paths and directories and removing files
import shutil # for removing full directories
import math # used for functions like square root
from pprint import pprint # for debugging
from unitconversions import convert_WperFt2_to_WperM2, convert_degF_to_degC, convert_IP_Uvalue_to_SI_Uvalue, convert_ft_to_m, convert_ft2_to_m2, convert_ft3_to_m3, \
    convert_Btuh_to_W, convert_kW_to_ton, convert_CFM_to_m3PerSec
from dictionaries import make_foundation_and_floor_dict, make_hvac_dict, make_furnace_capacity_dict, make_hpOrAC_capacity_dict, make_baseboard_capacity_dict, \
    make_duct_dict, make_foundation_dict
from datavalidation import validate


def genmodels(gui_params, get_data_dict):

    ### --- Set the main working directory. --- ###
    set_dir = get_data_dict["parent"]

    ### --- Define building block directory and folder names as variables, so they can be established only once here, and flow throughout. --- ###
    building_block_dir = "Building Blocks"
    schedule_dir = "Schedules"
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

    ### --- Get input variables from tkinter user interface. --- ###
    begin_mo = get_data_dict["begin_mo"]
    begin_day = get_data_dict["begin_day"]
    end_mo = get_data_dict["end_mo"]
    end_day = get_data_dict["end_day"]
    sim_type = get_data_dict["sim_type"]
    output_gran = gui_params["output_gran"]
    output_enduses = gui_params["output_enduses"]

    ### --- Update simulation status in command prompt. --- ###
    print("Starting model build...")

    ### --- Create Schedules.csv file and store headers in a list --- ###
    read_file = pd.read_excel (get_data_dict["REEDR_wb"], sheet_name="Schedules_8760")
    if os.path.exists(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)) == True:
        try:
            os.remove(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file))
            read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)), index = None, header=True)
            get_data_dict["runlog"].write("Schedules.csv successfully overwritten at " + os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file) + ". \n" + "... \n")
        except Exception as e:
            get_data_dict["runlog"].write("!!! Schedules.csv could not be made at " + os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file) + ". \n")
            get_data_dict["runlog"].write("!!! REEDR experienced the following error: " + str(e) + ". \n")
    else:
        read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file)), index = None, header=True)
        get_data_dict["runlog"].write(schedule_file + " successfully created at " + os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file) + ". \n" + "... \n")
    
    sched_list = (list(read_file.columns))

    ### --- Gather the run labels from the user specified runs, and create subdirectories that will house each run's input and output. --- ###
    directory_names = []
    for i in range(len(get_data_dict["df"])): # Note: df is a Pandas dataframe that contains user inputs from the "Model_Inputs" tab in REEDR.xlsx
        directory_names.append(get_data_dict["df"].loc[i][0])

    get_data_dict["runlog"].write("Starting to build subdirectories under " + os.path.join(get_data_dict["master_directory"]) + ". \n")

    for name in directory_names:
        path = os.path.join(get_data_dict["master_directory"], name) # Note: the "master directory" is the user-defined "Project" folder
        try:
            os.mkdir(path)
            get_data_dict["runlog"].write("... subdirectory successfully created at " + path + ". \n")
        except Exception as e:
            get_data_dict["runlog"].write("!!! subdirectory could not be created at " + path + ". \n")
            get_data_dict["runlog"].write("!!! REEDR experienced the following error: " + str(e) + ". \n")
            get_data_dict["runlog"].close()
            print("\n*** ERROR: Subdirectory could not be created for the run: " + name + ". ***\nPlease ensure that ALL Run Labels are unique.\n")
            return True

    get_data_dict["runlog"].write("... \n")

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
    # primary furnace heating capacity dictionary
    furnace_capacity_dict = make_furnace_capacity_dict()
    # primary heat pump or ac capacity dictionary
    hpOrAC_capacity_dict = make_hpOrAC_capacity_dict()
    # baseboard capacity dictionary
    baseboard_capacity_dict = make_baseboard_capacity_dict()
    # duct dictionary
    duct_dict = make_duct_dict()
    # foundation type dictionary
    foundation_dict = make_foundation_dict()

    ### --- IDF WRITER LOOP BEGINS HERE. --- ###
    # The loop covers every dictionary (effectively a runlabel row) in the big dictionary list.
    # Each time the loop comes to a new dictionary/runlabel row, it updates the changable variables before doing anything else.
    get_data_dict["runlog"].write("Starting to build EnergyPlus .idf model files... \n")

    i = 1
    for dictionary in get_data_dict["master_dict_list"]:

        # Update simulation status...
        status = "...building model " + str(i) + " of " + str(len(get_data_dict["df"])) + "..."
        print(status)

        # Get user inputs from REEDR Excel input file. Each variable below maps to a field in the Excel input sheet.
        run_label = str(dictionary["Run Label"])
        try:
            timestep = validate(dictionary["Timesteps Per Hr"], "Simulation timesteps per hour" , "integer" , 1 , 60)
        except:
            print("\n*** ERROR: Timstep must be...\n")
            return True
        location_pull = dictionary["Weather File"]
        bldg_orient = dictionary["Bldg Orient [deg]"]
        conditioned_footprint_area = round(convert_ft2_to_m2(dictionary["Conditioned Footprint Area [ft^2]"]),10)
        total_conditioned_volume = round(convert_ft3_to_m3(dictionary["Total Conditioned Volume Above Foundation Walls [ft^3]"]),10)
        ratio_width_to_depth = dictionary["Ratio Width to Depth"]
        above_ground_wall_con = dictionary["Exterior Non-Foundation Wall Construction"]
        ceiling_and_roof_con = dictionary["Ceiling And Roof Construction"]
        foundation_and_floor_con = dictionary["Foundation And Floor Construction"]
        foundationwall_ht_AG = round(convert_ft_to_m(dictionary["Foundation Wall Height Above Ground [ft]"]),10)
        foundationwall_ht_BG = -1 * round(convert_ft_to_m(dictionary["Foundation Wall Height Below Ground [ft]"]),10)
        windowu_val = round(convert_IP_Uvalue_to_SI_Uvalue(dictionary["Window U-Value [Btu/h/ft^2/F]"]),2)
        window_shgc = dictionary["Window SHGC"]
        window_shades = dictionary["Window Shades"]
        # window_overhangs = dictionary["Window Overhangs"] - CURRENTLY NOT USED
        wtw_ratio_front = dictionary["WtW Ratio Front [%]"]
        wtw_ratio_back = dictionary["WtW Ratio Back [%]"]
        wtw_ratio_left = dictionary["WtW Ratio Left [%]"]
        wtw_ratio_right = dictionary["WtW Ratio Right [%]"]
        hvac_type = dictionary["Primary HVAC Type"]
        furnace_capacity_primary = dictionary["Primary HVAC Furnace or Resistance Wall Heat Max Rated Capacity"]
        hpOrAC_capacity_primary = dictionary["Primary HVAC Heat Pump or AC Max Rated Capacity"]
        hp_supp_heat_type = dictionary["ASHP Backup Heat Type"]
        hp_supp_heat_capacity = dictionary["ASHP Backup Max Rated Capacity"]
        hp_max_resistance_temp = convert_degF_to_degC(dictionary["ASHP Backup Heat Lockout Temp [deg F]"])
        hp_min_compressor_temp = convert_degF_to_degC(dictionary["ASHP Compressor Lockout Temp [deg F]"])
        baseboard_heat_capacity = dictionary["Backup Electric Baseboard Heat Capacity"]
        supply_leak = dictionary["Supply Duct Leakage [%]"]
        return_leak = dictionary["Return Duct Leakage [%]"]
        htg_stpt_sch = dictionary["Htg StPt Sch"]
        clg_stpt_sch = dictionary["Clg StPt Sch"]
        gas_furnace_AFUE = dictionary["Gas Furnace AFUE [%]"]
        water_heater_type = dictionary["Water Heater Type"]
        dhw_stpt_sch = dictionary["DHW StPt Sch"]
        people = dictionary["Number Of People"]
        interior_lpd = convert_WperFt2_to_WperM2(dictionary["Interior LPD [W/ft^2]"])/2 #divide total lpd by plug lights and hardwired lights
        exterior_lp = dictionary["Exterior LP [W]"]/2 #divide total lp by garage lights and exterior facade lights
        range_type = dictionary["Range"]
        dryer_type = dictionary["Dryer"]
        frig = dictionary["Refrigerator"]
        clotheswasher = dictionary["ClothesWasher"]
        dishwasher = dictionary["Dishwasher"]
        misc_elec = dictionary["Misc Electric Gains [Max W]"]
        misc_gas = convert_Btuh_to_W(dictionary["Misc Gas Gains [Max Btu/h]"])

        ## Set window construction
        win_construction = "Exterior Window"

        # Establish foundation type
        chars = 4
        foundation_key = foundation_and_floor_con[:chars]
        foundation_type = foundation_dict[foundation_key][0]
        returnduct_location = foundation_dict[foundation_key][1]

        # Set foundation parameters based on foundation type
        main_floor_construction = foundation_and_floor_dict[foundation_and_floor_con][0]
        foundation_surface = foundation_and_floor_dict[foundation_and_floor_con][1]
        int_horiz_ins_mat_name = foundation_and_floor_dict[foundation_and_floor_con][2]
        int_horiz_ins_depth = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con][3])
        int_horiz_ins_width = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con][4])
        int_vert_ins_mat_name = foundation_and_floor_dict[foundation_and_floor_con][5]   
        int_vert_ins_depth = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con][6])
        ext_vert_ins_mat_name = foundation_and_floor_dict[foundation_and_floor_con][7]  
        ext_vert_ins_depth = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con][8])
        wall_ht_above_grade = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con][9])
        wall_ht_below_slab = convert_ft_to_m(foundation_and_floor_dict[foundation_and_floor_con][10])
        floor_insulation_layer = foundation_and_floor_dict[foundation_and_floor_con][11]
        floor_main_outside_boundary_condition = foundation_and_floor_dict[foundation_and_floor_con][12]
        floor_main_outside_boundary_condition_object = foundation_and_floor_dict[foundation_and_floor_con][13]
        foundation_zone_name = foundation_and_floor_dict[foundation_and_floor_con][14]

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
        #... choose whether to add window overhangs - CURRENTLY NOT USED
        # if window_overhangs == "Yes":
        #     with open(os.path.join(set_dir, building_block_dir, window_main_dir, 'Overhangs.txt'), 'r') as f:
        #         overhangs_t = f"{f.read()}".format(**locals())
        # else:
        #     overhangs_t = ""

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
        
        ### --- Adding building HVAC system --- ###
        # Get HVAC capacities from Excel input sheet.
        if furnace_capacity_primary in furnace_capacity_dict:
            furnace_capacity = furnace_capacity_dict[furnace_capacity_primary]
        else:
            furnace_capacity = ""
        if hpOrAC_capacity_primary in hpOrAC_capacity_dict:
            hpOrAC_capacity = hpOrAC_capacity_dict[hpOrAC_capacity_primary]
        else:
            hpOrAC_capacity = ""
        if hp_supp_heat_capacity in furnace_capacity_dict:
            supp_furnace_capacity = furnace_capacity_dict[hp_supp_heat_capacity]
        else:
            supp_furnace_capacity = ""
        if baseboard_heat_capacity in baseboard_capacity_dict:    
            baseboard_capacity = baseboard_capacity_dict[baseboard_heat_capacity]
        else:
            baseboard_capacity = 0
        
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
        heating_capacitymult_spd_1 = hvac_dict[hvac_type][31]
        heating_capacitymult_spd_2 = hvac_dict[hvac_type][32]
        heating_capacitymult_spd_3 = hvac_dict[hvac_type][33]
        heating_capacitymult_spd_4 = hvac_dict[hvac_type][34]

        # Assume effectively no integrated supplemental backup heat for a DHP
        if AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed" and hvac_dict[hvac_type][0] == "Zonal":
            hp_max_resistance_temp = convert_degF_to_degC(68)
            hp_min_compressor_temp = convert_degF_to_degC(-20)

        # Set max fan speed using the proper user inputted total HVAC capacity
        if AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirtoAir" or AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed":
            fan_m3PerSec_max = convert_CFM_to_m3PerSec(fan_CFMperTon_max * convert_kW_to_ton(hpOrAC_capacity/1000))
        else:
            fan_m3PerSec_max = convert_CFM_to_m3PerSec(fan_CFMperTon_max * convert_kW_to_ton(furnace_capacity/1000))
        
        # Set fan speeds and capacities using characteristics from HVAC dictionary and user selected HVAC type.
        # Variable speed equipment is modeled using four speeds.
        fan_m3PerSec_spd_1 = fan_CFMmult_spd_1 * fan_m3PerSec_max
        fan_m3PerSec_spd_2 = fan_CFMmult_spd_2 * fan_m3PerSec_max
        fan_m3PerSec_spd_3 = fan_CFMmult_spd_3 * fan_m3PerSec_max
        fan_m3PerSec_spd_4 = fan_CFMmult_spd_4 * fan_m3PerSec_max
        htg_capacity_spd_1 = heating_capacitymult_spd_1 * hpOrAC_capacity
        htg_capacity_spd_2 = heating_capacitymult_spd_2 * hpOrAC_capacity
        htg_capacity_spd_3 = heating_capacitymult_spd_3 * hpOrAC_capacity
        htg_capacity_spd_4 = heating_capacitymult_spd_4 * hpOrAC_capacity
        clg_capacity_spd_1 = htg_capacity_spd_1
        clg_capacity_spd_2 = htg_capacity_spd_2
        clg_capacity_spd_3 = htg_capacity_spd_3
        clg_capacity_spd_4 = htg_capacity_spd_4

        fan_max_flow_allowed = 1 * fan_m3PerSec_max

        # Add baseboard capacity if defined
        if baseboard_capacity != 0:
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
            AFN_main_leakage_t = f.read()
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
                AFN_crawl_unheatedbsmt_leakage_adder_t = f.read()
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
                AFN_crawl_unheatedbsmt_leakage_adder_t = f.read()
            #...add AFN surfaces for basement walls
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_surface_dir, 'AFN_CrawlUnheatedBsmtSurfaceAdder.txt'), 'r') as f:
                AFN_crawl_unheatedbsmt_surface_adder_t = f.read()
  
        # Get duct inputs based on HVAC type; for "zonal" systems assume "perfect ducts"
        maintrunk_duct_length = duct_dict[hvac_dict[hvac_type][0]][0]
        maintrunk_duct_Ufactor = duct_dict[hvac_dict[hvac_type][0]][1]
        zonesupply_duct_length = duct_dict[hvac_dict[hvac_type][0]][2]
        zonesupply_duct_Ufactor = duct_dict[hvac_dict[hvac_type][0]][3]
        zonereturn_duct_length = duct_dict[hvac_dict[hvac_type][0]][4]
        zonereturn_duct_Ufactor = duct_dict[hvac_dict[hvac_type][0]][5]
        mainreturn_duct_length = duct_dict[hvac_dict[hvac_type][0]][6]
        mainreturn_duct_Ufactor = duct_dict[hvac_dict[hvac_type][0]][7]
        
        # If HVAC type is "zonal", overwrite user-entered supply and duct leakage and assume "perfect" ducts
        if hvac_dict[hvac_type][0] == "Zonal":
            supply_leak = duct_dict[hvac_dict[hvac_type][0]][8]
            return_leak = duct_dict[hvac_dict[hvac_type][0]][9]

        # Add AFN ducts to all models
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, 'AFN_Ducts.txt'), 'r') as f:
            AFN_ducts_t = f"{f.read()}".format(**locals())
        
        #  Add a theromstat (T-stat)
        with open(os.path.join(set_dir, building_block_dir, hvac_tstat_dir, 'Thermostat.txt'), 'r') as f:
            thermostat_t = f.read()
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
        
        ### --- Assemble Final IDF Text File --- ###
        # Nests all the .txt files, now morphed into strings, in a listin the order they are to be written to the new idfs.
        # Nesting them this way allows us to easily write the full idf file, because we can simply iterate over the list
        master_tl = [
            simparam_t, performanceprecision_t, locations_t, sched_t, mat_t, above_ground_wall_t, ceiling_attic_t, glazing_t, win_construction_t, \
            construction_t, range_t, dryer_t, clotheswasher_t, dishwasher_t, frig_t, misc_elec_t, misc_gas_t, people_t, lights_t, \
            foundation_type_t, geom_rules_t, internal_mass_t, geom_main_envelope_t, geom_nonslab_adder_t, geom_main_windows_t, \
            living_zone_t, attic_zone_t, unheatedbsmt_zone_t, crawlspace_zone_t, geom_nonhtdbsmt_adder_t, \
            AFN_sim_control_t, AFN_main_zones_t, AFN_main_leakage_t, AFN_main_surfaces_t, AFN_nodes_main_t, AFN_linkage_main_t, \
            AFN_crawl_zone_t, AFN_unheatedbsmt_zone_t, AFN_crawl_unheatedbsmt_leakage_adder_t, AFN_crawl_unheatedbsmt_surface_adder_t, \
            AFN_ducts_t, system_sizing_t, airloop_t, AFN_linkage_coolingcoiladder_t, AFN_nodes_coolingcoiladder_t, \
            zone_equip_list_t, HVAC_equip_1_t, HVAC_equip_2_t, heating_coil_t, supp_heating_coil_t, cooling_coil_t, fan_t, \
            baseboard_t, thermostat_t, zone_sizing_t, water_heater_t, dhw_t, perf_t, output_t, user_output_t
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
        get_data_dict["runlog"].write("... successfully built EnergyPlus model at " +  path + " \n")

    print("...model build complete.")
    print()

    get_data_dict["runlog"].write("... \n")

    return False
    ##########################################################################################################################
