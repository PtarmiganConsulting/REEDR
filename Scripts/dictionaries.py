import os

# This is a separate file that makes dictionaries for genmodels.

def make_foundation_and_floor_dict():
    foundation_and_floor_dict = {
        "Vented Crawlspace - R0 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name
            "", # int_horiz_ins_depth
            "", # int_horiz_ins_width
            "", # int_vert_ins_mat_name
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.5, # wall_ht_above_grade 
            1, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "crawlspace", # floor_main outside boundary condition object
            "crawlspace", # foundation_zone_name
            ],
        "Vented Crawlspace - R13 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.5, # wall_ht_above_grade 
            1, # wall_ht_below_slab
            "Fiberglass_Batt_R13", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "crawlspace", # floor_main outside boundary condition object
            "crawlspace", # foundation_zone_name
            ],
        "Vented Crawlspace - R19 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.5, # wall_ht_above_grade 
            1, # wall_ht_below_slab
            "Fiberglass_Batt_R19", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "crawlspace", # floor_main outside boundary condition object
            "crawlspace", # foundation_zone_name
            ],
        "Vented Crawlspace - R30 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.5, # wall_ht_above_grade 
            1, # wall_ht_below_slab
            "Fiberglass_Batt_R30", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "crawlspace", # floor_main outside boundary condition object
            "crawlspace", # foundation_zone_name
            ],
        "Vented Crawlspace - R38 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.5, # wall_ht_above_grade 
            1, # wall_ht_below_slab
            "Fiberglass_Batt_R38", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "crawlspace", # floor_main outside boundary condition object
            "crawlspace", # foundation_zone_name
            ],
        "Slab - Uninsulated": [
            "Slab Construction", # main_floor_construction
            "floor_main", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0, # wall_ht_above_grade 
            0, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Foundation", # floor_main outside boundary condition
            "Kiva Foundation", # floor_main outside boundary condition object
            "", # foundation_zone_name
            ],
        "Slab - R5 Perimeter with No Thermal Break": [
            "Slab Construction", # main_floor_construction
            "floor_main", # foundation_surface
            "XPS_R5", # int_horiz_ins_mat_name 
            0, # int_horiz_ins_depth 
            2, # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0, # wall_ht_above_grade 
            0, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Foundation", # floor_main outside boundary condition
            "Kiva Foundation", # floor_main outside boundary condition object
            "", # foundation_zone_name
            ],
        "Slab - R10 Perimeter with No Thermal Break": [
            "Slab Construction", # main_floor_construction
            "floor_main", # foundation_surface
            "XPS_R10", # int_horiz_ins_mat_name 
            0, # int_horiz_ins_depth 
            2, # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0, # wall_ht_above_grade 
            0, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Foundation", # floor_main outside boundary condition
            "Kiva Foundation", # floor_main outside boundary condition object
            "", # foundation_zone_name
            ],
        "Slab - R5 Perimeter with R5 Thermal Break": [
            "Slab Construction", # main_floor_construction
            "floor_main", # foundation_surface
            "XPS_R5", # int_horiz_ins_mat_name 
            0, # int_horiz_ins_depth 
            2, # int_horiz_ins_width 
            "XPS_R5", # int_vert_ins_mat_name 
            0.5, # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0, # wall_ht_above_grade 
            0, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Foundation", # floor_main outside boundary condition
            "Kiva Foundation", # floor_main outside boundary condition object
            "", # foundation_zone_name
            ],
        "Slab - R10 Perimeter with R5 Thermal Break": [
            "Slab Construction", # main_floor_construction
            "floor_main", # foundation_surface
            "XPS_R10", # int_horiz_ins_mat_name 
            0, # int_horiz_ins_depth 
            2, # int_horiz_ins_width 
            "XPS_R5", # int_vert_ins_mat_name 
            0.5, # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0, # wall_ht_above_grade 
            0, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Foundation", # floor_main outside boundary condition
            "Kiva Foundation", # floor_main outside boundary condition object
            "", # foundation_zone_name
            ],
        "Slab - R5 Under Full Slab with R5 Thermal Break": [
            "Slab Construction w Full R5 Insulation", # main_floor_construction
            "floor_main", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "XPS_R5", # int_vert_ins_mat_name 
            0.25, # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0, # wall_ht_above_grade 
            0, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Foundation", # floor_main outside boundary condition
            "Kiva Foundation", # floor_main outside boundary condition object
            "", # foundation_zone_name
            ],
        "Slab - R10 Under Full Slab with R5 Thermal Break": [
            "Slab Construction w Full R10 Insulation", # main_floor_construction
            "floor_main", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "XPS_R5", # int_vert_ins_mat_name 
            0.25, # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0, # wall_ht_above_grade 
            0, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Foundation", # floor_main outside boundary condition
            "Kiva Foundation", # floor_main outside boundary condition object
            "", # foundation_zone_name
            ],
        "Heated Basement - Uninsulated": [
            "Interior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth
            0.2, # wall_ht_above_grade
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Adiabatic", # floor_main outside boundary condition
            "", # floor_main outside boundary condition object
            "living", # foundation_zone_name
            ],
        "Heated Basement - R5 Exterior Insulation": [
            "Interior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "XPS_R5", # ext_vert_ins_mat_name 
            2.9, # ext_vert_ins_depth
            0.2, # wall_ht_above_grade
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Adiabatic", # floor_main outside boundary condition
            "", # floor_main outside boundary condition object
            "living", # foundation_zone_name
            ],
        "Heated Basement - R10 Exterior Insulation": [
            "Interior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "XPS_R10", # ext_vert_ins_mat_name 
            2.9, # ext_vert_ins_depth
            0.2, # wall_ht_above_grade
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Adiabatic", # floor_main outside boundary condition
            "", # floor_main outside boundary condition object
            "living", # foundation_zone_name
            ],
        "Heated Basement - R15 Exterior Insulation": [
            "Interior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "XPS_R15", # ext_vert_ins_mat_name 
            2.9, # ext_vert_ins_depth
            0.2, # wall_ht_above_grade
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Adiabatic", # floor_main outside boundary condition
            "", # floor_main outside boundary condition object
            "living", # foundation_zone_name
            ],
        "Unheated Basement - Uninsulated": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.2, # wall_ht_above_grade 
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R0", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "unheatedbsmt", # floor_main outside boundary condition object
            "unheatedbsmt", # foundation_zone_name
            ],
        "Unheated Basement - R13 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.2, # wall_ht_above_grade 
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R13", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "unheatedbsmt", # floor_main outside boundary condition object
            "unheatedbsmt", # foundation_zone_name
            ],
        "Unheated Basement - R19 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.2, # wall_ht_above_grade 
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R19", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "unheatedbsmt", # floor_main outside boundary condition object
            "unheatedbsmt", # foundation_zone_name
            ],
        "Unheated Basement - R30 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.2, # wall_ht_above_grade 
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R30", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "unheatedbsmt", # floor_main outside boundary condition object
            "unheatedbsmt", # foundation_zone_name
            ],
        "Unheated Basement - R38 Cavity Insulation": [
            "Exterior Floor", # main_floor_construction
            "floor_foundation", # foundation_surface
            "", # int_horiz_ins_mat_name 
            "", # int_horiz_ins_depth 
            "", # int_horiz_ins_width 
            "", # int_vert_ins_mat_name 
            "", # int_vert_ins_depth               
            "", # ext_vert_ins_mat_name 
            "", # ext_vert_ins_depth 
            0.2, # wall_ht_above_grade 
            0.3, # wall_ht_below_slab
            "Fiberglass_Batt_R38", # floor insulation layer material name
            "Zone", # floor_main outside boundary condition
            "unheatedbsmt", # floor_main outside boundary condition object
            "unheatedbsmt", # foundation_zone_name    
            ],
    }
    return foundation_and_floor_dict

