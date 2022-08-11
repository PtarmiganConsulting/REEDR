#--------------------------------------------------------------------------
#$ Notes
# - this is the prototype txt file maker, let me know if it needs different or expanded functionality, or a different file structure
# - variable names could probably be better, will make final version more readable
# - this will be a much shorter file ultimately, as all of the major operations can be performed with a repeatable function
# - to get the gist of how it works, look at any main section
#--------------------------------------------------------------------------
import pandas as pd
# from pprint import pprint

#--------------------------------------------------------------------------
#$ MainGeometry Writer
text = "" # this becomes the big string that is written to each text file
df = pd.read_csv("MainGeometry.csv")

list_of_rows = []
columns_as_list = df.columns


range_grabber = len(df) - 1 # num of rows, should probably rename this -- used as range to iterate over variable # of rows
counter = 0
for _ in range(range_grabber): # this loop turns every row into a list, and then makes a list of those lists for iteration
    row_as_list = list(df.loc[counter])
    list_of_rows.append(row_as_list)
    counter += 1
# pprint(list_of_rows)

for i in range(range_grabber):
    row = list_of_rows[i]
    # row_re = row.copy()
    # row_re.reverse()
    for ii in range(len(row)):
        # the next lines the default values for a line of the text file
        field = f"!- {columns_as_list[ii]}"
        row_val = row[ii]
        tab = "     "
        separator = ",  "
        carriage = "\n"
        if row.index(row_val) == 0: # first row has no tab or column label, this catches and corrects those rows
            tab = ""
            field = ""
        if ii == len(row) - 1: # last rows have a different separator and carriage length, this catches and corrects those rows
            separator = ";  "
            carriage = "\n\n"
        text += f"{tab}{row_val}{separator}{field}{carriage}" # universal template that can become any line we need

with open('MainGeometry.txt', 'w') as text_file: # finally, the text file is written
    text_file.write(text)
#--------------------------------------------------------------------------
#$ MainWindows
text = "" # this becomes the big string that is written to each text file
df = pd.read_csv("MainWindows.csv")

list_of_rows = []
columns_as_list = df.columns


range_grabber = len(df) - 1 # num of rows, should probably rename this -- used as range to iterate over variable # of rows
counter = 0
for _ in range(range_grabber): # this loop turns every row into a list, and then makes a list of those lists for iteration
    row_as_list = list(df.loc[counter])
    list_of_rows.append(row_as_list)
    counter += 1
# pprint(list_of_rows)

for i in range(range_grabber):
    row = list_of_rows[i]
    # row_re = row.copy()
    # row_re.reverse()
    for ii in range(len(row)):
        # the next lines the default values for a line of the text file
        field = f"!- {columns_as_list[ii]}"
        row_val = row[ii]
        tab = "     "
        separator = ",  "
        carriage = "\n"
        if row.index(row_val) == 0: # first row has no tab or column label, this catches and corrects those rows
            tab = ""
            field = ""
        if ii == len(row) - 1: # last rows have a different separator and carriage length, this catches and corrects those rows
            separator = ";  "
            carriage = "\n\n"
        text += f"{tab}{row_val}{separator}{field}{carriage}" # universal template that will print any line we need

with open('MainWindows.txt', 'w') as text_file: # finally, the text file is written
    text_file.write(text)

#--------------------------------------------------------------------------
#$ NonSlabGeometryAdder
text = "" # this becomes the big string that is written to each text file
df = pd.read_csv("NonSlabGeometryAdder.csv")

list_of_rows = []
columns_as_list = df.columns


range_grabber = len(df) - 1 # num of rows, should probably rename this -- used as range to iterate over variable # of rows
counter = 0
for _ in range(range_grabber): # this loop turns every row into a list, and then makes a list of those lists for iteration
    row_as_list = list(df.loc[counter])
    list_of_rows.append(row_as_list)
    counter += 1
# pprint(list_of_rows)

for i in range(range_grabber):
    row = list_of_rows[i]
    # row_re = row.copy()
    # row_re.reverse()
    for ii in range(len(row)):
        # the next lines the default values for a line of the text file
        field = f"!- {columns_as_list[ii]}"
        row_val = row[ii]
        tab = "     "
        separator = ",  "
        carriage = "\n"
        if row.index(row_val) == 0: # first row has no tab or column label, this catches and corrects those rows
            tab = ""
            field = ""
        if ii == len(row) - 1: # last rows have a different separator and carriage length, this catches and corrects those rows
            separator = ";  "
            carriage = "\n\n"
        text += f"{tab}{row_val}{separator}{field}{carriage}" # universal template that will print any line we need

with open('NonSlabGeometryAdder.txt', 'w') as text_file: # finally, the text file is written
    text_file.write(text)

#--------------------------------------------------------------------------
#$ SecondStoryGeometryAdder

text = "" # this becomes the big string that is written to each text file
df = pd.read_csv("SecondStoryGeometryAdder.csv")

list_of_rows = []
columns_as_list = df.columns


range_grabber = len(df) - 1 # num of rows, should probably rename this -- used as range to iterate over variable # of rows
counter = 0
for _ in range(range_grabber): # this loop turns every row into a list, and then makes a list of those lists for iteration
    row_as_list = list(df.loc[counter])
    list_of_rows.append(row_as_list)
    counter += 1
