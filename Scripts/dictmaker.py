#*******************************************************************************************************************************************************************

#Copyright (C) 2023 Ptarmigan Consulting LLC

#This file is part of REEDR.

#REEDR is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
#either version 3 of the License, or (at your option) any later version.

#REEDR is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
#PURPOSE. See the GNU General Public License for more details.

#You should have received a copy of the GNU General Public License along with REEDR. If not, see <https://www.gnu.org/licenses/>. 

#*******************************************************************************************************************************************************************

import pandas as pd

def dict_maker(csv_path):
    new_dict = {}
    input_df = pd.read_csv(csv_path)


    row_range = len(input_df)
    columns = input_df.columns
    list_cols = list(columns)

    list_cols.pop(0)

    for i in range(row_range):
        sub_dict = {}
        row = list(input_df.loc[i])
        row_name = row[0]
        row.pop(0)
        row_adj_len = len(row)

        for ii in range(row_adj_len):
            if row[ii] == "$":
                row[ii] = ""

            if str(row[ii]) == "nan":
                row[ii] = ""
            
            # for handling some type errors 
            try:
                row[ii] = float(row[ii])
            except:
                pass

        for ii in range(row_adj_len):
            sub_dict.update({list_cols[ii]:row[ii]})
        
        new_dict.update({row_name:sub_dict})
    
    return new_dict