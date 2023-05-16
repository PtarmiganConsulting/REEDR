#*******************************************************************************************************************************************************************

#Copyright (C) 2023 Ptarmigan Consulting LLC

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************

### --- Import modules. --- ###
import pandas as pd # to import xcel, some initial data manipulation
import os # for making paths and directories and removing files
import shutil # for removing full directories
import math # used for functions like square root
from pprint import pprint
from pathlib import Path
import datetime
from Scripts.unitconversions import convert_WperFt2_to_WperM2, convert_degF_to_degC, convert_IP_Uvalue_to_SI_Uvalue, convert_ft_to_m, convert_ft2_to_m2, \
    convert_Btuh_to_W, convert_CFM_to_m3PerSec, convert_W_to_ton
from Scripts.datavalidation import validate, convert_capacity
from Scripts.utilfunctions import estimateInfiltrationAdjustment, findLastRealLayer, formatLayerList, getFoundationIdentifier
from Scripts.dictmaker import dict_maker


def genmodels(gui_params, get_data_dict, control_panel_dict):

    ### --- Set the main working directory. --- ###
    set_dir = get_data_dict["parent"]

    ### -- Check EnergyPlus.exe path --- ###
    ePlusExePath = gui_params["path_val"]
    if os.path.exists(ePlusExePath) == False:
        print("*** ERROR: Could not find energyplus.exe at the path specified. Please ensure EnergyPlus is installed on your computer at the path specified.\n")
        return True

    ### --- Define control panel directory and file names as variables, so they can be established only once here, and flow throughout --- ###
    #... get folder and file names from CSV
    control_panel_folder_name = control_panel_dict["control_panel_folder_name"]
    control_panel_names_dict = control_panel_dict["control_panel_names_dict"]
    control_panel_names_lookup_id = control_panel_dict["control_panel_names_lookup_id"]
    #... assign fieldnames to python variables
    buildingBlock_names_file = control_panel_names_dict["buildingBlock_names_file"][control_panel_names_lookup_id]
    inputTemplate_names_file = control_panel_names_dict["inputTemplate_names_file"][control_panel_names_lookup_id]
    found_type_assumptions_file = control_panel_names_dict["found_type_assumptions_file"][control_panel_names_lookup_id]
    roof_pitch_file = control_panel_names_dict["roof_pitch_file"][control_panel_names_lookup_id]
    envelope_construction_dir = control_panel_names_dict["envelope_construction_dir"][control_panel_names_lookup_id]
    envelope_construction_ceilingRoof_file = control_panel_names_dict["envelope_construction_ceilingRoof_file"][control_panel_names_lookup_id]
    envelope_construction_nonFoundWall_file = control_panel_names_dict["envelope_construction_nonFoundWall_file"][control_panel_names_lookup_id]
    envelope_construction_floorFound_file = control_panel_names_dict["envelope_construction_floorFound_file"][control_panel_names_lookup_id]
    hvac_systems_dir = control_panel_names_dict["hvac_systems_dir"][control_panel_names_lookup_id]
    hvac_systems_primary_file = control_panel_names_dict["hvac_systems_primary_file"][control_panel_names_lookup_id]
    infil_regression_coeff_dir = control_panel_names_dict["infil_regression_coeff_dir"][control_panel_names_lookup_id]
    infil_regression_coeff_attic_file = control_panel_names_dict["infil_regression_coeff_attic_file"][control_panel_names_lookup_id]
    infil_regression_coeff_crawl_file = control_panel_names_dict["infil_regression_coeff_crawl_file"][control_panel_names_lookup_id]
    infil_regression_coeff_living_file = control_panel_names_dict["infil_regression_coeff_living_file"][control_panel_names_lookup_id]

    ### --- Define building block directory and file names as variables, so they can be established only once here, and flow throughout. --- ###
    #... get folder and file names from CSV
    building_block_names_path = os.path.join(set_dir, control_panel_folder_name, buildingBlock_names_file)
    building_block_names_dict = dict_maker(building_block_names_path)
    bldg_blk_names_lookup_id = "folder_or_file_name"
    #... assign folder and file names to python variables
    building_block_dir = building_block_names_dict["building_block_dir"][bldg_blk_names_lookup_id]
    building_block_constructions_file = building_block_names_dict["building_block_constructions_file"][bldg_blk_names_lookup_id]
    building_block_foundation_file = building_block_names_dict["building_block_foundation_file"][bldg_blk_names_lookup_id]
    building_block_materials_file = building_block_names_dict["building_block_materials_file"][bldg_blk_names_lookup_id]
    building_block_outputControl_file = building_block_names_dict["building_block_outputControl_file"][bldg_blk_names_lookup_id]
    building_block_performanceCurve_file = building_block_names_dict["building_block_performanceCurve_file"][bldg_blk_names_lookup_id]
    building_block_simParameters_file = building_block_names_dict["building_block_simParameters_file"][bldg_blk_names_lookup_id]
    schedule_dir = building_block_names_dict["schedule_dir"][bldg_blk_names_lookup_id]
    schedule_elec_gains_dir = building_block_names_dict["schedule_elec_gains_dir"][bldg_blk_names_lookup_id]
    schedule_elec_gains_default_file = building_block_names_dict["schedule_elec_gains_default_file"][bldg_blk_names_lookup_id]
    schedule_elec_gains_custom_file = building_block_names_dict["schedule_elec_gains_custom_file"][bldg_blk_names_lookup_id]
    schedule_gas_gains_dir = building_block_names_dict["schedule_gas_gains_dir"][bldg_blk_names_lookup_id]
    schedule_gas_gains_default_file = building_block_names_dict["schedule_gas_gains_default_file"][bldg_blk_names_lookup_id]
    schedule_gas_gains_custom_file = building_block_names_dict["schedule_gas_gains_custom_file"][bldg_blk_names_lookup_id]
    schedule_DHW_draws_dir = building_block_names_dict["schedule_DHW_draws_dir"][bldg_blk_names_lookup_id]
    schedule_CSV = building_block_names_dict["schedule_CSV"][bldg_blk_names_lookup_id]
    schedule_file = building_block_names_dict["schedule_file"][bldg_blk_names_lookup_id]
    #location_and_climate_dir = building_block_names_dict["location_and_climate_dir"][bldg_blk_names_lookup_id]
    dhw_main_dir = building_block_names_dict["dhw_main_dir"][bldg_blk_names_lookup_id]
    dhw_wh_type_dir = building_block_names_dict["dhw_wh_type_dir"][bldg_blk_names_lookup_id]
    dhw_sys_file = building_block_names_dict["dhw_sys_file"][bldg_blk_names_lookup_id]
    gains_main_dir = building_block_names_dict["gains_main_dir"][bldg_blk_names_lookup_id]
    gains_cw_file = building_block_names_dict["gains_cw_file"][bldg_blk_names_lookup_id]
    gains_dw_file = building_block_names_dict["gains_dw_file"][bldg_blk_names_lookup_id]
    gains_lights_file = building_block_names_dict["gains_lights_file"][bldg_blk_names_lookup_id]
    gains_miscElec_file = building_block_names_dict["gains_miscElec_file"][bldg_blk_names_lookup_id]
    gains_miscGas_file = building_block_names_dict["gains_miscGas_file"][bldg_blk_names_lookup_id]
    gains_people_file = building_block_names_dict["gains_people_file"][bldg_blk_names_lookup_id]
    gains_frig_file = building_block_names_dict["gains_frig_file"][bldg_blk_names_lookup_id]
    gains_dryertype_dir = building_block_names_dict["gains_dryertype_dir"][bldg_blk_names_lookup_id]
    gains_rangetype_dir = building_block_names_dict["gains_rangetype_dir"][bldg_blk_names_lookup_id]
    hvac_afn_main_dir = building_block_names_dict["hvac_afn_main_dir"][bldg_blk_names_lookup_id]
    hvac_afn_ducts_file = building_block_names_dict["hvac_afn_ducts_file"][bldg_blk_names_lookup_id]
    hvac_afn_simcontrol_file = building_block_names_dict["hvac_afn_simcontrol_file"][bldg_blk_names_lookup_id]
    hvac_afn_leakage_dir = building_block_names_dict["hvac_afn_leakage_dir"][bldg_blk_names_lookup_id]
    hvac_afn_leakage_main_file = building_block_names_dict["hvac_afn_leakage_main_file"][bldg_blk_names_lookup_id]
    hvac_afn_leakage_adder_file = building_block_names_dict["hvac_afn_leakage_adder_file"][bldg_blk_names_lookup_id]
    hvac_afn_linkage_dir = building_block_names_dict["hvac_afn_linkage_dir"][bldg_blk_names_lookup_id]
    hvac_afn_linkage_main_file = building_block_names_dict["hvac_afn_linkage_main_file"][bldg_blk_names_lookup_id]
    hvac_afn_linkage_adder_file = building_block_names_dict["hvac_afn_linkage_adder_file"][bldg_blk_names_lookup_id]
    hvac_afn_node_dir = building_block_names_dict["hvac_afn_node_dir"][bldg_blk_names_lookup_id]
    hvac_afn_node_main_file = building_block_names_dict["hvac_afn_node_main_file"][bldg_blk_names_lookup_id]
    hvac_afn_node_adder_file = building_block_names_dict["hvac_afn_node_adder_file"][bldg_blk_names_lookup_id]
    hvac_afn_surface_dir = building_block_names_dict["hvac_afn_surface_dir"][bldg_blk_names_lookup_id]
    hvac_afn_surface_main_file = building_block_names_dict["hvac_afn_surface_main_file"][bldg_blk_names_lookup_id]
    hvac_afn_surface_adder_file = building_block_names_dict["hvac_afn_surface_adder_file"][bldg_blk_names_lookup_id]
    hvac_afn_zone_dir = building_block_names_dict["hvac_afn_zone_dir"][bldg_blk_names_lookup_id]
    hvac_afn_zone_main_file = building_block_names_dict["hvac_afn_zone_main_file"][bldg_blk_names_lookup_id]
    hvac_afn_zone_crawl_adder_file = building_block_names_dict["hvac_afn_zone_crawl_adder_file"][bldg_blk_names_lookup_id]
    hvac_afn_zone_unhtdbsmt_adder_file = building_block_names_dict["hvac_afn_zone_unhtdbsmt_adder_file"][bldg_blk_names_lookup_id]
    hvac_airloop_main_dir = building_block_names_dict["hvac_airloop_main_dir"][bldg_blk_names_lookup_id]
    hvac_airloop_file = building_block_names_dict["hvac_airloop_file"][bldg_blk_names_lookup_id]
    hvac_airloop_sysSizing_file = building_block_names_dict["hvac_airloop_sysSizing_file"][bldg_blk_names_lookup_id]
    hvac_airloop_hvac_dir = building_block_names_dict["hvac_airloop_hvac_dir"][bldg_blk_names_lookup_id]
    hvac_coil_dir = building_block_names_dict["hvac_coil_dir"][bldg_blk_names_lookup_id]
    hvac_fan_dir = building_block_names_dict["hvac_fan_dir"][bldg_blk_names_lookup_id]
    hvac_tstat_dir = building_block_names_dict["hvac_tstat_dir"][bldg_blk_names_lookup_id]
    hvac_tstat_file = building_block_names_dict["hvac_tstat_file"][bldg_blk_names_lookup_id]
    hvac_zone_main_dir = building_block_names_dict["hvac_zone_main_dir"][bldg_blk_names_lookup_id]
    hvac_zone_equipList_file = building_block_names_dict["hvac_zone_equipList_file"][bldg_blk_names_lookup_id]
    hvac_zone_zoneSizing_file = building_block_names_dict["hvac_zone_zoneSizing_file"][bldg_blk_names_lookup_id]
    hvac_zone_hvac_dir = building_block_names_dict["hvac_zone_hvac_dir"][bldg_blk_names_lookup_id]
    output_dir = building_block_names_dict["output_dir"][bldg_blk_names_lookup_id]
    output_otherOutput_file = building_block_names_dict["output_otherOutput_file"][bldg_blk_names_lookup_id]
    window_main_dir = building_block_names_dict["window_main_dir"][bldg_blk_names_lookup_id]
    window_main_simpleGlazingSys_file = building_block_names_dict["window_main_simpleGlazingSys_file"][bldg_blk_names_lookup_id]
    window_blinds_dir = building_block_names_dict["window_blinds_dir"][bldg_blk_names_lookup_id]
    geometry_main_dir = building_block_names_dict["geometry_main_dir"][bldg_blk_names_lookup_id]
    geometry_globalRules_file = building_block_names_dict["geometry_globalRules_file"][bldg_blk_names_lookup_id]
    geometry_internalMass_file = building_block_names_dict["geometry_internalMass_file"][bldg_blk_names_lookup_id]
    geometry_envelope_dir = building_block_names_dict["geometry_envelope_dir"][bldg_blk_names_lookup_id]
    geometry_envelope_main_file = building_block_names_dict["geometry_envelope_main_file"][bldg_blk_names_lookup_id]
    geometry_envelope_nonslabAdder_file = building_block_names_dict["geometry_envelope_nonslabAdder_file"][bldg_blk_names_lookup_id]
    geometry_envelope_nonhtdbsmntAdder_file = building_block_names_dict["geometry_envelope_nonhtdbsmntAdder_file"][bldg_blk_names_lookup_id]
    geometry_window_dir = building_block_names_dict["geometry_window_dir"][bldg_blk_names_lookup_id]
    geometry_window_file = building_block_names_dict["geometry_window_file"][bldg_blk_names_lookup_id]
    geometry_zone_dir = building_block_names_dict["geometry_zone_dir"][bldg_blk_names_lookup_id]
    geometry_attic_file = building_block_names_dict["geometry_attic_file"][bldg_blk_names_lookup_id]
    geometry_crawlspace_file = building_block_names_dict["geometry_crawlspace_file"][bldg_blk_names_lookup_id]
    geometry_living_file = building_block_names_dict["geometry_living_file"][bldg_blk_names_lookup_id]
    geometry_unhtdbsmnt_file = building_block_names_dict["geometry_unhtdbsmnt_file"][bldg_blk_names_lookup_id]
    performanceprecision_dir = building_block_names_dict["performanceprecision_dir"][bldg_blk_names_lookup_id]
    performanceprecision_highSpeed_file = building_block_names_dict["performanceprecision_highSpeed_file"][bldg_blk_names_lookup_id]
    performanceprecision_normal_file = building_block_names_dict["performanceprecision_normal_file"][bldg_blk_names_lookup_id]

    ### --- Define user input data field names --- ###
    #... get input template fieldnames from CSV
    model_input_temp_fieldnames_path = os.path.join(set_dir, control_panel_folder_name, inputTemplate_names_file)
    model_input_temp_fieldnames_dict = dict_maker(model_input_temp_fieldnames_path)
    input_template_names_lookup_id = "field_name"
    #... assign fieldnames to python variables
    runLabel_fieldname = model_input_temp_fieldnames_dict["runLabel_fieldname"][input_template_names_lookup_id]
    timestep_fieldname = model_input_temp_fieldnames_dict["timestep_fieldname"][input_template_names_lookup_id]
    weather_fieldname = model_input_temp_fieldnames_dict["weather_fieldname"][input_template_names_lookup_id]
    orient_fieldname = model_input_temp_fieldnames_dict["orient_fieldname"][input_template_names_lookup_id]
    footprint_fieldname = model_input_temp_fieldnames_dict["footprint_fieldname"][input_template_names_lookup_id]
    stories_fieldname = model_input_temp_fieldnames_dict["stories_fieldname"][input_template_names_lookup_id]
    heightPerStory_fieldname = model_input_temp_fieldnames_dict["heightPerStory_fieldname"][input_template_names_lookup_id]
    bldgRatio_fieldname = model_input_temp_fieldnames_dict["bldgRatio_fieldname"][input_template_names_lookup_id]
    roofPitch_fieldname = model_input_temp_fieldnames_dict["roofPitch_fieldname"][input_template_names_lookup_id]
    wallInputMethod_fieldname  = model_input_temp_fieldnames_dict["wallInputMethod_fieldname"][input_template_names_lookup_id]
    wallCon_fieldname = model_input_temp_fieldnames_dict["wallCon_fieldname"][input_template_names_lookup_id]
    wallRvalue_fieldname = model_input_temp_fieldnames_dict["wallRvalue_fieldname"][input_template_names_lookup_id]
    ceilingInputMethod_fieldname  = model_input_temp_fieldnames_dict["ceilingInputMethod_fieldname"][input_template_names_lookup_id]
    ceilingCon_fieldname = model_input_temp_fieldnames_dict["ceilingCon_fieldname"][input_template_names_lookup_id]
    ceilingRvalue_fieldname = model_input_temp_fieldnames_dict["ceilingRvalue_fieldname"][input_template_names_lookup_id]
    floorInputMethod_fieldname = model_input_temp_fieldnames_dict["floorInputMethod_fieldname"][input_template_names_lookup_id]
    floorCon_fieldname = model_input_temp_fieldnames_dict["floorCon_fieldname"][input_template_names_lookup_id]
    foundType_fieldname = model_input_temp_fieldnames_dict["foundType_fieldname"][input_template_names_lookup_id]
    floorRvalue_fieldname = model_input_temp_fieldnames_dict["floorRvalue_fieldname"][input_template_names_lookup_id]
    slabPerimRvalue_fieldname = model_input_temp_fieldnames_dict["slabPerimRvalue_fieldname"][input_template_names_lookup_id]
    slabUnderRvalue_fieldname = model_input_temp_fieldnames_dict["slabUnderRvalue_fieldname"][input_template_names_lookup_id]
    slabTBvalue_fieldname = model_input_temp_fieldnames_dict["slabTBvalue_fieldname"][input_template_names_lookup_id]
    foundWallRvalue_fieldname = model_input_temp_fieldnames_dict["foundWallRvalue_fieldname"][input_template_names_lookup_id]
    windowuUvalue_fieldname = model_input_temp_fieldnames_dict["windowuUvalue_fieldname"][input_template_names_lookup_id]
    windowSHGC_fieldname = model_input_temp_fieldnames_dict["windowSHGC_fieldname"][input_template_names_lookup_id]
    windowShade_fieldname = model_input_temp_fieldnames_dict["windowShade_fieldname"][input_template_names_lookup_id]
    wtwFront_fieldname = model_input_temp_fieldnames_dict["wtwFront_fieldname"][input_template_names_lookup_id]
    wtwBack_fieldname = model_input_temp_fieldnames_dict["wtwBack_fieldname"][input_template_names_lookup_id]
    wtwLeft_fieldname = model_input_temp_fieldnames_dict["wtwLeft_fieldname"][input_template_names_lookup_id]
    wtwRight_fieldname = model_input_temp_fieldnames_dict["wtwRight_fieldname"][input_template_names_lookup_id]
    infiltration_fieldname = model_input_temp_fieldnames_dict["infiltration_fieldname"][input_template_names_lookup_id]
    primaryHVAC_fieldname = model_input_temp_fieldnames_dict["primaryHVAC_fieldname"][input_template_names_lookup_id]
    hvacSizingMethod_fieldname = model_input_temp_fieldnames_dict["hvacSizingMethod_fieldname"][input_template_names_lookup_id]
    primaryHtgCapacityUnits_fieldname = model_input_temp_fieldnames_dict["primaryHtgCapacityUnits_fieldname"][input_template_names_lookup_id]
    primaryHtgCapacity_fieldname = model_input_temp_fieldnames_dict["primaryHtgCapacity_fieldname"][input_template_names_lookup_id]
    primaryClgCapacityUnits_fieldname = model_input_temp_fieldnames_dict["primaryClgCapacityUnits_fieldname"][input_template_names_lookup_id]
    primaryClgCapacity_fieldname = model_input_temp_fieldnames_dict["primaryClgCapacity_fieldname"][input_template_names_lookup_id]
    hpBackupType_fieldname = model_input_temp_fieldnames_dict["hpBackupType_fieldname"][input_template_names_lookup_id]
    hpBackupCapacityUnits_fieldname = model_input_temp_fieldnames_dict["hpBackupCapacityUnits_fieldname"][input_template_names_lookup_id]
    hpBackupCapacity_fieldname = model_input_temp_fieldnames_dict["hpBackupCapacity_fieldname"][input_template_names_lookup_id]
    backupBaseboardCapacity_fieldname = model_input_temp_fieldnames_dict["backupBaseboardCapacity_fieldname"][input_template_names_lookup_id]
    hpBackupLockout_fieldname = model_input_temp_fieldnames_dict["hpBackupLockout_fieldname"][input_template_names_lookup_id]
    hpCompressorLockout_fieldname = model_input_temp_fieldnames_dict["hpCompressorLockout_fieldname"][input_template_names_lookup_id]
    AFUE_fieldname = model_input_temp_fieldnames_dict["AFUE_fieldname"][input_template_names_lookup_id]
    supplyLeakage_fieldname = model_input_temp_fieldnames_dict["supplyLeakage_fieldname"][input_template_names_lookup_id]
    supplyRvalue_fieldname = model_input_temp_fieldnames_dict["supplyRvalue_fieldname"][input_template_names_lookup_id]
    returnLeakage_fieldname = model_input_temp_fieldnames_dict["returnLeakage_fieldname"][input_template_names_lookup_id]
    returnRvalue_fieldname = model_input_temp_fieldnames_dict["returnRvalue_fieldname"][input_template_names_lookup_id]
    htgSched_fieldname = model_input_temp_fieldnames_dict["htgSched_fieldname"][input_template_names_lookup_id]
    clgSched_fieldname = model_input_temp_fieldnames_dict["clgSched_fieldname"][input_template_names_lookup_id]
    dhwType_fieldname = model_input_temp_fieldnames_dict["dhwType_fieldname"][input_template_names_lookup_id]
    dhwSched_fieldname = model_input_temp_fieldnames_dict["dhwSched_fieldname"][input_template_names_lookup_id]
    numOfPeople_fieldname = model_input_temp_fieldnames_dict["numOfPeople_fieldname"][input_template_names_lookup_id]
    intLPD_fieldname = model_input_temp_fieldnames_dict["intLPD_fieldname"][input_template_names_lookup_id]
    extLP_fieldname = model_input_temp_fieldnames_dict["extLP_fieldname"][input_template_names_lookup_id]
    range_fieldname = model_input_temp_fieldnames_dict["range_fieldname"][input_template_names_lookup_id]
    dryer_fieldname = model_input_temp_fieldnames_dict["dryer_fieldname"][input_template_names_lookup_id]
    frig_fieldname = model_input_temp_fieldnames_dict["frig_fieldname"][input_template_names_lookup_id]
    cw_fieldname = model_input_temp_fieldnames_dict["cw_fieldname"][input_template_names_lookup_id]
    dw_fieldname = model_input_temp_fieldnames_dict["dw_fieldname"][input_template_names_lookup_id]
    miscElec_fieldname = model_input_temp_fieldnames_dict["miscElec_fieldname"][input_template_names_lookup_id]
    miscElecShed_fieldname = model_input_temp_fieldnames_dict["miscElecShed_fieldname"][input_template_names_lookup_id]
    miscGas_fieldname = model_input_temp_fieldnames_dict["miscGas_fieldname"][input_template_names_lookup_id]
    miscGasShed_fieldname = model_input_temp_fieldnames_dict["miscGasShed_fieldname"][input_template_names_lookup_id]

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
    if os.path.exists(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_CSV)) == True:
        try:
            os.remove(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_CSV))
            read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_CSV)), index = None, header=True)
        except:
            print("\n*** ERROR: Could not remove Schedule File. Please ensure that 8760 Schedule File is not open when running REEDR.\n")
            return True
    else:
        read_file.to_csv ((os.path.join(set_dir, building_block_dir, schedule_dir, schedule_CSV)), index = None, header=True)
    
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
    foundation_and_floor_path = os.path.join(set_dir, control_panel_folder_name, envelope_construction_dir, envelope_construction_floorFound_file)
    foundation_and_floor_dict = dict_maker(foundation_and_floor_path)

    # exterior non-foundation wall construction dictionary
    nonfoundation_wall_path = os.path.join(set_dir, control_panel_folder_name, envelope_construction_dir, envelope_construction_nonFoundWall_file)
    nonfoundation_wall_dict = dict_maker(nonfoundation_wall_path)

    # ceiling and roof construction dictionary
    ceiling_and_roof_con_path = os.path.join(set_dir, control_panel_folder_name, envelope_construction_dir, envelope_construction_ceilingRoof_file)
    ceiling_and_roof_con_dict = dict_maker(ceiling_and_roof_con_path)

    # hvac type dictionary
    hvac_path = os.path.join(set_dir, control_panel_folder_name, hvac_systems_dir, hvac_systems_primary_file)
    hvac_dict = dict_maker(hvac_path)

    # living zone infiltration regression coefficient dictionary
    living_infiltration_coeff_path = os.path.join(set_dir, control_panel_folder_name, infil_regression_coeff_dir, infil_regression_coeff_living_file)
    living_infiltration_coeff_dict = dict_maker(living_infiltration_coeff_path)

    # attic zone infiltration regression coefficients dictionary
    attic_infiltration_coeff_path = os.path.join(set_dir, control_panel_folder_name, infil_regression_coeff_dir, infil_regression_coeff_attic_file)
    attic_infiltration_coeff_dict = dict_maker(attic_infiltration_coeff_path)
    
    # crawl zone infiltration regression coefficients dictionary
    crawl_infiltration_coeff_path = os.path.join(set_dir, control_panel_folder_name, infil_regression_coeff_dir, infil_regression_coeff_crawl_file)
    crawl_infiltration_coeff_dict = dict_maker(crawl_infiltration_coeff_path)

    # foundation type assumptions dictionary
    foundation_type_assumptions_path = os.path.join(set_dir, control_panel_folder_name, found_type_assumptions_file)
    foundation_type_assumptions_dict = dict_maker(foundation_type_assumptions_path)

    # roof pitch dictionary
    roof_pitch_path = os.path.join(set_dir, control_panel_folder_name, roof_pitch_file)
    roof_pitch_dict = dict_maker(roof_pitch_path)
    
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
            # check to see if Actual Meterological Year (AMY) file. If so, treat differently to properly find sizing file
            # NOTE: THIS ISN'T CURRENTLY NEEDED OR USED, BECAUSE THE WEATHER FILES ARE USED FOR DESIGN DAYS.
            # if "AMY" in dictionary[weather_fieldname]:
            #     Str = dictionary[weather_fieldname]
            #     # strip off "AMY" and year
            #     Str = Str[:len(Str)-8]
            #     # convert to TMYx file to find proper design days
            #     Str = Str + "TMYx.2004-2018"
            #     location_path = os.path.join(set_dir, building_block_dir, location_and_climate_dir)
            #     location_pull = validate(weather_fieldname, Str, "file", dummy_int, dummy_int, dummy_list, location_path)
            # else:
            #     location_path = os.path.join(set_dir, building_block_dir, location_and_climate_dir)
            #     location_pull = validate(weather_fieldname, dictionary[weather_fieldname], "file", dummy_int, dummy_int, dummy_list, location_path)

             #... building orientation
            bldg_orient_lo = 0
            bldg_orient_hi = 359
            bldg_orient = validate(orient_fieldname, dictionary[orient_fieldname], "num_between", bldg_orient_lo, bldg_orient_hi, dummy_list)

            #... conditioned footprint area
            conditioned_footprint_area = float(validate(footprint_fieldname, round(convert_ft2_to_m2(dictionary[footprint_fieldname]),10), "num_not_zero", dummy_int, dummy_int, dummy_list))
            conditioned_footprint_area_ft2 = dictionary[footprint_fieldname]

            #... average building stories
            avgStories = float(validate(stories_fieldname, round(dictionary[stories_fieldname],10), "num_not_zero", dummy_int, dummy_int, dummy_list))

            #... average height per story
            avgHtPerStory = float(validate(heightPerStory_fieldname, round(convert_ft_to_m(dictionary[heightPerStory_fieldname]),10), "num_not_zero", dummy_int, dummy_int, dummy_list))
            avgHtPerStory_ft2 = dictionary[heightPerStory_fieldname]

            #... total conditioned volume
            total_conditioned_volume = conditioned_footprint_area * avgStories * avgHtPerStory

            #... Width to depth ratio
            ratio_width_to_depth = validate(bldgRatio_fieldname, dictionary[bldgRatio_fieldname], "num_not_zero", dummy_int, dummy_int, dummy_list)

            #... roof pitch
            valid_roof_pitch_options = roof_pitch_dict.keys()
            roof_pitch_selection = validate(roofPitch_fieldname, dictionary[roofPitch_fieldname], "list", dummy_int, dummy_int, valid_roof_pitch_options)
            roof_pitch_value = roof_pitch_dict[roof_pitch_selection]["pitch_value"]

            #... above ground wall construction
            # get above ground wall insulation input method, either "Pre-Defined Construction" or "Overall Effective R-Value"
            above_ground_wall_input_method = dictionary[wallInputMethod_fieldname]
            above_ground_wall_list = nonfoundation_wall_dict.keys()
            # if "Pre-Defined Construction", make sure construction exists and is defined
            if above_ground_wall_input_method == "Pre-Defined Construction":
                above_ground_wall_con = validate(wallCon_fieldname, dictionary[wallCon_fieldname], "list", dummy_int, dummy_int, above_ground_wall_list)
                above_ground_wall_ins_depth = 999
            # if "Overall Effective R-Value", make sure value magnitude makes sense
            elif above_ground_wall_input_method == "Overall Effective R-Value":
                wall_R_lo = 3.5
                wall_R_hi = 60
                above_ground_wall_R_value = validate(wallRvalue_fieldname, dictionary[wallRvalue_fieldname], "num_between", wall_R_lo, wall_R_hi, dummy_list)
                above_ground_wall_con = validate(wallCon_fieldname, "Wall with Overall Effective R-Value", "list", dummy_int, dummy_int, above_ground_wall_list)
                if above_ground_wall_R_value <= 7:
                    above_ground_wall_ins_depth = 0.0100374650*above_ground_wall_R_value - 0.0282398722
                elif above_ground_wall_R_value <= 15:
                    above_ground_wall_ins_depth = 0.0099181735*above_ground_wall_R_value - 0.0271154261
                elif above_ground_wall_R_value <= 30:
                    above_ground_wall_ins_depth = 0.0099956190*above_ground_wall_R_value - 0.0266703825
                else:
                    above_ground_wall_ins_depth = 0.0098995937*above_ground_wall_R_value - 0.0226454174
            else:
                print(str(wallInputMethod_fieldname) + " cannot be blank and must be set to either Pre-Defined Construction OR Overall Effective R-Value.")
                return True

            #... ceiling and roof construction
            # get ceiling insulation input method, either "Pre-Defined Construction" or "Ceiling Overall Effective R-Value (Assumes Simple Roof)"
            ceiling_input_method = dictionary[ceilingInputMethod_fieldname]
            ceiling_and_roof_con_list = ceiling_and_roof_con_dict.keys()
            if ceiling_input_method == "Pre-Defined Construction":
                ceiling_and_roof_con = validate(ceilingCon_fieldname, dictionary[ceilingCon_fieldname], "list", dummy_int, dummy_int, ceiling_and_roof_con_list)
                ceiling_ins_depth = 999
            elif ceiling_input_method == "Ceiling Overall Effective R-Value (Assumes Uninsulated Roof)":
                ceiling_R_lo = 2.0
                ceiling_R_hi = 120
                ceiling_R_value = validate(ceilingRvalue_fieldname, dictionary[ceilingRvalue_fieldname], "num_between", ceiling_R_lo, ceiling_R_hi, dummy_list)
                ceiling_and_roof_con = validate(ceilingCon_fieldname, "Attic w Overall Effective R-Value", "list", dummy_int, dummy_int, ceiling_and_roof_con_list)
                if ceiling_R_value <= 7:
                    ceiling_ins_depth = 0.0109882982*ceiling_R_value - 0.0224857088
                elif ceiling_R_value <= 15:
                    ceiling_ins_depth = 0.0109882982*ceiling_R_value - 0.0224857088
                elif ceiling_R_value <= 30:
                    ceiling_ins_depth = 0.0107985849*ceiling_R_value - 0.0192404814
                else:
                    ceiling_ins_depth = 0.0107985849*ceiling_R_value - 0.0192404814
            else:
                print(str(ceilingInputMethod_fieldname) + " cannot be blank and must be set to either Pre-Defined Construction OR Ceiling Overall Effective R-Value (Assumes Simple Roof).")
                return True

            #... foundation and floor construction
            floor_input_method = dictionary[floorInputMethod_fieldname]
            foundation_list = foundation_and_floor_dict.keys()
            if floor_input_method == "Pre-Defined Construction":
                foundation_and_floor_con = str(dictionary[floorCon_fieldname])
                foundation_and_floor_con = validate(floorCon_fieldname, dictionary[floorCon_fieldname], "list" , dummy_int, dummy_int, foundation_list)
                floor_ins_depth = 0.0001
                slab_perim_ins_depth = 999
                under_slab_ins_depth = 999
                thermal_break_depth = 999
                found_wall_ins_depth = 999
            elif floor_input_method == "Foundation Type with Effective R-Values":
                # Get floor and foundation custom inputs from user
                found_type_list = ["Vented Crawlspace","Slab","Heated Basement","Unheated Basement"]
                user_found_type = validate(foundType_fieldname, dictionary[foundType_fieldname], "list", dummy_int, dummy_int, found_type_list)
                floor_effective_Rvalue = validate(floorRvalue_fieldname, dictionary[floorRvalue_fieldname], "any_num", dummy_int, dummy_int, dummy_list)
                slab_perimeter_Rvalue = validate(slabPerimRvalue_fieldname, dictionary[slabPerimRvalue_fieldname], "any_num", dummy_int, dummy_int, dummy_list)
                under_slab_Rvalue = validate(slabUnderRvalue_fieldname, dictionary[slabUnderRvalue_fieldname], "any_num", dummy_int, dummy_int, dummy_list)
                slab_thermalbreak_Rvalue = validate(slabTBvalue_fieldname, dictionary[slabTBvalue_fieldname], "any_num", dummy_int, dummy_int, dummy_list)
                foundation_wall_Rvalue = validate(foundWallRvalue_fieldname, dictionary[foundWallRvalue_fieldname], "any_num", dummy_int, dummy_int, dummy_list)
                # Pass these inputs to a function that can determine which general foundation construction to use
                foundation_identifier = getFoundationIdentifier(user_found_type, floor_effective_Rvalue, slab_perimeter_Rvalue, under_slab_Rvalue, slab_thermalbreak_Rvalue, foundation_wall_Rvalue)
                # Determine floor insulation depth
                if floor_effective_Rvalue == 0:
                    floor_ins_depth = 0.0001
                elif floor_effective_Rvalue <= 7:
                    floor_ins_depth = 0.0088309555*floor_effective_Rvalue - 0.0217952236
                elif floor_effective_Rvalue <= 15:
                    floor_ins_depth = 0.0088309555*floor_effective_Rvalue - 0.0217952236
                elif floor_effective_Rvalue <= 30:
                    floor_ins_depth = 0.0088309555*floor_effective_Rvalue - 0.0217952236
                else:
                    floor_ins_depth = 0.0088309555*floor_effective_Rvalue - 0.0217952236
  
                # Determine slab and foundation wall insulation depths
                slab_perim_ins_depth = max(0.0051073508 * slab_perimeter_Rvalue - 0.0000009870, 0.0001)
                under_slab_ins_depth =  max(0.0051073508 * under_slab_Rvalue - 0.0000009870, 0.0001)
                thermal_break_depth =  max(0.0051073508 * slab_thermalbreak_Rvalue - 0.0000009870, 0.0001)
                found_wall_ins_depth =  max(0.0051073508 * foundation_wall_Rvalue - 0.0000009870, 0.0001)
                
                foundation_and_floor_con = validate(floorCon_fieldname, foundation_identifier, "list" , dummy_int, dummy_int, foundation_list)
            else:
                print(str(floorInputMethod_fieldname) + " cannot be blank and must be set to either Pre-Defined Construction OR Foundation Type with Effective R-Values.")
                return True

            # Establish foundation type
            other_found_chars = {}
            other_found_chars["foundation_type"] = foundation_and_floor_dict[foundation_and_floor_con]["foundation_type"]
            foundation_type = other_found_chars["foundation_type"]

            # Establish if foundation is slab or heated basement, if using regression-based infiltration estimate
            if foundation_type == "Slab" or foundation_type == "Heated Basement":
                hasSlabOrHtdBsmnt = 1
            else:
                hasSlabOrHtdBsmnt = 0

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
            window_shades = validate(windowShade_fieldname, dictionary[windowShade_fieldname], "list", dummy_int, dummy_int, window_shades_list)
            # Set window construction
            win_construction = "Exterior Window"

            #... window to wall ratios
            wtw_lo = 0.0001
            wtw_hi = 0.99
            wtw_ratio_front = validate(wtwFront_fieldname, dictionary[wtwFront_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)
            wtw_ratio_back = validate(wtwBack_fieldname, dictionary[wtwBack_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)
            wtw_ratio_left = validate(wtwLeft_fieldname, dictionary[wtwLeft_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)
            wtw_ratio_right = validate(wtwRight_fieldname, dictionary[wtwRight_fieldname], "num_between", wtw_lo, wtw_hi, dummy_list)

            #... infiltration
            infiltration = validate(infiltration_fieldname, dictionary[infiltration_fieldname], "num_not_zero", dummy_int, dummy_int, dummy_list)

            #... primary HVAC type
            hvac_type_list = hvac_dict.keys()
            hvac_type = validate(primaryHVAC_fieldname, dictionary[primaryHVAC_fieldname], "list", dummy_int, dummy_int, hvac_type_list)

            #... HVAC sizing method
            hvacSizingMethod_list = ["Manual", "Autosize"]
            hvacSizingMethod = validate(hvacSizingMethod_fieldname, dictionary[hvacSizingMethod_fieldname], "list", dummy_int, dummy_int, hvacSizingMethod_list)

            #... get HVAC characteristics for primary HVAC type
            CentralOrZonal = hvac_dict[hvac_type]["CentralOrZonal"]
            ZoneEquipment1ObjectType = hvac_dict[hvac_type]["ZoneEquipment1ObjectType"]
            ZoneEquipment1Name = hvac_dict[hvac_type]["ZoneEquipment1Name"]
            ZoneEquipment1CoolingSequence = hvac_dict[hvac_type]["ZoneEquipment1CoolingSequence"]
            ZoneEquipment1HeatingSequence = hvac_dict[hvac_type]["ZoneEquipment1HeatingSequence"]
            ZoneEquipment2ObjectType = hvac_dict[hvac_type]["ZoneEquipment2ObjectType"]
            ZoneEquipment2Name = hvac_dict[hvac_type]["ZoneEquipment2Name"]
            ZoneEquipment2CoolingSequence = hvac_dict[hvac_type]["ZoneEquipment2CoolingSequence"]
            ZoneEquipment2HeatingSequence = hvac_dict[hvac_type]["ZoneEquipment2HeatingSequence"]
            ZoneAirInletNodeName = hvac_dict[hvac_type]["ZoneAirInletNodeName"]
            ZoneAirExhaustNodeName = hvac_dict[hvac_type]["ZoneAirExhaustNodeName"]
            ZoneReturnAirNodeName = hvac_dict[hvac_type]["ZoneReturnAirNodeName"]
            heatCoilFuelType  = hvac_dict[hvac_type]["heatCoilFuelType"]

            unitaryTextFile = os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, hvac_dict[hvac_type]["unitaryTextFile"])
            airDistUnitTextFile = os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, hvac_dict[hvac_type]["airDistUnitTextFile"])
            heatCoilTextFile = os.path.join(set_dir, building_block_dir, hvac_coil_dir, hvac_dict[hvac_type]["heatCoilTextFile"])
            
            if hvac_dict[hvac_type]["coolCoilTextFile"] != "No":
                coolCoilTextFile = os.path.join(set_dir, building_block_dir, hvac_coil_dir, hvac_dict[hvac_type]["coolCoilTextFile"])
            else:
                coolCoilTextFile = "No"
            fanTextFile = os.path.join(set_dir, building_block_dir, hvac_fan_dir, hvac_dict[hvac_type]["fanTextFile"])
            
            AirLoopHVAC_HeatingCoil_ObjectType = hvac_dict[hvac_type]["AirLoopHVAC_HeatingCoil_ObjectType"]
            AirLoopHVAC_HeatingCoil_Name = hvac_dict[hvac_type]["AirLoopHVAC_HeatingCoil_Name"]
            AirLoopHVAC_CoolingCoil_ObjectType = hvac_dict[hvac_type]["AirLoopHVAC_CoolingCoil_ObjectType"]
            AirLoopHVAC_CoolingCoil_Name = hvac_dict[hvac_type]["AirLoopHVAC_CoolingCoil_Name"]
            AirLoopHVAC_Unitary_ObjectType = hvac_dict[hvac_type]["AirLoopHVAC_Unitary_ObjectType"]
            AirLoopHVAC_Unitary_ObjectName = hvac_dict[hvac_type]["AirLoopHVAC_Unitary_ObjectName"]
            fan_name = hvac_dict[hvac_type]["fan_name"]
            heating_speeds = hvac_dict[hvac_type]["heating_speeds"]
            cooling_speeds = hvac_dict[hvac_type]["cooling_speeds"]
            fan_CFMperTon_max = hvac_dict[hvac_type]["fan_CFMperTon_max"]
            fan_CFMmult_spd_1 = hvac_dict[hvac_type]["fan_CFMmult_spd_1"]
            fan_CFMmult_spd_2 = hvac_dict[hvac_type]["fan_CFMmult_spd_2"]
            fan_CFMmult_spd_3 = hvac_dict[hvac_type]["fan_CFMmult_spd_3"]
            fan_CFMmult_spd_4 = hvac_dict[hvac_type]["fan_CFMmult_spd_4"]
            capacitymult_spd_1 = hvac_dict[hvac_type]["capacitymult_spd_1"]
            capacitymult_spd_2 = hvac_dict[hvac_type]["capacitymult_spd_2"]
            capacitymult_spd_3 = hvac_dict[hvac_type]["capacitymult_spd_3"]
            capacitymult_spd_4 = hvac_dict[hvac_type]["capacitymult_spd_4"]
            
            #... heating capacity units
            primaryHVAC_capacity_units_list = ["kBtu/h", "kW", "ton"]
            if hvacSizingMethod == "Manual":
                primaryHtg_capacity_units = validate(primaryHtgCapacityUnits_fieldname, dictionary[primaryHtgCapacityUnits_fieldname], "list", dummy_int, dummy_int, primaryHVAC_capacity_units_list)

            #... primary heating capacity
            if hvacSizingMethod == "Manual":
                primary_heating_capacity = validate(primaryHtgCapacity_fieldname, dictionary[primaryHtgCapacity_fieldname], "num_not_zero", dummy_int, dummy_int, dummy_list)
                primary_heating_capacity = convert_capacity(primaryHtg_capacity_units, primary_heating_capacity)
            else:
                primary_heating_capacity = "Autosize"

            #... cooling capacity and capacity units
            if AirLoopHVAC_Unitary_ObjectName == "SS Heat Pump" or AirLoopHVAC_Unitary_ObjectName == "DS Heat Pump" or AirLoopHVAC_Unitary_ObjectName == "MS Heat Pump" \
            or coolCoilTextFile != "No":
                if hvacSizingMethod == "Manual":
                    primaryClg_capacity_units = validate(primaryClgCapacityUnits_fieldname, dictionary[primaryClgCapacityUnits_fieldname], "list", dummy_int, dummy_int, primaryHVAC_capacity_units_list)
                    primary_cooling_capacity = validate(primaryClgCapacity_fieldname, dictionary[primaryClgCapacity_fieldname], "num_not_zero", dummy_int, dummy_int, dummy_list)
                    primary_cooling_capacity = convert_capacity(primaryClg_capacity_units, primary_cooling_capacity)
                else:
                    primary_cooling_capacity = "Autosize"

                #... cooling setpoint schedule
                clg_stpt_sch = validate(clgSched_fieldname, dictionary[clgSched_fieldname], "list", dummy_int, dummy_int, sched_validation_list)
            else:
                primary_cooling_capacity = 0
                clg_stpt_sch = validate(clgSched_fieldname, "Cool_EZ_Sch_1", "list", dummy_int, dummy_int, sched_validation_list)

            #... heat pump specific inputs
            if AirLoopHVAC_Unitary_ObjectName == "SS Heat Pump" or AirLoopHVAC_Unitary_ObjectName == "DS Heat Pump" or AirLoopHVAC_Unitary_ObjectName == "MS Heat Pump" \
            and CentralOrZonal == "Central":
                #... ASHP backup heat type
                hp_supp_heat_type_list = ["Electric", "Gas"]
                hp_supp_heat_type = validate(hpBackupType_fieldname, dictionary[hpBackupType_fieldname], "list", dummy_int, dummy_int, hp_supp_heat_type_list)
                if hvacSizingMethod == "Manual":
                    #... ASHP backup heat capacity units
                    ASHPbackup_capacity_units_list = ["kBtu/h", "kW"]
                    ASHPbackup_capacity_units = validate(hpBackupCapacityUnits_fieldname, dictionary[hpBackupCapacityUnits_fieldname], "list", dummy_int, dummy_int, ASHPbackup_capacity_units_list)
                    #... ASHP backup heat capacity
                    hp_supp_heat_capacity = convert_capacity(ASHPbackup_capacity_units, validate(hpBackupCapacity_fieldname, dictionary[hpBackupCapacity_fieldname], "num_not_zero", dummy_int, dummy_int, dummy_list))
                else:
                    hp_supp_heat_capacity = "Autosize"
                
                #... backup heat lockout
                hp_max_resistance_temp = validate(hpBackupLockout_fieldname, convert_degF_to_degC(dictionary[hpBackupLockout_fieldname]), "any_num", dummy_int, dummy_int, dummy_list)
                #... compressor lockout
                hp_min_compressor_temp = validate(hpCompressorLockout_fieldname, convert_degF_to_degC(dictionary[hpCompressorLockout_fieldname]), "any_num", dummy_int, dummy_int, dummy_list)
            else:
                hp_supp_heat_type = "No"
                hp_supp_heat_capacity = 0

            #... baseboard heating capacity
            if str(dictionary[backupBaseboardCapacity_fieldname]) == "nan" or hvacSizingMethod == "Manual":
                baseboard_heat_capacity = 0
            else:
                baseboard_heat_capacity = convert_capacity("kW", validate(backupBaseboardCapacity_fieldname, dictionary[backupBaseboardCapacity_fieldname], "any_num", dummy_int, dummy_int, dummy_list))
            
            #... duct inputs
            if CentralOrZonal == "Central":
                #... duct leakage
                duct_leak_lo = 0.0001
                duct_leak_hi = 0.99
                supply_leak = validate(supplyLeakage_fieldname, dictionary[supplyLeakage_fieldname], "num_between", duct_leak_lo, duct_leak_hi, dummy_list)
                return_leak = validate(returnLeakage_fieldname, dictionary[returnLeakage_fieldname], "num_between", duct_leak_lo, duct_leak_hi, dummy_list)
                #... duct R-value
                supplyRvalue = validate(supplyRvalue_fieldname, dictionary[supplyRvalue_fieldname], "any_num", dummy_int, dummy_int, dummy_list)
                returnRvalue = validate(returnRvalue_fieldname, dictionary[returnRvalue_fieldname], "any_num", dummy_int, dummy_int, dummy_list)
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
            htg_stpt_sch = validate(htgSched_fieldname, dictionary[htgSched_fieldname], "list", dummy_int, dummy_int, sched_validation_list)

            #... gas furnace AFUE
            if AirLoopHVAC_HeatingCoil_Name == "Heating_Fuel_Main" or hp_supp_heat_type == "Gas":
                AFUE_lo = 0.5
                AFUE_hi = 0.99
                gas_furnace_AFUE = validate(AFUE_fieldname, dictionary[AFUE_fieldname], "num_between", AFUE_lo, AFUE_hi, dummy_list)
            
            #... water heater type
            water_heater_type_list = ["Electric Storage_50-gallon", "Gas Storage_50-gallon", "HPWH_50-gallon", "HPWH_80-gallon", "No"]
            water_heater_type = validate(dhwType_fieldname, dictionary[dhwType_fieldname], "list", dummy_int, dummy_int, water_heater_type_list)
            if water_heater_type == "HPWH_50-gallon":
                HPWH = 1
            else:
                HPWH = 0
            
            #... DHW setpoint schedule
            if water_heater_type != "No":
                dhw_stpt_sch = validate(dhwSched_fieldname, dictionary[dhwSched_fieldname], "list", dummy_int, dummy_int, sched_validation_list)
            else:
                dhw_stpt_sch = validate(dhwSched_fieldname, "DHW_EZ_Sch_1", "list", dummy_int, dummy_int, sched_validation_list)

            #... number of people
            people = validate(numOfPeople_fieldname, dictionary[numOfPeople_fieldname], "any_num", dummy_int, dummy_int, dummy_list)

            #... interior lighting power density
            interior_lpd = validate(intLPD_fieldname, convert_WperFt2_to_WperM2(dictionary[intLPD_fieldname]), "any_num", dummy_int, dummy_int, dummy_list) #divide total lpd by plug lights and hardwired lights

            #... exterior lighting power
            exterior_lp = validate(extLP_fieldname, dictionary[extLP_fieldname], "any_num", dummy_int, dummy_int, dummy_list) #divide total lp by garage lights and exterior facade lights

            #... range type
            range_type_list = ["Electric", "Gas", "No"]
            range_type = validate(range_fieldname, dictionary[range_fieldname], "list", dummy_int, dummy_int, range_type_list)

            #... dryer type
            dryer_type_list = ["Electric", "Gas", "No"]
            dryer_type = validate(dryer_fieldname, dictionary[dryer_fieldname], "list", dummy_int, dummy_int, dryer_type_list)

            #... frig type
            frig_list = ["Yes", "No"]
            frig = validate(frig_fieldname, dictionary[frig_fieldname], "list", dummy_int, dummy_int, frig_list)

            #... clotheswasher type
            clotheswasher_list = ["Yes", "No"]
            clotheswasher = validate(cw_fieldname, dictionary[cw_fieldname], "list", dummy_int, dummy_int, clotheswasher_list)

            #... dishwasher type
            dishwasher_list = ["Yes", "No"]
            dishwasher = validate(dw_fieldname, dictionary[dw_fieldname], "list", dummy_int, dummy_int, dishwasher_list)

            #... miscellaneous electric power
            misc_elec = validate(miscElec_fieldname, dictionary[miscElec_fieldname], "any_num", dummy_int, dummy_int, dummy_list)

            if misc_elec != 0:
                #... miscellaneous electric power schedule
                misc_elec_sch = validate(miscElecShed_fieldname, dictionary[miscElecShed_fieldname], "list", dummy_int, dummy_int, sched_validation_list)

            #... miscellaneous gas power
            misc_gas = validate(miscGas_fieldname, convert_Btuh_to_W(dictionary[miscGas_fieldname]), "any_num", dummy_int, dummy_int, dummy_list)

            if misc_gas != 0:
                #... miscellaneous gas power schedule
                misc_gas_sch = validate(miscGasShed_fieldname, dictionary[miscGasShed_fieldname], "list", dummy_int, dummy_int, sched_validation_list)
            
        except:
            return True
        
        

        # Get wall construction layers
        wall_layers = []
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["exterior_wall_layer"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_1"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_2"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_3"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_4"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_5"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_6"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_7"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_8"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_9"])
        wall_layers.append(nonfoundation_wall_dict[above_ground_wall_con]["next_wall_layer_10"])
        #... find last "real" (non-empty) layer
        last_real_layer_num = findLastRealLayer(wall_layers)
        #... format layers with proper punctuation for EnergyPlus
        wall_layers = formatLayerList(last_real_layer_num, wall_layers)

        # Get ceiling construction layers
        ceiling_layers = []
        ceiling_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["exterior_ceiling_layer"])
        ceiling_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_ceiling_layer_1"])
        ceiling_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_ceiling_layer_2"])
        ceiling_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_ceiling_layer_3"])
        ceiling_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_ceiling_layer_4"])
        ceiling_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_ceiling_layer_5"])
        #... find last "real" (non-empty) layer
        last_real_layer_num = findLastRealLayer(ceiling_layers)
        #... format layers with proper punctuation for EnergyPlus
        ceiling_layers = formatLayerList(last_real_layer_num, ceiling_layers)

        # Get roof construction layers
        roof_layers = []
        roof_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["exterior_roof_layer"])
        roof_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_roof_layer_1"])
        roof_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_roof_layer_2"])
        roof_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_roof_layer_3"])
        roof_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_roof_layer_4"])
        roof_layers.append(ceiling_and_roof_con_dict[ceiling_and_roof_con]["next_roof_layer_5"])
        #... find last "real" (non-empty) layer
        last_real_layer_num = findLastRealLayer(roof_layers)
        #... format layers with proper punctuation for EnergyPlus
        roof_layers = formatLayerList(last_real_layer_num, roof_layers)

        # Get floor construction layers
        floor_layers = []
        floor_layers.append(foundation_and_floor_dict[foundation_and_floor_con]["exterior_floor_layer"])
        floor_layers.append(foundation_and_floor_dict[foundation_and_floor_con]["next_floor_layer_1"])
        floor_layers.append(foundation_and_floor_dict[foundation_and_floor_con]["next_floor_layer_2"])
        floor_layers.append(foundation_and_floor_dict[foundation_and_floor_con]["next_floor_layer_3"])
        floor_layers.append(foundation_and_floor_dict[foundation_and_floor_con]["next_floor_layer_4"])
        floor_layers.append(foundation_and_floor_dict[foundation_and_floor_con]["next_floor_layer_5"])
        #... find last "real" (non-empty) layer
        last_real_layer_num = findLastRealLayer(floor_layers)
        #... format layers with proper punctuation for EnergyPlus
        floor_layers = formatLayerList(last_real_layer_num, floor_layers)

        # Get other foundation characteristics
        other_found_chars["slab_perimeter_ins_name"] = foundation_and_floor_dict[foundation_and_floor_con]["slab_perimeter_ins_name"]
        other_found_chars["slab_perimeter_ins_width[ft]"] = foundation_and_floor_dict[foundation_and_floor_con]["slab_perimeter_ins_width[ft]"]
        other_found_chars["slab_thermalbreak_ins_name"] = foundation_and_floor_dict[foundation_and_floor_con]["slab_thermalbreak_ins_name"]
        other_found_chars["slab_thermalbreak_ins_depth[ft]"] = foundation_and_floor_dict[foundation_and_floor_con]["slab_thermalbreak_ins_depth[ft]"]
        other_found_chars["bsmnt_wall_ext_ins_name"] = foundation_and_floor_dict[foundation_and_floor_con]["bsmnt_wall_ext_ins_name"]
        other_found_chars["bsmnt_wall_ext_ins_depth[ft]"] = foundation_and_floor_dict[foundation_and_floor_con]["bsmnt_wall_ext_ins_depth[ft]"]

        # Get EnergyPlus assumptions for main foundation types
        foundation_assumptions = {}
        found_type = other_found_chars["foundation_type"]
        foundation_assumptions["foundation_surface"] = foundation_type_assumptions_dict[found_type]["foundation_surface"]
        foundation_assumptions["footer_ht_above_grade[ft]"] = foundation_type_assumptions_dict[found_type]["footer_ht_above_grade[ft]"]
        foundation_assumptions["footer_ht_below_slab[ft]"] = foundation_type_assumptions_dict[found_type]["footer_ht_below_slab[ft]"]
        foundation_assumptions["floor_main_outside_boundary_condition"] = foundation_type_assumptions_dict[found_type]["floor_main_outside_boundary_condition"]
        foundation_assumptions["floor_main_outside_boundary_condition_object"] = foundation_type_assumptions_dict[found_type]["floor_main_outside_boundary_condition_object"]
        foundation_assumptions["foundation_zone_name"] = foundation_type_assumptions_dict[found_type]["foundation_zone_name"]
        foundation_assumptions["foundationwall_ht_AG[ft]"] = foundation_type_assumptions_dict[found_type]["foundationwall_ht_AG[ft]"]
        foundation_assumptions["foundationwall_ht_BG[ft]"] = foundation_type_assumptions_dict[found_type]["foundationwall_ht_BG[ft]"]
        foundation_assumptions["returnduct_location"] = foundation_type_assumptions_dict[found_type]["returnduct_location"]

        # Set general foundation parameters based on foundation type
        foundation_surface = foundation_assumptions["foundation_surface"]
        wall_ht_above_grade = convert_ft_to_m(foundation_assumptions["footer_ht_above_grade[ft]"])
        wall_ht_below_slab = convert_ft_to_m(foundation_assumptions["footer_ht_below_slab[ft]"])
        floor_main_outside_boundary_condition = foundation_assumptions["floor_main_outside_boundary_condition"]
        floor_main_outside_boundary_condition_object = foundation_assumptions["floor_main_outside_boundary_condition_object"]
        foundation_zone_name = foundation_assumptions["foundation_zone_name"]
        foundationwall_ht_AG = round(convert_ft_to_m(float(foundation_assumptions["foundationwall_ht_AG[ft]"])),10)
        foundationwall_ht_AG_ft = foundation_assumptions["foundationwall_ht_AG[ft]"]
        foundationwall_ht_BG = -1 * round(convert_ft_to_m(float(foundation_assumptions["foundationwall_ht_BG[ft]"])),10)
        foundationwall_ht_BG_ft = foundation_assumptions["foundationwall_ht_BG[ft]"]
        if CentralOrZonal == "Central":
            returnduct_location = foundation_assumptions["returnduct_location"]
            supplyduct_location = "attic"
        else:
            returnduct_location = "living"
            supplyduct_location = "living"

        # Set foundation insulation based on specific foundation selection
        int_horiz_ins_mat_name = other_found_chars["slab_perimeter_ins_name"]
        int_horiz_ins_depth = convert_ft_to_m(0)
        int_horiz_ins_width = convert_ft_to_m(other_found_chars["slab_perimeter_ins_width[ft]"])
        int_vert_ins_mat_name = other_found_chars["slab_thermalbreak_ins_name"] 
        int_vert_ins_depth = convert_ft_to_m(other_found_chars["slab_thermalbreak_ins_depth[ft]"])
        ext_vert_ins_mat_name = other_found_chars["bsmnt_wall_ext_ins_name"]
        ext_vert_ins_depth = convert_ft_to_m(other_found_chars["bsmnt_wall_ext_ins_depth[ft]"])

        # Set geometry parameters that are needed to create geometry but not needed to be changed by user. All units in ft and converted to meters.
        origin_x = convert_ft_to_m(0) 
        origin_y = convert_ft_to_m(0)
        origin_z = convert_ft_to_m(0)
        number_of_stories = 1

        # Calculate intermediate geometry variables
        building_width = round(ratio_width_to_depth * math.sqrt(conditioned_footprint_area / ratio_width_to_depth), 10)
        building_depth = round(conditioned_footprint_area / building_width, 10)
        roof_ridge_depth = round(building_depth / 2, 10)
        roof_ht = (roof_pitch_value) * roof_ridge_depth
        avg_conditioned_envelope_ht = round(total_conditioned_volume / conditioned_footprint_area, 10)
        first_flr_ht_AG = round(foundationwall_ht_AG + avg_conditioned_envelope_ht, 10)
        top_flr_ht_AG = round(first_flr_ht_AG, 10)
        roof_ht_AG = round(top_flr_ht_AG + roof_ht, 10)
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
        if range_type == "No":
            range_t = ""
        else:
            range_file = range_type + ".txt"
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_rangetype_dir, range_file), 'r') as f:
                range_t = f.read()
        #... add dryer
        if dryer_type == "No":
            dryer_t = ""
        else:
            dryer_file = dryer_type + ".txt"
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_dryertype_dir, dryer_file), 'r') as f:
                dryer_t = f.read()
        #... add clotheswasher
        if clotheswasher == "No":
            clotheswasher_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_cw_file), 'r') as f:
                clotheswasher_t = f.read()
        #... add dishwasher
        if dishwasher == "No":
            dishwasher_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_dw_file), 'r') as f:
                dishwasher_t = f.read()
        #... add refrigerator
        if frig == "No":
            frig_t = ""
        else:
            with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_frig_file), 'r') as f:
                frig_t = f.read()
        #... add miscellaneous electric gains
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_miscElec_file), 'r') as f:
            misc_elec_t = f"{f.read()}".format(**locals())
        #... add miscellaneous gas gains
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_miscGas_file), 'r') as f:
            misc_gas_t = f"{f.read()}".format(**locals())
        #... add people
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_people_file), 'r') as f:
            people_t = f"{f.read()}".format(**locals())
        #... add lights
        with open(os.path.join(set_dir, building_block_dir, gains_main_dir, gains_lights_file), 'r') as f:
            lights_t = f"{f.read()}".format(**locals())

        # Constructions
        with open(os.path.join(set_dir, building_block_dir, building_block_constructions_file), 'r') as f:
            construction_t = f"{f.read()}".format(**locals())

        # Simulation Parameters
        with open(os.path.join(set_dir, building_block_dir, building_block_simParameters_file), 'r') as f:
            simparam_t = f"{f.read()}".format(**locals())

        # Performance Precision Tradeoffs
        if sim_type == "Test Run":
            with open(os.path.join(set_dir, building_block_dir, performanceprecision_dir, performanceprecision_highSpeed_file), 'r') as f:
                performanceprecision_t = f"{f.read()}".format(**locals())
        else:
            with open(os.path.join(set_dir, building_block_dir, performanceprecision_dir, performanceprecision_normal_file), 'r') as f:
                performanceprecision_t = f"{f.read()}".format(**locals())

        # Windows
        #... set U-value and SHGC
        with open(os.path.join(set_dir, building_block_dir, window_main_dir, window_main_simpleGlazingSys_file), 'r') as f:
            glazing_t = f"{f.read()}".format(**locals())
        #... set window construction (i.e. with or without blinds)
        window_con_file = window_shades + ".txt"
        with open(os.path.join(set_dir, building_block_dir, window_main_dir, window_blinds_dir, window_con_file), 'r') as f:
            win_construction_t = f.read()

        # Location & Climate
        # NOTE: THIS ISN'T CURRENTLY NEEDED OR USED, BECAUSE THE WEATHER FILES ARE USED FOR DESIGN DAYS.
        #... also includes design day
        # location_design_day_file = location_pull + ".txt"
        # with open(os.path.join(set_dir, building_block_dir, location_and_climate_dir, location_design_day_file), 'r') as f: # our location & climate dictionary in action
        #     locations_t = f.read()

        # Materials
        with open(os.path.join(set_dir, building_block_dir, building_block_materials_file), 'r') as f:
            mat_t = f"{f.read()}".format(**locals())

        # Performance Curves
        with open(os.path.join(set_dir, building_block_dir, building_block_performanceCurve_file), 'r') as f:
            perf_t = f.read()

        # Schedules
        htg_sch_num = sched_list.index(htg_stpt_sch) + 1
        clg_sch_num = sched_list.index(clg_stpt_sch) + 1
        dhw_sch_num = sched_list.index(dhw_stpt_sch) + 1

        #... misc electric gains
        if misc_elec != 0 and misc_elec_sch != str(PNNL_default[0]):
            try:
                misc_elec_sch_num = sched_list.index(misc_elec_sch) + 1
                with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_elec_gains_dir, schedule_elec_gains_custom_file), 'r') as f:
                    misc_elec_sched_t = f"{f.read()}".format(**locals())
            except:
                print("\n*** ERROR: REEDR could not find schedule for miscellaneous electric gains. Please ensure this input is valid. \n")
                return True
        else:
            with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_elec_gains_dir, schedule_elec_gains_default_file), 'r') as f:
                    misc_elec_sched_t = f"{f.read()}".format(**locals())
        #... misc gas gains
        if misc_gas != 0 and misc_gas_sch != str(PNNL_default[0]):
            try:
                misc_gas_sch_num = sched_list.index(misc_gas_sch) + 1
                with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_gas_gains_dir, schedule_gas_gains_custom_file), 'r') as f:
                    misc_gas_sched_t = f"{f.read()}".format(**locals())
            except:
                print("\n*** ERROR: REEDR could not find schedule for miscellaneous gas gains. Please ensure this input is valid. \n")
                return True
        else:
            with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_gas_gains_dir, schedule_gas_gains_default_file), 'r') as f:
                    misc_gas_sched_t = f"{f.read()}".format(**locals())

        #... most other schedules
        with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_file), 'r') as f:
            sched_t = f"{f.read()}".format(**locals())

        # Add Kiva foundation inputs
        with open(os.path.join(set_dir, building_block_dir, building_block_foundation_file), 'r') as f:
            foundation_type_t = f"{f.read()}".format(**locals())

        ### --- Adding building geometry --- ###
        #...insert geometry rules
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_globalRules_file), 'r') as f:
            geom_rules_t = f.read()
        #...insert internal mass
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_internalMass_file), 'r') as f:
            internal_mass_t = f.read()
        #...insert aspects of building geometry common to all buildings (e.g. main walls, ceiling, roof)
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, geometry_envelope_main_file), 'r') as f:
            geom_main_envelope_t = f"{f.read()}".format(**locals())
        #...insert window geometry
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_window_dir, geometry_window_file), 'r') as f:
            geom_main_windows_t = f"{f.read()}".format(**locals())
        #...insert living zone geometry in all buildings
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, geometry_living_file), 'r') as f:
            living_zone_t = f.read()
        #...insert attic zone geometry in all buildings
        with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, geometry_attic_file), 'r') as f:
            attic_zone_t = f.read()
        #...if foundation type is slab, add necessary slab geometry and set non-slab geometry files as empty strings
        if foundation_type == "Slab":
            geom_nonslab_adder_t = ""
            unheatedbsmt_zone_t = ""
            crawlspace_zone_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, geometry_envelope_nonhtdbsmntAdder_file), 'r') as f:
                geom_nonhtdbsmt_adder_t = f"{f.read()}".format(**locals())
        #...if foundation type is heated basement, add necessary heated basement geometry and set non-htd basement geometry files as empty strings
        elif foundation_type == "Heated Basement":
            unheatedbsmt_zone_t = ""
            crawlspace_zone_t = ""
            geom_nonhtdbsmt_adder_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, geometry_envelope_nonslabAdder_file), 'r') as f:
                geom_nonslab_adder_t = f"{f.read()}".format(**locals())
        #...if foundation type is a vented crawl, add necessary crawl geometry and set non-crawl geometry files as empty strings
        elif foundation_type == "Vented Crawlspace":
            unheatedbsmt_zone_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, geometry_crawlspace_file), 'r') as f:
                crawlspace_zone_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, geometry_envelope_nonslabAdder_file), 'r') as f:
                geom_nonslab_adder_t = f"{f.read()}".format(**locals())
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, geometry_envelope_nonhtdbsmntAdder_file), 'r') as f:
                geom_nonhtdbsmt_adder_t = f"{f.read()}".format(**locals()) 
        else: # foundation type is unheated basement
            crawlspace_zone_t = ""
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_zone_dir, geometry_unhtdbsmnt_file), 'r') as f:
                unheatedbsmt_zone_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, geometry_envelope_nonslabAdder_file), 'r') as f:
                geom_nonslab_adder_t = f"{f.read()}".format(**locals())
            with open(os.path.join(set_dir, building_block_dir, geometry_main_dir, geometry_envelope_dir, geometry_envelope_nonhtdbsmntAdder_file), 'r') as f:
                geom_nonhtdbsmt_adder_t = f"{f.read()}".format(**locals())
        
        DesignSpecificationOutdoorAirObjectName = ""

        # Assume effectively no integrated supplemental backup heat for a DHP
        if AirLoopHVAC_Unitary_ObjectType == "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed" and CentralOrZonal == "Zonal":
            hp_max_resistance_temp = convert_degF_to_degC(68)
            hp_min_compressor_temp = convert_degF_to_degC(-20)

        # Set capacity to use for sizing fans. If heating only, use heating capacity. If heating and cooling, use average capacity.
        if hvacSizingMethod == "Manual":
            if AirLoopHVAC_Unitary_ObjectName == "SS Heat Pump" or AirLoopHVAC_Unitary_ObjectName == "DS Heat Pump" or AirLoopHVAC_Unitary_ObjectName == "MS Heat Pump" \
                or coolCoilTextFile != "No":

                sizing_capacity = convert_W_to_ton((primary_heating_capacity + primary_cooling_capacity)/2)
            else:
                sizing_capacity = convert_W_to_ton(primary_heating_capacity)

        # Set max fan speed using the proper user inputted total HVAC capacity
        if hvacSizingMethod == "Manual":
            fan_m3PerSec_max = convert_CFM_to_m3PerSec(fan_CFMperTon_max * sizing_capacity)
        
        # Set fan speeds and capacities using characteristics from HVAC dictionary and user selected HVAC type.
        # Variable speed equipment is modeled using four speeds.
        if hvacSizingMethod == "Manual":
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
        else:
            fan_m3PerSec_spd_1 = "Autosize"
            fan_m3PerSec_spd_2 = "Autosize"
            fan_m3PerSec_spd_3 = "Autosize"
            fan_m3PerSec_spd_4 = "Autosize"
            htg_capacity_spd_1 = "Autosize"
            htg_capacity_spd_2 = "Autosize"
            htg_capacity_spd_3 = "Autosize"
            htg_capacity_spd_4 = "Autosize"
            clg_capacity_spd_1 = "Autosize"
            clg_capacity_spd_2 = "Autosize"
            clg_capacity_spd_3 = "Autosize"
            clg_capacity_spd_4 = "Autosize"

            fan_max_flow_allowed = "Autosize"

        # Add baseboard capacity if defined, and properly handle assingment of HPWH
        if baseboard_heat_capacity != 0 and HPWH == 0:

            ZoneEquipment3ObjectType = "!-"
            ZoneEquipment3Name = "!-"
            ZoneEquipment3CoolingSequence = "!-"
            ZoneEquipment3HeatingSequence = "!-"
            
            ZoneEquipment2ObjectType = "ZoneHVAC:Baseboard:Convective:Electric"
            ZoneEquipment2Name = "BaseboardElectric"
            ZoneEquipment2CoolingSequence = "2"
            ZoneEquipment2HeatingSequence = "2"
            with open(os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'BaseboardHeat.txt'), 'r') as f:
                baseboard_t = f"{f.read()}".format(**locals())
            
        elif baseboard_heat_capacity != 0 and HPWH == 1:
            
            ZoneEquipment3ObjectType = "ZoneHVAC:Baseboard:Convective:Electric"
            ZoneEquipment3Name = "BaseboardElectric"
            ZoneEquipment3CoolingSequence = "3"
            ZoneEquipment3HeatingSequence = "3"
            with open(os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'BaseboardHeat.txt'), 'r') as f:
                baseboard_t = f"{f.read()}".format(**locals())

            ZoneEquipment2ObjectType = ZoneEquipment1ObjectType
            ZoneEquipment2Name = ZoneEquipment1Name
            ZoneEquipment2CoolingSequence = 2
            ZoneEquipment2HeatingSequence = 2

            ZoneEquipment1ObjectType = "WaterHeater:HeatPump:WrappedCondenser"
            ZoneEquipment1Name = "Water Heater"
            ZoneEquipment1CoolingSequence = 1
            ZoneEquipment1HeatingSequence = 1

            ZoneAirInletNodeName = "Zone Inlet Nodes"
            ZoneAirExhaustNodeName = "Zone Exhaust Node"

        elif baseboard_heat_capacity == 0 and HPWH == 1:

            baseboard_t = ""

            ZoneEquipment3ObjectType = "!-"
            ZoneEquipment3Name = "!-"
            ZoneEquipment3CoolingSequence = "!-"
            ZoneEquipment3HeatingSequence = "!-"

            ZoneEquipment2ObjectType = ZoneEquipment1ObjectType
            ZoneEquipment2Name = ZoneEquipment1Name
            ZoneEquipment2CoolingSequence = 2
            ZoneEquipment2HeatingSequence = 2

            ZoneEquipment1ObjectType = "WaterHeater:HeatPump:WrappedCondenser"
            ZoneEquipment1Name = "Water Heater"
            ZoneEquipment1CoolingSequence = 1
            ZoneEquipment1HeatingSequence = 1

            ZoneAirInletNodeName = "Zone Inlet Nodes"
            ZoneAirExhaustNodeName = "Zone Exhaust Node"

        else:

            baseboard_t = ""

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
        if AirLoopHVAC_CoolingCoil_ObjectType == "No":
            airloop_main_fan_coil_outlet_node = "Heating Coil Air Inlet Node"
            AFN_main_fan_coil_outlet_node = "HeatingInletNode"
            AFN_nodes_coolingcoiladder_t = ""
            AFN_linkage_coolingcoiladder_t = ""
        else:
            airloop_main_fan_coil_outlet_node = "Cooling Coil Air Inlet Node"
            AFN_main_fan_coil_outlet_node = "FanOutletNode"
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_node_dir, hvac_afn_node_adder_file), 'r') as f:
                AFN_nodes_coolingcoiladder_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_linkage_dir, hvac_afn_linkage_adder_file), 'r') as f:
                AFN_linkage_coolingcoiladder_t = f"{f.read()}".format(**locals())

        # Estimate effective leakage areas (ELAs), used to represent building infiltration, in AFN model
        infiltrationInACH50 = infiltration
        if foundation_type == "Heated Basement":
            infiltrationVolume_ft3 = conditioned_footprint_area_ft2 * avgHtPerStory_ft2 * avgStories + \
                                    (foundationwall_ht_AG_ft + foundationwall_ht_BG_ft) * conditioned_footprint_area_ft2
        else:
            infiltrationVolume_ft3 = conditioned_footprint_area_ft2 * avgHtPerStory_ft2 * avgStories
     
        infiltrationInCFM50 = infiltrationInACH50/60 * infiltrationVolume_ft3
        infiltrationInM3PerSec50Pa = infiltrationInCFM50 * 0.00047194745 #convert CFM to m^3/s
        infiltrationInM3PerSec4Pa = infiltrationInM3PerSec50Pa * (4/50)**0.65 #convert to airflow at 4Pa
        density_air = 1.205 # at sea level, 20 degrees C
        ref_pressure = 4 # reference pressure in Pa
        Cd = 1 # discharge coefficient
        ELA_total_4Pa_m2 = infiltrationInM3PerSec4Pa * math.sqrt(density_air/(2*ref_pressure))/Cd

        ELA_wall_frontback = ELA_total_4Pa_m2 * 1/4/2
        ELA_wall_leftright = ELA_total_4Pa_m2 * 1/4/2
        ELA_ceiling = ELA_total_4Pa_m2 * 1/2
        ELA_floor = 0.00001

        total_envelope_height = dictionary[stories_fieldname] * dictionary[heightPerStory_fieldname]
        
        adjust = []
        adjust = estimateInfiltrationAdjustment(foundation_type, infiltrationInACH50, dictionary[footprint_fieldname], total_envelope_height, \
            living_infiltration_coeff_dict, attic_infiltration_coeff_dict, crawl_infiltration_coeff_dict)

        attic_adjust = adjust[1]
        crawl_adjust = adjust[2]
        
        roof_hypotenuse = math.sqrt(roof_ht**2 + (building_depth/2)**2)
        attic_wall_area = 2*(0.5*building_depth*roof_ht) + 2*(roof_hypotenuse*building_width)
        ELA_attic = attic_adjust * attic_wall_area * 0.00010812648958345

        crawl_wall_area = 2*(abs(foundationwall_ht_AG) + abs(foundationwall_ht_BG))*building_depth + 2*(abs(foundationwall_ht_AG) + abs(foundationwall_ht_BG))*building_width
        ELA_crawl = crawl_adjust * crawl_wall_area * 0.00010812648958345
        
        ### --- Add Air Flow Network (AFN) and airloop. Currently all HVAC systems are modeled with ducts. "Ductless" systems are modeled with "perfect" ducts. --- ### 
        AFN_control = "MultizoneWithDistribution"
        # The following text files are added for all building models
        #...insert system sizing block
        with open(os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_sysSizing_file), 'r') as f:
            system_sizing_t = f.read()
        #...insert air loop
        with open(os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_file), 'r') as f:
            airloop_t = f"{f.read()}".format(**locals())
        #...insert AFN nodes common to all buildings
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_node_dir, hvac_afn_node_main_file), 'r') as f:
            AFN_nodes_main_t = f.read()
        #...insert AFN linkages common to all buildings
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_linkage_dir, hvac_afn_linkage_main_file), 'r') as f:
            AFN_linkage_main_t = f"{f.read()}".format(**locals()) 
        #...insert AFN simulation control
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_simcontrol_file), 'r') as f:
            AFN_sim_control_t = f"{f.read()}".format(**locals())
        #...insert AFN zones common to all buildings (i.e., main, attic)
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_zone_dir, hvac_afn_zone_main_file), 'r') as f:
            AFN_main_zones_t = f.read()
        #...insert AFN surface leakage
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_leakage_dir, hvac_afn_leakage_main_file), 'r') as f:
            AFN_main_leakage_t = f"{f.read()}".format(**locals())
        #...insert AFN surfaces common to all geometries
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_surface_dir, hvac_afn_surface_main_file), 'r') as f:
            AFN_main_surfaces_t = f.read()
        
        # Insert AFN "adders" for certain foundation types
        if foundation_type == "Slab" or foundation_type == "Heated Basement":
            AFN_crawl_zone_t = ""
            AFN_unheatedbsmt_zone_t = ""
            AFN_crawl_unheatedbsmt_leakage_adder_t = ""
            AFN_crawl_unheatedbsmt_surface_adder_t = ""
        elif foundation_type == "Vented Crawlspace":
            AFN_unheatedbsmt_zone_t = ""
            #...add a crawlspace AFN zone
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_zone_dir, hvac_afn_zone_crawl_adder_file), 'r') as f:
                AFN_crawl_zone_t = f.read()
            #...add surface leakage for crawlspace walls
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_leakage_dir, hvac_afn_leakage_adder_file), 'r') as f:
                AFN_crawl_unheatedbsmt_leakage_adder_t = f"{f.read()}".format(**locals())
            #...add crawlspace surfaces
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_surface_dir, hvac_afn_surface_adder_file), 'r') as f:
                AFN_crawl_unheatedbsmt_surface_adder_t = f.read()

        else: # foundation type is unheated basement
            AFN_crawl_zone_t = ""
            #...add an unheated basement zone
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_zone_dir, hvac_afn_zone_unhtdbsmt_adder_file), 'r') as f:
                AFN_unheatedbsmt_zone_t = f.read()
            #...add surface leakage for basement walls
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_leakage_dir, hvac_afn_leakage_adder_file), 'r') as f:
                AFN_crawl_unheatedbsmt_leakage_adder_t = f"{f.read()}".format(**locals())
            #...add AFN surfaces for basement walls
            with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_surface_dir, hvac_afn_surface_adder_file), 'r') as f:
                AFN_crawl_unheatedbsmt_surface_adder_t = f.read()

        if CentralOrZonal == "Central":
            maintrunk_duct_length = 2 # units are meters
            zonesupply_duct_length = 15
            zonereturn_duct_length = 8
            mainreturn_duct_length = 1

            supply_duct_Ufactor = supplyUvalue # units are W/m2-K
            return_duct_Ufactor = returnUvalue
        elif CentralOrZonal == "Zonal":
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
        with open(os.path.join(set_dir, building_block_dir, hvac_afn_main_dir, hvac_afn_ducts_file), 'r') as f:
            AFN_ducts_t = f"{f.read()}".format(**locals())
        #  Add a theromstat (T-stat)
        with open(os.path.join(set_dir, building_block_dir, hvac_tstat_dir, hvac_tstat_file), 'r') as f:
            thermostat_t = f"{f.read()}".format(**locals())
        # Add zone sizing
        with open(os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_zoneSizing_file), 'r') as f:
            zone_sizing_t = f"{f.read()}".format(**locals())
        # Add zone equipment list
        with open(os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_equipList_file), 'r') as f:
            zone_equip_list_t = f"{f.read()}".format(**locals())
        # Add HVAC equipment text file 1, which is typically the unitary HVAC text file
        with open(unitaryTextFile, 'r') as f:
            HVAC_equip_1_t = f"{f.read()}".format(**locals())
        # Add HVAC equipment text file 2, which is typically the air distribution unit
        if airDistUnitTextFile == "No":
            HVAC_equip_2_t = ""
        else:
            with open(airDistUnitTextFile, 'r') as f:
                HVAC_equip_2_t = f"{f.read()}".format(**locals())
        # Add heating coil text file
        if heatCoilTextFile == "No":
            heating_coil_t = ""
        else:
            with open(heatCoilTextFile, 'r') as f:
                heating_coil_t = f"{f.read()}".format(**locals())
        # Add cooling coil text file
        if coolCoilTextFile == "No":    
            cooling_coil_t = ""
        else:
            with open(coolCoilTextFile, 'r') as f:
                cooling_coil_t = f"{f.read()}".format(**locals())
        # Add fan text file
        if fanTextFile == "No":    
            fan_t = ""
        else:
            with open(fanTextFile, 'r') as f:
                fan_t = f"{f.read()}".format(**locals())

        # Domestic Hot Water (DHW)
        if water_heater_type == "No" or people == 0:
            water_heater_t = ""
            dhw_t = ""
            dhw_draw_sch_t = ""
        else:
            water_heater_file = water_heater_type + ".txt"
            DHW_people = str(min(people,5))
            DHW_draw_sch = "Year_" + DHW_people + "_Occupant_DHW"
            DHW_draw_sch_file = DHW_people + "_Occupant_Draws.txt"
            with open(os.path.join(set_dir, building_block_dir, dhw_main_dir, dhw_wh_type_dir, water_heater_file), 'r') as f:
                water_heater_t = f.read()
            with open(os.path.join(set_dir, building_block_dir, dhw_main_dir, dhw_sys_file), 'r') as f:
                dhw_t = f"{f.read()}".format(**locals())
            with open(os.path.join(set_dir, building_block_dir, schedule_dir, schedule_DHW_draws_dir, DHW_draw_sch_file), 'r') as f:
                dhw_draw_sch_t = f"{f.read()}".format(**locals())

        # Output text files
        #... add user requested output file
        user_output_file = output_lookup + ".txt"
        with open(os.path.join(set_dir, building_block_dir, output_dir, user_output_file), 'r') as f:
            user_output_t = f"{f.read()}".format(**locals())  
        #... add general output
        with open(os.path.join(set_dir, building_block_dir, output_dir, output_otherOutput_file), 'r') as f:
            output_t = f.read()

        # Output file control
        #... add general output
        with open(os.path.join(set_dir, building_block_dir, building_block_outputControl_file), 'r') as f:
            outputcontrol_t = f.read()
        
        ### --- Assemble Final IDF Text File --- ###
        # Nests all the .txt files, now morphed into strings, in a listin the order they are to be written to the new idfs.
        # Nesting them this way allows us to easily write the full idf file, because we can simply iterate over the list
        master_tl = [
            simparam_t, performanceprecision_t, sched_t, misc_elec_sched_t, misc_gas_sched_t, \
            mat_t, glazing_t, win_construction_t, construction_t, \
            range_t, dryer_t, clotheswasher_t, dishwasher_t, frig_t, misc_elec_t, misc_gas_t, people_t, lights_t, \
            foundation_type_t, geom_rules_t, internal_mass_t, geom_main_envelope_t, geom_nonslab_adder_t, geom_main_windows_t, \
            living_zone_t, attic_zone_t, unheatedbsmt_zone_t, crawlspace_zone_t, geom_nonhtdbsmt_adder_t, \
            AFN_sim_control_t, AFN_main_zones_t, AFN_main_leakage_t, AFN_main_surfaces_t, AFN_nodes_main_t, AFN_linkage_main_t, \
            AFN_crawl_zone_t, AFN_unheatedbsmt_zone_t, AFN_crawl_unheatedbsmt_leakage_adder_t, AFN_crawl_unheatedbsmt_surface_adder_t, \
            AFN_ducts_t, system_sizing_t, airloop_t, AFN_linkage_coolingcoiladder_t, AFN_nodes_coolingcoiladder_t, \
            zone_equip_list_t, HVAC_equip_1_t, HVAC_equip_2_t, heating_coil_t, supp_heating_coil_t, cooling_coil_t, fan_t, \
            baseboard_t, thermostat_t, zone_sizing_t, water_heater_t, dhw_t, dhw_draw_sch_t, perf_t, output_t, user_output_t, outputcontrol_t
            ]
        #locations_t

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
