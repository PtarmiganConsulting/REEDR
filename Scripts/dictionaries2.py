import os


# This is a separate file that makes dictionaries for genmodels.

def make_Energy_All_End_Uses_dict():
    Energy_All_End_Uses_dict = {
        "Run Label": {
            "mapping_fieldname": 'Run_Label', 
            "conversion_ID": "Run_Label"
            },
        "Total Elec [kWh]": {
            "mapping_fieldname": 'Electricity:Facility [J]', 
            "conversion_ID": "Elec"
            },
        "Total Gas [therm]": {
            "mapping_fieldname": 'NaturalGas:Facility [J]', 
            "conversion_ID": "Gas"
            },
        "Total Heat Elec [kWh]": {
            "mapping_fieldname": 'Heating:Electricity [J]', 
            "conversion_ID": "Elec"
            },
        "Prim Furnace Heat Elec [kWh]": {
            "mapping_fieldname": 'HEATING_RESISTANCE_MAIN:Heating Coil Electricity Energy [J]', 
            "conversion_ID": "Elec"
            },
        "ASHP Compressor Heat Elec [kWh]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Electricity Energy [J]', 
            "conversion_ID": "Elec"
            },
        "ASHP Backup Heat Elec [kWh]": {
            "mapping_fieldname": 'HEATING_RESISTANCE_BACKUP:Heating Coil Electricity Energy [J]', 
            "conversion_ID": "Elec"
            },
        "ASHP Defrost Elec [kWh]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Defrost Electricity Energy [J]', 
            "conversion_ID": "Elec"
            },
        "ASHP Crankcase Heater Elec [kWh]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Crankcase Heater Electricity Energy [J]',
            "conversion_ID": "Elec"
            },
        "Baseboard Heat Elec [kWh]": {
            "mapping_fieldname": 'BASEBOARDELECTRIC:Baseboard Total Heating Energy [J]',
            "conversion_ID": "Elec"
            },
        "Cool Elec [kWh]": {
            "mapping_fieldname": 'Cooling:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "Fan Elec [kWh]": {
            "mapping_fieldname": 'Fans:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "Pump Elec [kWh]": {
            "mapping_fieldname": 'Pumps:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "DHW Elec [kWh]": {
            "mapping_fieldname": 'WaterSystems:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "IntLights Elec [kWh]": {
            "mapping_fieldname": 'InteriorLights:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "ExtLights Elec [kWh]": {
            "mapping_fieldname": 'ExteriorLights:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "Total IntEquip Elec [kWh]": {
            "mapping_fieldname": 'InteriorEquipment:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "IntEquip Range Elec [kWh]": {
            "mapping_fieldname": 'electric_range:InteriorEquipment:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "IntEquip Dryer Elec [kWh]": {
            "mapping_fieldname": 'electric_dryer:InteriorEquipment:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "IntEquip Clotheswasher Elec [kWh]": {
            "mapping_fieldname": 'clotheswasher:InteriorEquipment:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "IntEquip Dishwasher Elec [kWh]": {
            "mapping_fieldname": 'dishwasher:InteriorEquipment:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "IntEquip Refrigerator Elec [kWh]": {
            "mapping_fieldname": 'refrigerator:InteriorEquipment:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "IntEquip Misc Elec [kWh]": {
            "mapping_fieldname": 'electric_mels:InteriorEquipment:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "HeatRecov Elec [kWh]": {
            "mapping_fieldname": 'HeatRecovery:Electricity [J]',
            "conversion_ID": "Elec"
            },
        "Total Heat Gas [therm]": {
            "mapping_fieldname": 'Heating:NaturalGas [J]',
            "conversion_ID": "Gas"
            },
        "DHW Gas [therm]": {
            "mapping_fieldname": 'WaterSystems:NaturalGas [J]',
            "conversion_ID": "Gas"
            },
        "Total IntEquip Gas [therm]": {
            "mapping_fieldname": 'InteriorEquipment:NaturalGas [J]',
            "conversion_ID": "Gas"
            },
        "IntEquip Range Gas [therm]": {
            "mapping_fieldname": 'gas_range:InteriorEquipment:NaturalGas ',
            "conversion_ID": "Gas"
            },
        "IntEquip Dryer Gas [therm]": {
            "mapping_fieldname": 'gas_dryer:InteriorEquipment:NaturalGas [J]',
            "conversion_ID": "Gas"
            },
        "IntEquip Misc Gas [therm]": {
            "mapping_fieldname": 'gas_mels:InteriorEquipment:NaturalGas [J]',
            "conversion_ID": "Gas"
            },
        "UnmetHours Heating": {
            "mapping_fieldname": 'Facility:Facility Heating Setpoint Not Met Time [hr]',
            "conversion_ID": "NA"
            },
        "UnmetHours Cooling": {
            "mapping_fieldname": 'Facility:Facility Cooling Setpoint Not Met Time [hr]',
            "conversion_ID": "NA"
            },
        "Infiltration Living [ACH]": {
            "mapping_fieldname": 'LIVING:AFN Zone Infiltration Air Change Rate [ach]',
            "conversion_ID": "NA"
            },
        "Infiltration Attic [ACH]": {
            "mapping_fieldname": 'ATTIC:AFN Zone Infiltration Air Change Rate [ach]',
            "conversion_ID": "NA"
            },
        "Infiltration Crawlspace [ACH]": {
            "mapping_fieldname": 'CRAWLSPACE:AFN Zone Infiltration Air Change Rate [ach]',
            "conversion_ID": "NA"
            },
        "Infiltration UnheatedBasement [ACH]": {
            "mapping_fieldname": 'UNHEATEDBSMT:AFN Zone Infiltration Air Change Rate [ach]',
            "conversion_ID": "NA"
            },
    }
    return Energy_All_End_Uses_dict


