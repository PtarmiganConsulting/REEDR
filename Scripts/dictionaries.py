import os

# This is a separate file that makes dictionaries for genmodels.

def make_foundation_and_floor_dict():
    foundation_and_floor_dict = {
        "Vented Crawlspace - R0 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name
            "int_horiz_ins_depth": "", # int_horiz_ins_depth
            "int_horiz_ins_width": "", # int_horiz_ins_width
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.5, # wall_ht_above_grade 
            "wall_ht_below_slab": 1, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "crawlspace", # floor_main outside boundary condition object
            "foundation_zone_name": "crawlspace", # foundation_zone_name
            },
        "Vented Crawlspace - R13 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.5, # wall_ht_above_grade 
            "wall_ht_below_slab": 1, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R13", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "crawlspace", # floor_main outside boundary condition object
            "foundation_zone_name": "crawlspace", # foundation_zone_name
            },
        "Vented Crawlspace - R19 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.5, # wall_ht_above_grade 
            "wall_ht_below_slab": 1, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R19", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "crawlspace", # floor_main outside boundary condition object
            "foundation_zone_name": "crawlspace", # foundation_zone_name
            },
        "Vented Crawlspace - R30 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.5, # wall_ht_above_grade 
            "wall_ht_below_slab": 1, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R30", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "crawlspace", # floor_main outside boundary condition object
            "foundation_zone_name": "crawlspace", # foundation_zone_name
            },
        "Vented Crawlspace - R38 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.5, # wall_ht_above_grade 
            "wall_ht_below_slab": 1, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R38", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "crawlspace", # floor_main outside boundary condition object
            "foundation_zone_name": "crawlspace", # foundation_zone_name
            },
        "Slab - Uninsulated": {
            "main_floor_construction": "Slab Construction", # main_floor_construction
            "foundation_surface": "floor_main", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0, # wall_ht_above_grade 
            "wall_ht_below_slab": 0, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Foundation", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "Kiva Foundation", # floor_main outside boundary condition object
            "foundation_zone_name": "", # foundation_zone_name
            },
        "Slab - R5 Perimeter with No Thermal Break": {
            "main_floor_construction": "Slab Construction", # main_floor_construction
            "foundation_surface": "floor_main", # foundation_surface
            "int_horiz_ins_mat_name": "XPS_R5", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": 0, # int_horiz_ins_depth 
            "int_horiz_ins_width": 2, # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0, # wall_ht_above_grade 
            "wall_ht_below_slab": 0, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Foundation", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "Kiva Foundation", # floor_main outside boundary condition object
            "foundation_zone_name": "", # foundation_zone_name
            },
        "Slab - R10 Perimeter with No Thermal Break": {
            "main_floor_construction": "Slab Construction", # main_floor_construction
            "foundation_surface": "floor_main", # foundation_surface
            "int_horiz_ins_mat_name": "XPS_R10", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": 0, # int_horiz_ins_depth 
            "int_horiz_ins_width": 2, # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0, # wall_ht_above_grade 
            "wall_ht_below_slab": 0, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Foundation", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "Kiva Foundation", # floor_main outside boundary condition object
            "foundation_zone_name": "", # foundation_zone_name
            },
        "Slab - R5 Perimeter with R5 Thermal Break": {
            "main_floor_construction": "Slab Construction", # main_floor_construction
            "foundation_surface": "floor_main", # foundation_surface
            "int_horiz_ins_mat_name": "XPS_R5", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": 0, # int_horiz_ins_depth 
            "int_horiz_ins_width": 2, # int_horiz_ins_width 
            "int_vert_ins_mat_name": "XPS_R5", # int_vert_ins_mat_name 
            "int_vert_ins_depth": 0.5, # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0, # wall_ht_above_grade 
            "wall_ht_below_slab": 0, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Foundation", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "Kiva Foundation", # floor_main outside boundary condition object
            "foundation_zone_name": "", # foundation_zone_name
            },
        "Slab - R10 Perimeter with R5 Thermal Break": {
            "main_floor_construction": "Slab Construction", # main_floor_construction
            "foundation_surface": "floor_main", # foundation_surface
            "int_horiz_ins_mat_name": "XPS_R10", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": 0, # int_horiz_ins_depth 
            "int_horiz_ins_width": 2, # int_horiz_ins_width 
            "int_vert_ins_mat_name": "XPS_R5", # int_vert_ins_mat_name 
            "int_vert_ins_depth": 0.5, # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0, # wall_ht_above_grade 
            "wall_ht_below_slab": 0, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Foundation", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "Kiva Foundation", # floor_main outside boundary condition object
            "foundation_zone_name": "", # foundation_zone_name
            },
        "Slab - R5 Under Full Slab with R5 Thermal Break": {
            "main_floor_construction": "Slab Construction w Full R5 Insulation", # main_floor_construction
            "foundation_surface": "floor_main", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "XPS_R5", # int_vert_ins_mat_name 
            "int_vert_ins_depth": 0.25, # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0, # wall_ht_above_grade 
            "wall_ht_below_slab": 0, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Foundation", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "Kiva Foundation", # floor_main outside boundary condition object
            "foundation_zone_name": "", # foundation_zone_name
            },
        "Slab - R10 Under Full Slab with R5 Thermal Break": {
            "main_floor_construction": "Slab Construction w Full R10 Insulation", # main_floor_construction
            "foundation_surface": "floor_main", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "XPS_R5", # int_vert_ins_mat_name 
            "int_vert_ins_depth": 0.25, # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0, # wall_ht_above_grade 
            "wall_ht_below_slab": 0, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Foundation", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "Kiva Foundation", # floor_main outside boundary condition object
            "foundation_zone_name": "", # foundation_zone_name
            },
        "Heated Basement - Uninsulated": {
            "main_floor_construction": "Interior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Adiabatic", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "", # floor_main outside boundary condition object
            "foundation_zone_name": "living", # foundation_zone_name
            },
        "Heated Basement - R5 Exterior Insulation": {
            "main_floor_construction": "Interior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "XPS_R5", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": 2.9, # ext_vert_ins_depth
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Adiabatic", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "", # floor_main outside boundary condition object
            "foundation_zone_name": "living", # foundation_zone_name
            },
        "Heated Basement - R10 Exterior Insulation": {
            "main_floor_construction": "Interior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "XPS_R10", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": 2.9, # ext_vert_ins_depth
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Adiabatic", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "", # floor_main outside boundary condition object
            "foundation_zone_name": "living", # foundation_zone_name
            },
        "Heated Basement - R15 Exterior Insulation": {
            "main_floor_construction": "Interior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "XPS_R15", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": 2.9, # ext_vert_ins_depth
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Adiabatic", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "", # floor_main outside boundary condition object
            "foundation_zone_name": "living", # foundation_zone_name
            },
        "Unheated Basement - Uninsulated": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade 
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R0", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "unheatedbsmt", # floor_main outside boundary condition object
            "foundation_zone_name": "unheatedbsmt", # foundation_zone_name
            },
        "Unheated Basement - R13 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade 
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R13", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "unheatedbsmt", # floor_main outside boundary condition object
            "foundation_zone_name": "unheatedbsmt", # foundation_zone_name
            },
        "Unheated Basement - R19 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade 
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R19", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "unheatedbsmt", # floor_main outside boundary condition object
            "foundation_zone_name": "unheatedbsmt", # foundation_zone_name
            },
        "Unheated Basement - R30 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade 
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R30", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "unheatedbsmt", # floor_main outside boundary condition object
            "foundation_zone_name": "unheatedbsmt", # foundation_zone_name
            },
        "Unheated Basement - R38 Cavity Insulation": {
            "main_floor_construction": "Exterior Floor", # main_floor_construction
            "foundation_surface": "floor_foundation", # foundation_surface
            "int_horiz_ins_mat_name": "", # int_horiz_ins_mat_name 
            "int_horiz_ins_depth": "", # int_horiz_ins_depth 
            "int_horiz_ins_width": "", # int_horiz_ins_width 
            "int_vert_ins_mat_name": "", # int_vert_ins_mat_name 
            "int_vert_ins_depth": "", # int_vert_ins_depth               
            "ext_vert_ins_mat_name": "", # ext_vert_ins_mat_name 
            "ext_vert_ins_depth": "", # ext_vert_ins_depth 
            "wall_ht_above_grade": 0.2, # wall_ht_above_grade 
            "wall_ht_below_slab": 0.3, # wall_ht_below_slab
            "floor_insulation_layer": "Fiberglass_Batt_R38", # floor insulation layer material name
            "floor_main_outside_boundary_condition": "Zone", # floor_main outside boundary condition
            "floor_main_outside_boundary_condition_object": "unheatedbsmt", # floor_main outside boundary condition object
            "foundation_zone_name": "unheatedbsmt", # foundation_zone_name    
            },
    }
    return foundation_and_floor_dict

