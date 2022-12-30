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