def make_hvac_dict(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, hvac_coil_dir, hvac_fan_dir):
    hvac_dict = {
        "Single Speed ASHP (8.2 HSPF 14 SEER)": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpSS.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_SS_8.2HSPF.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_14SEER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "Coil:Heating:DX:SingleSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatPump:AirtoAir", # AirLoopHVAC_Unitary_ObjectType
            "SS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            375, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Single Speed ASHP (8.5 HSPF 15 SEER)": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpSS.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_SS_8.5HSPF.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_15SEER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "Coil:Heating:DX:SingleSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatPump:AirtoAir", # AirLoopHVAC_Unitary_ObjectType
            "SS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            375, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Dual Speed ASHP (9.5 HSPF 19 SEER)": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpDS.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_DS_9.5HSPF.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_DS_19SEER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanMS.txt'), # additional fan text file
            "Coil:Heating:DX:MultiSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:MultiSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed", # AirLoopHVAC_Unitary_ObjectType
            "DS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            2, # heating_speeds
            2, # cooling_speeds
            380, # fan_CFMperTon_max
            0.75, # fan_CFMmult_spd_1
            1, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            0.72, # heating_capacitymult_spd_1
            1, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Variable Speed ASHP (10 HSPF 22 SEER)": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpMS.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_VS_10HSPF.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_VS_22SEER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanMS.txt'), # additional fan text file
            "Coil:Heating:DX:MultiSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:MultiSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed", # AirLoopHVAC_Unitary_ObjectType
            "MS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            4, # heating_speeds
            4, # cooling_speeds
            320, # fan_CFMperTon_max
            0.6, # fan_CFMmult_spd_1
            0.9, # fan_CFMmult_spd_2
            1, # fan_CFMmult_spd_3
            1.2, # fan_CFMmult_spd_4 #1.26
            0.49, # heating_capacitymult_spd_1
            0.67, # heating_capacitymult_spd_2
            1.0, # heating_capacitymult_spd_3
            1.2, # heating_capacitymult_spd_4
            ],   
        "Electric Furnace with CAC (15 SEER)": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_15SEER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            250, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Electric Furnace with No CAC": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatOnly.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "NA", # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "NA", # AirLoopHVAC_CoolingCoil_ObjectType
            "NA", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatOnly", # AirLoopHVAC_Unitary_ObjectType
            "Furnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            250, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Gas Furnace with CAC (15 SEER)": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Fuel_Main.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_15SEER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "Coil:Heating:Fuel", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Fuel_Main", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            200, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Gas Furnace with No CAC": [
            "Central", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatOnly.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Fuel_Main.txt'), # additional heating coil text file
            "NA", # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "Coil:Heating:Fuel", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Fuel_Main", # AirLoopHVAC_HeatingCoil_Name
            "NA", # AirLoopHVAC_CoolingCoil_ObjectType
            "NA", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatOnly", # AirLoopHVAC_Unitary_ObjectType
            "Furnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            200, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Resistance Wall Heat with No AC": [
            "Zonal", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatOnly.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "NA", # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "NA", # AirLoopHVAC_CoolingCoil_ObjectType
            "NA", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatOnly", # AirLoopHVAC_Unitary_ObjectType
            "Furnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            325, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Resistance Wall Heat with Room AC (8.5 EER)": [
            "Zonal", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_WinAC_8.5EER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            325, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],   
        "Resistance Wall Heat with Room AC (9.8 EER)": [
            "Zonal", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_WinAC_9.8EER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            325, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Resistance Wall Heat with Room AC (10.7 EER)": [
            "Zonal", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_WinAC_10.7EER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            1, # heating_speeds
            1, # cooling_speeds
            325, # fan_CFMperTon_max
            1, # fan_CFMmult_spd_1
            -999, # fan_CFMmult_spd_2
            -999, # fan_CFMmult_spd_3
            -999, # fan_CFMmult_spd_4
            1, # heating_capacitymult_spd_1
            -999, # heating_capacitymult_spd_2
            -999, # heating_capacitymult_spd_3
            -999, # heating_capacitymult_spd_4
            ],
        "Ductless Heat Pump (10 HSPF 22 SEER)": [
            "Zonal", # Central or Zonal HVAC
            "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneDirectAir ADU", # ZoneEquipment1Name
            "1", # ZoneEquipment1CoolingSequence
            "1", # ZoneEquipment1HeatingSequence
            "!-", # ZoneEquipment2ObjectType
            "!-", # ZoneEquipment2Name
            "!-", # ZoneEquipment2CoolingSequence
            "!-", # ZoneEquipment2HeatingSequence
            "Zone Inlet Node", # ZoneAirInletNodeName
            "", # ZoneAirExhaustNodeName
            "Zone Outlet Node", # ZoneReturnAirNodeName
            os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpMS.txt'), # HVAC equipment text file 1
            os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_DHP_VS_10HSPF.txt'), # additional heating coil text file
            os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_VS_22SEER.txt'), # additional cooling coil text file
            os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanMS.txt'), # additional fan text file
            "Coil:Heating:DX:MultiSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "Coil:Cooling:DX:MultiSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed", # AirLoopHVAC_Unitary_ObjectType
            "MS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "Fan", # fan_name
            4, # heating_speeds
            4, # cooling_speeds
            285, # fan_CFMperTon_max
            0.3, # fan_CFMmult_spd_1
            0.67, # fan_CFMmult_spd_2
            0.85, # fan_CFMmult_spd_3
            1, # fan_CFMmult_spd_4
            0.3, # heating_capacitymult_spd_1
            0.67, # heating_capacitymult_spd_2
            1.0, # heating_capacitymult_spd_3
            1.26, # heating_capacitymult_spd_4
            ],           
    }
    return hvac_dict

def make_furnace_capacity_dict():
    furnace_capacity_dict = {
        "5 kW (17 kBtu)": 5000,
        "7 kW (24 kBtu)": 7000,
        "8 kW (27 kBtu)": 8000,
        "10 kW (34 kBtu)": 10000,
        "12 kW (41 kBtu)*": 12000,
        "15 kW (51 kBtu)": 15000,
        "17 kW (58 kBtu)*": 17000,
        "20 kW (68 kBtu)": 20000,
        "25 kW (85 kBtu)": 25000,
        "30 kW (102 kBtu)": 30000,
        "35 kW (119 kBtu)": 35000,
        "40 kW (136 kBtu)": 40000,
        "30 kBtu (8.8 kW)": 8792.1,
        "40 kBtu (11.7 kW)": 11722.8,
        "60 kBtu (17.6 kW)": 17584.3,
        "80 kBtu (23.4 kW)": 23445.7,
        "100 kBtu (29.3 kW)": 29307.1,
        "120 kBtu (35.2 kW)": 35168.5,
    }
    return furnace_capacity_dict

def make_hpOrAC_capacity_dict():
    hpOrAC_capacity_dict = {
        "6 kBtu (0.5 ton)": 1758.5,
        "9 kBtu (0.75 ton)": 2637.7,
        "12 kBtu (1 ton)": 3516.9,
        "18 kBtu (1.5 ton)": 5275.4,
        "24 kBtu (2 ton)": 7033.8,
        "36 kBtu (3 ton)": 10550.7,
        "48 kBtu (4 ton)": 14067.6,
        "60 kBtu (5 ton)": 17584.5,
        "72 kBtu (6 ton)": 21101.4,
        "84 kBtu (7 ton)": 24618.3,
        "96 kBtu (8 ton)": 28135.2,
    }
    return hpOrAC_capacity_dict

def make_baseboard_capacity_dict():
    baseboard_capacity_dict = {
        "5 kW": 5000,
        "10 kW": 10000,
        "15 kW": 15000,
        "20 kW": 20000,
        "25 kW": 25000,
        "30 kW": 30000,
        "35 kW": 35000,
        "40 kW": 40000,
    }
    return baseboard_capacity_dict

def make_duct_dict():
    duct_dict = {
        "Central": [
            2, # maintrunk_duct_length
            0.943, # maintrunk_duct_U-factor
            15, # zonesupply_duct_length
            0.943, # zonesupply_duct_U-factor
            8, # zonereturn_duct_length
            0.943, # zonereturn_duct_U-factor
            1, # mainreturn_duct_length
            0.943, # mainreturn_duct_U-factor
            "user-assigned", # supply_leak
            "user-assigned", # return_leak
            ], 
        "Zonal": [
            0.0001, # maintrunk_duct_length
            0.0001, # maintrunk_duct_U-factor
            0.0001, # zonesupply_duct_length
            0.0001, # zonesupply_duct_U-factor
            0.0001, # zonereturn_duct_length
            0.0001, # zonereturn_duct_U-factor
            0.0001, # mainreturn_duct_length
            0.0001, # mainreturn_duct_U-factor
            0.0001, # supply_leak
            0.0001, # return_leak
            ],
    }
    return duct_dict

def make_foundation_dict():
    foundation_dict = {
        "Vent": ["Vented Crawlspace", "crawlspace"],
        "Slab": ["Slab", "attic"],
        "Heat": ["Heated Basement", "living"],
        "Unhe": ["Unheated Basement", "unheatedbsmt"],
    }
    return foundation_dict