def make_hvac_dict(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, hvac_coil_dir, hvac_fan_dir):
    hvac_dict = {
        "Single Speed ASHP (8.2 HSPF 14 SEER)": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpSS.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_SS_8.2HSPF.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_14SEER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:DX:SingleSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatPump:AirtoAir", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "SS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 375, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Single Speed ASHP (8.5 HSPF 15 SEER)": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpSS.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_SS_8.5HSPF.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_15SEER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:DX:SingleSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatPump:AirtoAir", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "SS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 375, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Dual Speed ASHP (9.5 HSPF 19 SEER)": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpDS.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_DS_9.5HSPF.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_DS_19SEER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanMS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:DX:MultiSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:MultiSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "DS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 2, # heating_speeds
            "cooling_speeds": 2, # cooling_speeds
            "fan_CFMperTon_max": 380, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 0.75, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": 1, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 0.72, # heating_capacitymult_spd_1
            "capacitymult_spd_2": 1, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Variable Speed ASHP (10 HSPF 22 SEER)": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpMS.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_ASHP_VS_10HSPF.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_VS_22SEER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanMS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:DX:MultiSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:MultiSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "MS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 4, # heating_speeds
            "cooling_speeds": 4, # cooling_speeds
            "fan_CFMperTon_max": 320, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 0.6, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": 0.9, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": 1, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": 1.2, # fan_CFMmult_spd_4 #1.26
            "capacitymult_spd_1": 0.49, # heating_capacitymult_spd_1
            "capacitymult_spd_2": 0.67, # heating_capacitymult_spd_2
            "capacitymult_spd_3": 1.0, # heating_capacitymult_spd_3
            "capacitymult_spd_4": 1.2, # heating_capacitymult_spd_4
            },   
        "Electric Furnace with CAC (15 SEER)": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_15SEER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 250, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Electric Furnace with No CAC": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatOnly.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": "NA", # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "NA", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "NA", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatOnly", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "Furnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 250, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Gas Furnace with CAC (15 SEER)": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Fuel_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_SS_15SEER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Fuel", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Fuel_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 200, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Gas Furnace with No CAC": {
            "CentralOrZonal": "Central", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatOnly.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Fuel_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": "NA", # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'CentralFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Fuel", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Fuel_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "NA", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "NA", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatOnly", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "Furnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 200, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Resistance Wall Heat with No AC": {
            "CentralOrZonal": "Zonal", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatOnly.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": "NA", # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "NA", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "NA", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatOnly", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "Furnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 325, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Resistance Wall Heat with Room AC (8.5 EER)": {
            "CentralOrZonal": "Zonal", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_WinAC_8.5EER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 325, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },   
        "Resistance Wall Heat with Room AC (9.8 EER)": {
            "CentralOrZonal": "Zonal", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_WinAC_9.8EER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 325, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Resistance Wall Heat with Room AC (10.7 EER)": {
            "CentralOrZonal": "Zonal", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatCool.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_Resistance_Main.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_WinAC_10.7EER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanSS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:Electric", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "Heating_Resistance_Main", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:SingleSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatCool", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "ACandFurnace", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 1, # heating_speeds
            "cooling_speeds": 1, # cooling_speeds
            "fan_CFMperTon_max": 325, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 1, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": -999, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": -999, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": -999, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 1, # heating_capacitymult_spd_1
            "capacitymult_spd_2": -999, # heating_capacitymult_spd_2
            "capacitymult_spd_3": -999, # heating_capacitymult_spd_3
            "capacitymult_spd_4": -999, # heating_capacitymult_spd_4
            },
        "Ductless Heat Pump (10 HSPF 22 SEER)": {
            "CentralOrZonal": "Zonal", # Central or Zonal HVAC
            "ZoneEquipment1ObjectType": "ZoneHVAC:AirDistributionUnit", # ZoneEquipment1ObjectType
            "ZoneEquipment1Name": "ZoneDirectAir ADU", # ZoneEquipment1Name
            "ZoneEquipment1CoolingSequence": "1", # ZoneEquipment1CoolingSequence
            "ZoneEquipment1HeatingSequence": "1", # ZoneEquipment1HeatingSequence
            "ZoneEquipment2ObjectType": "!-", # ZoneEquipment2ObjectType
            "ZoneEquipment2Name": "!-", # ZoneEquipment2Name
            "ZoneEquipment2CoolingSequence": "!-", # ZoneEquipment2CoolingSequence
            "ZoneEquipment2HeatingSequence": "!-", # ZoneEquipment2HeatingSequence
            "ZoneAirInletNodeName": "Zone Inlet Node", # ZoneAirInletNodeName
            "ZoneAirExhaustNodeName": "", # ZoneAirExhaustNodeName
            "ZoneReturnAirNodeName": "Zone Outlet Node", # ZoneReturnAirNodeName
            "unitaryTextFile": os.path.join(set_dir, building_block_dir, hvac_airloop_main_dir, hvac_airloop_hvac_dir, 'UnitaryHeatPumpMS.txt'), # HVAC equipment text file 1
            "airDistUnitTextFile": os.path.join(set_dir, building_block_dir, hvac_zone_main_dir, hvac_zone_hvac_dir, 'ADU.txt'), # HVAC equipment text file 2
            "heatCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Heating_DHP_VS_10HSPF.txt'), # additional heating coil text file
            "coolCoilTextFile": os.path.join(set_dir, building_block_dir, hvac_coil_dir, 'Cooling_ASHP_VS_22SEER.txt'), # additional cooling coil text file
            "fanTextFile": os.path.join(set_dir, building_block_dir, hvac_fan_dir, 'ZonalFanMS.txt'), # additional fan text file
            "AirLoopHVAC_HeatingCoil_ObjectType": "Coil:Heating:DX:MultiSpeed", # AirLoopHVAC_HeatingCoil_ObjectType
            "AirLoopHVAC_HeatingCoil_Name": "DX_Heating_Coil", # AirLoopHVAC_HeatingCoil_Name
            "AirLoopHVAC_CoolingCoil_ObjectType": "Coil:Cooling:DX:MultiSpeed", # AirLoopHVAC_CoolingCoil_ObjectType
            "AirLoopHVAC_CoolingCoil_Name": "DX_Cooling_Coil", # AirLoopHVAC_CoolingCoil_Name
            "AirLoopHVAC_Unitary_ObjectType": "AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed", # AirLoopHVAC_Unitary_ObjectType
            "AirLoopHVAC_Unitary_ObjectName": "MS Heat Pump", # AirLoopHVAC_Unitary_ObjectName
            "fan_name": "Fan", # fan_name
            "heating_speeds": 4, # heating_speeds
            "cooling_speeds": 4, # cooling_speeds
            "fan_CFMperTon_max": 285, # fan_CFMperTon_max
            "fan_CFMmult_spd_1": 0.3, # fan_CFMmult_spd_1
            "fan_CFMmult_spd_2": 0.67, # fan_CFMmult_spd_2
            "fan_CFMmult_spd_3": 0.85, # fan_CFMmult_spd_3
            "fan_CFMmult_spd_4": 1, # fan_CFMmult_spd_4
            "capacitymult_spd_1": 0.3, # heating_capacitymult_spd_1
            "capacitymult_spd_2": 0.67, # heating_capacitymult_spd_2
            "capacitymult_spd_3": 1.0, # heating_capacitymult_spd_3
            "capacitymult_spd_4": 1.26, # heating_capacitymult_spd_4
            },           
    }
    return hvac_dict

