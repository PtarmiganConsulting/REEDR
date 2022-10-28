import os

def validate(input_name, input_value, input_type, value_low, value_high, valid_list, file_path=None):
    
    #print(input_name) for debugging

    #First check if string is empty
    if str(input_value) == "nan":
        print("\n*** ERROR: " + str(input_name) + " field cannot be blank. Please specify a valid " + str(input_name) + ". ***\n")
        raise Exception
    
    # check if input is within valid list
    if input_type == "list":
        valid_list_string = "\n".join(valid_list)
        if input_value in valid_list:
            return input_value
        else:
            print("\n*** ERROR: Invalid value entered for the data field \"" + str(input_name) + "\" ***")
            print("This data field must be set to one of the following allowed values: \n\n" + valid_list_string + "\n")
            raise Exception

    # check if input is a file that exists
    if input_type == "file":
        #... then check if file exists
        filename = input_value + ".txt"
        if os.path.exists(os.path.join(file_path, filename)) == True:
            return input_value
        else:
            print("\n*** ERROR: Could not find " + str(input_name) + " called: " + str(input_value) + "\" ***")
            print("Make sure the file " + str(filename) + " exists at the path: " + str(file_path) + "\n")
            raise Exception
    
    # check if input is number between a low and high value
    if input_type == "num_between":
        if input_value >= value_low and input_value <= value_high:
            return input_value
        else:
            print("\n*** ERROR: " + str(input_name) + " must be a number between " + str(value_low) + " and " + str(value_high) + " ***\n")
            raise Exception

    # check if input is number between a low and high value
    if input_type == "num_not_zero":
        if input_value != 0 and input_value / input_value == 1:
            return input_value
        else:
            print("\n*** ERROR: " + str(input_name) + " must be numeric and greater than zero. ***\n")
            raise Exception

    # check if input is number between a low and high value
    if input_type == "any_num":
        if type(input_value) == str:
            print("\n*** ERROR: " + str(input_name) + " must be numeric. ***\n")
            raise Exception
        elif input_value == 0:
            return input_value
        elif input_value / input_value == 1:
            return input_value
        else:
            print("\n*** ERROR: " + str(input_name) + " must be numeric. ***\n")
            raise Exception

def convert_capacity(input_units, input_value):

    if input_units == "kW":
        capacity_in_W = 1000 * input_value
    elif input_units == "kBtu/h":
        capacity_in_W = 293.07107 * input_value
    elif input_units == "ton":
        capacity_in_W = 3516.8528421 * input_value
    else:
        print("\n*** ERROR: Could not convert capacity to Watts. ***\n")
        raise Exception
    
    return capacity_in_W