# special thanks to Katja

import pandas as pd
import os
from pathlib import Path
# from pprint import pprint as pprint
from statistics import mean

#########################################################################


cwd = Path(os. getcwd())
# ext_path = 'Projects\\birmrock2'
ext_path = 'Projects\\timestep106'
# filename = "RunReport_birmrockdev.xlsx"
# filename = "RunReport_birmrockdev.xlsx"
# filename = "RunReport_birmrock2.xlsx"
filename = "RunReport_timestep106.xlsx"
output_filename = "HDDs.xlsx"
# filename = "Kal.xlsx"
full_path = os.path.join(cwd, ext_path, filename)
output_path = os.path.join(cwd, ext_path, output_filename)


df = pd.read_excel(full_path)

values = list(df.iloc[:,0]) # dates and hours
values_2 = list(df.iloc[:,1]) # month
values_3 = list(df.iloc[:,2]) # day
values_4 = list(df.iloc[:,4]) # runlabel
values_5 = list(df.iloc[:,5]) # air temp

length_val = len(values) # length of the data sheet

tuples = []

for i in range(length_val):
    new_tup = (values_2[i], values_3[i], values_4[i], values_5[i])
    tuples.append(new_tup)

    # each row becomes a tuple of month, day, runlabel, and airtemp

runlabels = [] # a list of runlabels is extracted

for _ in values_4:
    if _ not in runlabels:
        runlabels.append(_)


dates = [] # a list of dates in a standard year are constructed

for i in range(len(tuples)):
    if str(tuples[i][0]) + "-" +  str(tuples[i][1]) not in dates:
        dates.append(str(tuples[i][0]) + "-" + str(tuples[i][1]))

############################################################################

the_structure = [] # first stage our ultimate export data structure

for _ in runlabels:
    the_structure.append([_, []])

    # make a list of lists each containing a unique runlabel and and empty list

for _ in the_structure:
    for date in dates:
        _[1].append([date])

    # each runlabel is now paired with a list containing every date in its own list(!)

for runlabel_list in the_structure:
    for tupe in tuples:
        if tupe[2] == runlabel_list[0]:
            for date_list in runlabel_list[1]:
                if str(tupe[0]) + "-" + str(tupe[1]) == date_list[0]:
                    date_list.append(tupe[3])

    # for every runlabel, each date list now also contains all the air temperatures on that date
                
new_structure = [] # recreate the structure, but this time containing the mean of the temp in every date list

for _ in runlabels:
    new_structure.append([_, []])

for runlabel_list in new_structure:
    for runlabel_list_OG in the_structure:
        if runlabel_list[0] == runlabel_list_OG[0]:
            for datelist in runlabel_list_OG[1]:
                new_data = []
                new_data.append(datelist[0])
                datelist.pop(0)
                new_data.append(mean(datelist))
                runlabel_list[1].append(new_data)

final_structure = [] # now pair every run label with the sum of every date's HDD

for runlabel_list in new_structure:
    output_pair = [runlabel_list[0]]
    hdd65 = []
    for pair in runlabel_list[1]:
        compute_hdd65 = 65 - pair[1]
        if compute_hdd65 < 0:
            compute_hdd65 = 0
        hdd65.append(compute_hdd65)
    output_pair.append(sum(hdd65))
    final_structure.append(output_pair)

output_vals = []
output_runlabels = []


# split runlabels and HDDS into their own vars for output spreadsheet
for pair in final_structure:
    output_runlabels.append(pair[0])
    output_vals.append(pair[1])

data = {'runlabel':output_runlabels, 'HDDs':output_vals}

new_df = pd.DataFrame(data)

print(new_df)

with pd.ExcelWriter(output_path) as writer:
    new_df.to_excel(writer, sheet_name="HDD Results", index=False)