def make_living_infiltration_coeff_dict():
    living_infiltration_coeff_dict = {
        "Slab_Low": {
            "Intercept": -5.4794627405224,
            "coeff_footprint": 0.449575948578335,
            "coeff_height": 0.340049847086377,
            "coeff_ACH50": 1.18718157939516,
        },
        "Slab_Med": {
            "Intercept": -5.41197321741644,
            "coeff_footprint": 0.357699043323076,
            "coeff_height": 0.374275258344276,
            "coeff_ACH50": 1.54427322040671,
        },
        "Slab_High": {
            "Intercept": -5.77021675553459,
            "coeff_footprint": 0.386814978635308,
            "coeff_height": 0.438267289039239,
            "coeff_ACH50": 1.54963030520262,
        },
        "Vented Crawlspace_Low": {
            "Intercept": -4.56455900410368,
            "coeff_footprint": 0.375134782319205,
            "coeff_height": 0.283151523710581,
            "coeff_ACH50": 1.0841939308996,
        },
        "Vented Crawlspace_Med": {
            "Intercept": -4.95189805160011,
            "coeff_footprint": 0.323089235151636,
            "coeff_height": 0.357954844729464,
            "coeff_ACH50": 1.47837666394136,
        },
        "Vented Crawlspace_High": {
            "Intercept": -5.56586988439739,
            "coeff_footprint": 0.376293528194144,
            "coeff_height": 0.418430811611842,
            "coeff_ACH50": 1.52439919409061,
        },
        "Unheated Basement_Low": {
            "Intercept": -4.0049211230694,
            "coeff_footprint": 0.29334006830038,
            "coeff_height": 0.308470008957762,
            "coeff_ACH50": 1.02449589465282,
        },
        "Unheated Basement_Med": {
            "Intercept": -4.89351918231486,
            "coeff_footprint": 0.319198071535125,
            "coeff_height": 0.357369610388076,
            "coeff_ACH50": 1.46661556201398,
        },
        "Unheated Basement_High": {
            "Intercept": -5.53520482885818,
            "coeff_footprint": 0.375588619399222,
            "coeff_height": 0.416030213110777,
            "coeff_ACH50": 1.51847061521071,
        },
        "Heated Basement_Low": {
            "Intercept": -7.50760925775228,
            "coeff_footprint": 0.827974951892082,
            "coeff_height": 0.00316063420335651,
            "coeff_ACH50": 1.4002739382372,
        },
        "Heated Basement_Med": {
            "Intercept": -5.80562124716613,
            "coeff_footprint": 0.51823062303286,
            "coeff_height": 0.0672650682960535,
            "coeff_ACH50": 1.754113322665,
        },
        "Heated Basement_High": {
            "Intercept": -5.45020719790042,
            "coeff_footprint": 0.481827544334094,
            "coeff_height": 0.0933158986544682,
            "coeff_ACH50": 1.70045883883582,
        },
    }
    return living_infiltration_coeff_dict