# pprint(list_of_rows)

for i in range(range_grabber):
    row = list_of_rows[i]
    # row_re = row.copy()
    # row_re.reverse()
    for ii in range(len(row)):
        # the next lines the default values for a line of the text file
        field = f"!- {columns_as_list[ii]}"
        row_val = row[ii]
        tab = "     "
        separator = ",  "
        carriage = "\n"
        if row.index(row_val) == 0: # first row has no tab or column label, this catches and corrects those rows
            tab = ""
            field = ""
        if ii == len(row) - 1: # last rows have a different separator and carriage length, this catches and corrects those rows
            separator = ";  "
            carriage = "\n\n"
        text += f"{tab}{row_val}{separator}{field}{carriage}" # universal template that will print any line we need

with open('SecondStoryGeometryAdder.txt', 'w') as text_file: # finally, the text file is written
    text_file.write(text)


#--------------------------------------------------------------------------
#$ SecondStoryWindowAdder

text = "" # this becomes the big string that is written to each text file
df = pd.read_csv("SecondStoryWindowAdder.csv")

list_of_rows = []
columns_as_list = df.columns


range_grabber = len(df) - 1 # num of rows, should probably rename this -- used as range to iterate over variable # of rows
counter = 0
for _ in range(range_grabber): # this loop turns every row into a list, and then makes a list of those lists for iteration
    row_as_list = list(df.loc[counter])
    list_of_rows.append(row_as_list)
    counter += 1
# pprint(list_of_rows)

for i in range(range_grabber):
    row = list_of_rows[i]
    # row_re = row.copy()
    # row_re.reverse()
    for ii in range(len(row)):
        # the next lines the default values for a line of the text file
        field = f"!- {columns_as_list[ii]}"
        row_val = row[ii]
        tab = "     "
        separator = ",  "
        carriage = "\n"
        if row.index(row_val) == 0: # first row has no tab or column label, this catches and corrects those rows
            tab = ""
            field = ""
        if ii == len(row) - 1: # last rows have a different separator and carriage length, this catches and corrects those rows
            separator = ";  "
            carriage = "\n\n"
        text += f"{tab}{row_val}{separator}{field}{carriage}" # universal template that will print any line we need

with open('SecondStoryWindowAdder.txt', 'w') as text_file: # finally, the text file is written
    text_file.write(text)

#--------------------------------------------------------------------------
#$ ThirdStoryGeometryAdder

text = "" # this becomes the big string that is written to each text file
df = pd.read_csv("ThirdStoryGeometryAdder.csv")

list_of_rows = []
columns_as_list = df.columns


range_grabber = len(df) - 1 # num of rows, should probably rename this -- used as range to iterate over variable # of rows
counter = 0
for _ in range(range_grabber): # this loop turns every row into a list, and then makes a list of those lists for iteration
    row_as_list = list(df.loc[counter])
    list_of_rows.append(row_as_list)
    counter += 1
# pprint(list_of_rows)

for i in range(range_grabber):
    row = list_of_rows[i]
    # row_re = row.copy()
    # row_re.reverse()
    for ii in range(len(row)):
        # the next lines the default values for a line of the text file
        field = f"!- {columns_as_list[ii]}"
        row_val = row[ii]
        tab = "     "
        separator = ",  "
        carriage = "\n"
        if row.index(row_val) == 0: # first row has no tab or column label, this catches and corrects those rows
            tab = ""
            field = ""
        if ii == len(row) - 1: # last rows have a different separator and carriage length, this catches and corrects those rows
            separator = ";  "
            carriage = "\n\n"
        text += f"{tab}{row_val}{separator}{field}{carriage}" # universal template that will print any line we need

with open('ThirdStoryGeometryAdder.txt', 'w') as text_file: # finally, the text file is written
    text_file.write(text)

#--------------------------------------------------------------------------
#$ ThirdStoryWindowAdder

text = "" # this becomes the big string that is written to each text file
df = pd.read_csv("ThirdStoryWindowAdder.csv")

list_of_rows = []
columns_as_list = df.columns


range_grabber = len(df) - 1 # num of rows, should probably rename this -- used as range to iterate over variable # of rows
counter = 0
for _ in range(range_grabber): # this loop turns every row into a list, and then makes a list of those lists for iteration
    row_as_list = list(df.loc[counter])
    list_of_rows.append(row_as_list)
    counter += 1
# pprint(list_of_rows)

for i in range(range_grabber):
    row = list_of_rows[i]
    # row_re = row.copy()
    # row_re.reverse()
    for ii in range(len(row)):
        # the next lines the default values for a line of the text file
        field = f"!- {columns_as_list[ii]}"
        row_val = row[ii]
        tab = "     "
        separator = ",  "
        carriage = "\n"
        if row.index(row_val) == 0: # first row has no tab or column label, this catches and corrects those rows
            tab = ""
            field = ""
        if ii == len(row) - 1: # last rows have a different separator and carriage length, this catches and corrects those rows
            separator = ";  "
            carriage = "\n\n"
        text += f"{tab}{row_val}{separator}{field}{carriage}" # universal template that will print any line we need

with open('ThirdStoryWindowAdder.txt', 'w') as text_file: # finally, the text file is written
    text_file.write(text)