def make_Demand_All_HVAC_dict():
    Demand_All_HVAC_dict = {
        "ASHP Compressor Heat [W]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "ASHP Resistance Backup Heat [W]": {
            "mapping_fieldname": 'HEATING_RESISTANCE_BACKUP:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "ASHP Defrost [W]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Defrost Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "ASHP Crankcase Heater [W]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Crankcase Heater Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Primary Elec Furnace Heat [W]": {
            "mapping_fieldname": 'HEATING_RESISTANCE_MAIN:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Gas Furnace Gas Use [Btu/h]": {
            "mapping_fieldname": 'MAIN FUEL HEATING COIL_UNIT1:Heating Coil NaturalGas Rate [W]', 
            "conversion_ID": "Gas"
            },
        "Gas Furnace Electric Use [W]": {
            "mapping_fieldname": 'MAIN FUEL HEATING COIL_UNIT1:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Cooling[W]": {
            "mapping_fieldname": 'DX_COOLING_COIL:Cooling Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Fan [W]": {
            "mapping_fieldname": 'FAN:Fan Electricity Rate [W]',
            "conversion_ID": "Elec"
            },
        "Living Zone Air Temperature [F]": {
            "mapping_fieldname": 'LIVING:Zone Mean Air Temperature [C]',
            "conversion_ID": "Temp"
            },
        "Attic Zone Air Temperature [F]": {
            "mapping_fieldname": 'ATTIC:Zone Mean Air Temperature [C]',
            "conversion_ID": "Temp"
            },
        "Crawlspace Zone Air Temperature [F]": {
            "mapping_fieldname": 'CRAWLSPACE:Zone Mean Air Temperature [C]',
            "conversion_ID": "Temp"
            },
        "Outdoor Air Temperature [F]": {
            "mapping_fieldname": 'Environment:Site Outdoor Air Drybulb Temperature [C]',
            "conversion_ID": "Temp"
            },
    }
    return Demand_All_HVAC_dict


def make_Demand_Heating_dict():
    Demand_Heating_dict = {
        "ASHP Compressor Heat [W]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "ASHP Resistance Backup Heat [W]": {
            "mapping_fieldname": 'HEATING_RESISTANCE_BACKUP:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "ASHP Defrost [W]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Defrost Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "ASHP Crankcase Heater [W]": {
            "mapping_fieldname": 'DX_HEATING_COIL:Heating Coil Crankcase Heater Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Primary Elec Furnace Heat [W]": {
            "mapping_fieldname": 'HEATING_RESISTANCE_MAIN:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Gas Furnace Gas Use [Btu/h]": {
            "mapping_fieldname": 'MAIN FUEL HEATING COIL_UNIT1:Heating Coil NaturalGas Rate [W]', 
            "conversion_ID": "Gas"
            },
        "Gas Furnace Electric Use [W]": {
            "mapping_fieldname": 'MAIN FUEL HEATING COIL_UNIT1:Heating Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Fan [W]": {
            "mapping_fieldname": 'FAN:Fan Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Living Zone Air Temperature [F]": {
            "mapping_fieldname": 'LIVING:Zone Mean Air Temperature [C]',
            "conversion_ID": "Temp"
            },
        "Attic Zone Air Temperature [F]": {
            "mapping_fieldname": 'ATTIC:Zone Mean Air Temperature [C]',
            "conversion_ID": "Temp"
            },
        "Crawlspace Zone Air Temperature [F]": {
            "mapping_fieldname": 'CRAWLSPACE:Zone Mean Air Temperature [C]',
            "conversion_ID": "Temp"
            },
        "Outdoor Air Temperature [F]": {
            "mapping_fieldname": 'Environment:Site Outdoor Air Drybulb Temperature [C]',
            "conversion_ID": "Temp"
            },
    }
    return Demand_Heating_dict