def make_attic_infiltration_coeff_dict():
    attic_infiltration_coeff_dict = {
        "Slab_Low": {
            "Intercept": 1.20628561488316,
            "coeff_footprint": 0.104222656723588,
            "coeff_height": -0.186698734594057,
            "coeff_ACH50": 0.0311213076551005,
        },
        "Slab_Med": {
            "Intercept": 0.836341162706868,
            "coeff_footprint": 0.107221500554972,
            "coeff_height": -0.109468611331111,
            "coeff_ACH50": 0.14375919670089,
        },
        "Slab_High": {
            "Intercept": 0.210021808379302,
            "coeff_footprint": 0.115380560889372,
            "coeff_height": -0.00718866652033437,
            "coeff_ACH50": 0.284454562866848,
        },
        "Vented Crawlspace_Low": {
            "Intercept": 1.58102134544365,
            "coeff_footprint": 0.05682517047341,
            "coeff_height": -0.17651399691023,
            "coeff_ACH50": 0.0255147565251867,
        },
        "Vented Crawlspace_Med": {
            "Intercept": 1.18936943365758,
            "coeff_footprint": 0.0640358403055768,
            "coeff_height": -0.0999325792341555,
            "coeff_ACH50": 0.131563521887011,
        },
        "Vented Crawlspace_High": {
            "Intercept": 0.541665794835799,
            "coeff_footprint": 0.0748564756756913,
            "coeff_height": 0.00547899248162892,
            "coeff_ACH50": 0.269358365472381,
        },
        "Unheated Basement_Low": {
            "Intercept": 1.6054636121344,
            "coeff_footprint": 0.0539986426948462,
            "coeff_height": -0.177196676842448,
            "coeff_ACH50": 0.025990856810172,
        },
        "Unheated Basement_Med": {
            "Intercept": 1.19506301644098,
            "coeff_footprint": 0.0636205769686148,
            "coeff_height": -0.100186946453521,
            "coeff_ACH50": 0.130811075329455,
        },
        "Unheated Basement_High": {
            "Intercept": 0.549378963778551,
            "coeff_footprint": 0.074516240809454,
            "coeff_height": 0.004815693684798,
            "coeff_ACH50": 0.26814686727753,
        },
        "Heated Basement_Low": {
            "Intercept": 1.23129226756326,
            "coeff_footprint": 0.0954891411911133,
            "coeff_height": -0.167483919772096,
            "coeff_ACH50": 0.0481161923744135,
        },
        "Heated Basement_Med": {
            "Intercept": 0.855140824123791,
            "coeff_footprint": 0.0920570038711215,
            "coeff_height": -0.0919666012731126,
            "coeff_ACH50": 0.202647584023343,
        },
        "Heated Basement_High": {
            "Intercept": 0.389139840435075,
            "coeff_footprint": 0.096817467876815,
            "coeff_height": -0.0242709692178634,
            "coeff_ACH50": 0.326247837260171,
        },
    }
    return attic_infiltration_coeff_dict

