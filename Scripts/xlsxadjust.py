from openpyxl import load_workbook
import pandas as pd

# need to give it eyes
def adapt_spreadsheet(standard_filename):

    df = pd.read_excel(standard_filename)
    # df_all = pd.read_excel(standard_filename, sheet_name=None)
    # df = df_all[0]
    df2 = pd.read_excel(standard_filename, sheet_name=1)
    df3 = pd.read_excel(standard_filename, sheet_name=2)

    timedata = list(df.iloc[:,0])
    sheet_len = len(df)

    month_vals = []
    day_vals = []
    hod_vals = []

    for i in range(sheet_len):
        input_val = str(timedata[i])
        input_scrub = input_val.split(" ") # needs to have "" values removed

        while "" in input_scrub:
            input_scrub.remove("")

        input_scrub = [input_scrub[0], input_scrub[1] ] # [month/day], hod] ex: ['01/01', '01:00:00']

        month, day = input_scrub[0].split("/")[0], input_scrub[0].split("/")[1] # ['month', 'day'] ex: ['01', '01']
        hod = input_scrub[1].split(":")[0]

        month_vals.append(month), day_vals.append(day), hod_vals.append(hod)

    df.insert(1, "Month", month_vals)
    df.insert(2, "Day", day_vals)
    df.insert(3, "HOD", hod_vals)

    with pd.ExcelWriter(standard_filename) as writer:
        # df.to_excel(writer, sheet_name="Model Out", index=False)
        df.to_excel(writer, sheet_name="Model Out", index=False)
        df2.to_excel(writer, sheet_name="Model In", index=False)
        df3.to_excel(writer, sheet_name="Run Characteristics", index=False)