def make_Demand_Cooling_dict():
    Demand_Cooling_dict = {
        "Cooling[W]": {
            "mapping_fieldname": 'DX_COOLING_COIL:Cooling Coil Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Fan [W]": {
            "mapping_fieldname": 'FAN:Fan Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Living Zone Air Temperature [F]": {
            "mapping_fieldname": 'LIVING:Zone Mean Air Temperature [C]', 
            "conversion_ID": "Temp"
            },
        "Attic Zone Air Temperature [F]": {
            "mapping_fieldname": 'ATTIC:Zone Mean Air Temperature [C]', 
            "conversion_ID": "Temp"
            },
        "Crawlspace Zone Air Temperature [F]": {
            "mapping_fieldname": 'CRAWLSPACE:Zone Mean Air Temperature [C]', 
            "conversion_ID": "Temp"
            },
        "Outdoor Air Temperature [F]": {
            "mapping_fieldname": 'Environment:Site Outdoor Air Drybulb Temperature [C]', 
            "conversion_ID": "Temp"
            },
    }
    return Demand_Cooling_dict


def make_Demand_Fan_dict():
    Demand_Fan_dict = {
        "Fan [W]": {
            "mapping_fieldname": 'FAN:Fan Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Living Zone Air Temperature [F]": {
            "mapping_fieldname": 'LIVING:Zone Mean Air Temperature [C]', 
            "conversion_ID": "Temp"
            },
        "Attic Zone Air Temperature [F]": {
            "mapping_fieldname": 'ATTIC:Zone Mean Air Temperature [C]', 
            "conversion_ID": "Temp"
            },
        "Crawlspace Zone Air Temperature [F]": {
            "mapping_fieldname": 'CRAWLSPACE:Zone Mean Air Temperature [C]', 
            "conversion_ID": "Temp"
            },
        "Outdoor Air Temperature [F]": {
            "mapping_fieldname": 'Environment:Site Outdoor Air Drybulb Temperature [C]', 
            "conversion_ID": "Temp"
            },
    }
    return Demand_Fan_dict


def make_Demand_Lighting_dict():
    Demand_Lighting_dict = {
        "Interior Lighting [W]": {
            "mapping_fieldname": 'INTERIOR LIGHTS:Lights Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Exterior Lighting [W]": {
            "mapping_fieldname": 'EXTERIOR LIGHTS:Lights Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
    }
    return Demand_Lighting_dict


def make_Demand_Water_Heating_dict():
    Demand_Water_Heating_dict = {
        "Electric Water Heater [W]": {
            "mapping_fieldname": 'WATER HEATER:Water Heater Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Gas Water Heater [Btu/h]": {
            "mapping_fieldname": 'WATER HEATER:Water Heater NaturalGas Rate [W]', 
            "conversion_ID": "Gas"
            },
        "Mains Water Temp[F]": {
            "mapping_fieldname": 'Environment:Site Mains Water Temperature [C]', 
            "conversion_ID": "Temp"
            },
    }
    return Demand_Water_Heating_dict


def make_Demand_Other_Equipment_dict():
    Demand_Other_Equipment_dict = {
        "Dishwasher [W]": {
            "mapping_fieldname": 'DISHWASHER1:Electric Equipment Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Refrigerator [W]": {
            "mapping_fieldname": 'REFRIGERATOR1:Electric Equipment Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Clothes Washer [W]": {
            "mapping_fieldname": 'CLOTHESWASHER1:Electric Equipment Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Electric Dryer [W]": {
            "mapping_fieldname": 'ELECTRIC_DRYER1:Electric Equipment Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Electric Range [W]": {
            "mapping_fieldname": 'ELECTRIC_RANGE1:Electric Equipment Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Miscellaneous Electric Loads [W]": {
            "mapping_fieldname": 'ELECTRIC_MELS1:Electric Equipment Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Gas Dryer Electric Use [W]": {
            "mapping_fieldname": 'GAS_DRYER1:Electric Equipment Electricity Rate [W]', 
            "conversion_ID": "Elec"
            },
        "Gas Dryer Gas Use [Btu/h]": {
            "mapping_fieldname": 'GAS_DRYER1:Gas Equipment NaturalGas Rate [W]', 
            "conversion_ID": "Gas"
            },
        "Gas Range [Btu/h]": {
            "mapping_fieldname": 'GAS_RANGE1:Gas Equipment NaturalGas Rate [W]',
            "conversion_ID": "Gas"
            },
        "Miscellaneous Gas Loads [Btu/h]": {
            "mapping_fieldname": 'GAS_MELS1:Gas Equipment NaturalGas Rate [W]',
            "conversion_ID": "Gas"
            },
    }
    return Demand_Other_Equipment_dict
