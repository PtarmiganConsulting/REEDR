import os

def validate(input_name, input_value, input_type, value_low, value_high, valid_list, file_path=None):
    
    # check if input is within valid list
    if input_type == "list":
        valid_list_string = "\n".join(valid_list)
        if input_value in valid_list:
            return input_value
        else:
            print("\n*** ERROR: Invalid value entered for the data field \"" + str(input_name) + "\" ***")
            print("This data field must be set to one of the following allowed values: \n\n" + valid_list_string + "\n")
            raise Exception

    # check if input is number between a low and high value
    if input_type == "num_between":
        if input_value >= value_low and input_value <= value_high:
            return input_value
        else:
            raise Exception

    # check if input is number between a low and high value
    if input_type == "num_not_zero":
        if input_value != 0 and input_value / input_value == 1:
            return input_value
        else:
            raise Exception

    # check if input is number between a low and high value
    if input_type == "any_num":
        if int(input_value) == 0:
            return input_value
        elif input_value / input_value == 1:
            return input_value
        else:
            raise Exception

    # check if input is a file that exists
    if input_type == "file":
        filename = input_value + ".txt"
        if os.path.exists(os.path.join(file_path, filename)) == True:
            return input_value
        else:
            raise Exception