def make_crawl_infiltration_coeff_dict():
    crawl_infiltration_coeff_dict = {
        "Vented Crawlspace_Low": {
            "Intercept": -0.57831567002439,
            "coeff_footprint": 0.598333210175362,
            "coeff_height": -0.0339554160401319,
            "coeff_ACH50": -0.00335138196797992,
        },
        "Vented Crawlspace_Med": {
            "Intercept": -0.683820631214255,
            "coeff_footprint": 0.61523330083822,
            "coeff_height": -0.0378108768305732,
            "coeff_ACH50": -0.0130367930108907,
        },
        "Vented Crawlspace_High": {
            "Intercept": -0.833135093128905,
            "coeff_footprint": 0.638219665153735,
            "coeff_height": -0.0405001563027068,
            "coeff_ACH50": -0.0214967560735974,
        },
        "Unheated Basement_Low": {
            "Intercept": -0.0819476129537362,
            "coeff_footprint": 0.531571799551593,
            "coeff_height": -0.0106147046591054,
            "coeff_ACH50": -0.00117380445863238,
        },
        "Unheated Basement_Med": {
            "Intercept": -0.105903565440005,
            "coeff_footprint": 0.535528403019468,
            "coeff_height": -0.0113518891287177,
            "coeff_ACH50": -0.00402690614571452,
        },
        "Unheated Basement_High": {
            "Intercept": -0.138301270286122,
            "coeff_footprint": 0.540410560453106,
            "coeff_height": -0.0113009258336327,
            "coeff_ACH50": -0.00604037052112423,
        },
    }
    return crawl_infiltration_coeff_dict