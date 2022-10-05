def validate(input_value, input_type, value_low, value_high, valid_list):
    
    # check if input is within valid list
    if input_type == "list":
        if input_value in valid_list:
            return input_value
        else:
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