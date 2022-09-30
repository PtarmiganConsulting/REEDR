def validate(input_value, variable_name, input_type, low, high):
    if input_type == "integer":
        if input_value >= low and input_value <= high:
            return input_value
        else:
            raise Exception