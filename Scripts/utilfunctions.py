#*******************************************************************************************************************************************************************

#Copyright (C) 2023 Ptarmigan Consulting LLC

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************


def findLastRealLayer(list_layers):

    for i in range(len(list_layers)):
            if list_layers[i] != "!-":
                last_real_layer_num = i

    return last_real_layer_num

def formatLayerList(last_real_layer_num, list_layers):

    #... add proper punctuation for EnergyPlus based on last real layer
    i = 0
    for i in range(len(list_layers)):
        if i == last_real_layer_num:
            # last layer in energy plus needs to end with a semi-colon
            list_layers[i] = list_layers[i] + ";"
        else:
            # otherwise it is either an intermediate layer or an empty layer, and use a comma
            list_layers[i] = list_layers[i] + ","

    return list_layers

def getFoundationIdentifier(user_found_type, floor_effective_Rvalue, slab_perimeter_Rvalue, under_slab_Rvalue, slab_thermalbreak_Rvalue, foundation_wall_Rvalue):

    #Foundation Identifier Options:
        #Crawl w Insulated Floor
        #Crawl w Insulated Floor and Crawl Wall
        #Slab w No Insulation
        #Slab w Perimeter Insulation Only
        #Slab w Thermal Break Only
        #Slab w Perimeter and Thermal Break Insulation
        #Slab w Full Under Insulation
        #Slab w Full Under Insulation and Thermal Break
        #Heated Basement w No Insulation
        #Heated Basement w Wall Insulation
        #Unheated Basement w Insulated Floor
        #Unheated Basement w Insulated Floor and Wall

    if user_found_type == "Crawlspace":
        if foundation_wall_Rvalue > 0:
            foundation_identifier = "Crawl w Insulated Floor and Crawl Wall"
        else:
            foundation_identifier = "Crawl w Insulated Floor"

    elif user_found_type == "Slab":
        if under_slab_Rvalue > 0 and slab_thermalbreak_Rvalue > 0:
            foundation_identifier = "Slab w Full Under Insulation and Thermal Break"
        elif under_slab_Rvalue > 0:
            foundation_identifier = "Slab w Full Under Insulation"
        elif slab_perimeter_Rvalue > 0 and slab_thermalbreak_Rvalue > 0:
            foundation_identifier = "Slab w Perimeter and Thermal Break Insulation"
        elif slab_perimeter_Rvalue > 0:
            foundation_identifier = "Slab w Perimeter Insulation Only"
        elif slab_thermalbreak_Rvalue > 0:
            foundation_identifier = "Slab w Thermal Break Only"
        else:
            foundation_identifier = "Slab w No Insulation"
        
    elif user_found_type == "Heated Basement":
        if foundation_wall_Rvalue > 0:
            foundation_identifier = "Heated Basement w Wall Insulation"
        else:
            foundation_identifier = "Heated Basement w No Insulation"

    elif user_found_type == "Unheated Basement":
        if foundation_wall_Rvalue > 0:
            foundation_identifier = "Unheated Basement w Insulated Floor and Wall"
        else:
            foundation_identifier = "Unheated Basement w Insulated Floor"

    else:
        foundation_identifier = "ERROR"


    return foundation_identifier